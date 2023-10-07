import os
import pickle
import mediapipe as mp
import cv2
import numpy as np

hands = mp.solutions.hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

data = []
signs = []

# Define the maximum number of features (landmark coordinates) per sample
max_features_per_sample = 171

for dir_name in os.listdir("./data"):
    counter = 0
    for img_path in os.listdir(os.path.join('./data', dir_name)):
        if counter >= 1000:  # Limit to 10 samples per class
            break

        data_aux = []
        x_ = []
        y_ = []

        try:
            img = cv2.imread(os.path.join('./data', dir_name, img_path))
            if img is None:
                raise Exception("Failed to load image: {}".format(img_path))
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        except Exception as e:
            print("Error loading image:", e)
            print(dir_name,img_path)
            continue  # Skip this image and move to the next one


        results = hands.process(img_rgb)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y

                    x_.append(x)
                    y_.append(y)

            max_x = max(x_)
            max_y = max(y_)

            for i in range(len(x_)):
                data_aux.append(x_[i] / max_x)
                data_aux.append(y_[i] / max_y)

            # Pad or truncate data_aux to have max_features_per_sample elements
            if len(data_aux) < max_features_per_sample:
                data_aux += [0] * (max_features_per_sample - len(data_aux))
            elif len(data_aux) > max_features_per_sample:
                data_aux = data_aux[:max_features_per_sample]

            data.append(data_aux)
            signs.append(dir_name)

        counter += 1

# Convert data and signs to NumPy arrays
data = np.array(data)
signs = np.array(signs)

# Save the generated dataset
f = open('./data.pickle', 'wb')
pickle.dump({'data': data, 'signs': signs}, f)
f.close()
