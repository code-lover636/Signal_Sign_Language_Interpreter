import cv2
import mediapipe as mp
import pickle
import numpy as np

#model = pickle.load(open('./model.pickle', 'rb'))
# model = model_dict['model']

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, max_num_hands=2, min_detection_confidence=0.8, min_tracking_confidence=0.5)
max_features_per_sample = 171

while cap.isOpened():
    data_aux = []
    x_ = []
    y_ = []
    ret, frame = cap.read()
    H, W, _ = frame.shape
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    results = hands.process(image)
    image.flags.writeable = True
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
        for hand_landmarks in results.multi_hand_landmarks:
            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y

                x_.append(x)
                y_.append(y)

            # for i in range(len(hand_landmarks.landmark)):
            #     x = hand_landmarks.landmark[i].x
            #     y = hand_landmarks.landmark[i].y
            #     data_aux.append(x - min(x_))
            #     data_aux.append(y - min(y_))
        # max_x = max(x_)
        # max_y = max(y_)

        # # x1 = int(min(x_) * W) - 10
        # # y1 = int(min(y_) * H) - 10

        # # x2 = int(max(x_) * W) - 10
        # # y2 = int(max(y_) * H) - 10
        # for i in range(len(x_)):
        #     data_aux.append(x_[i] / max_x)
        #     data_aux.append(y_[i] / max_y)
        
        # # Pad or truncate data_aux to have max_features_per_sample elements
        # if len(data_aux) < max_features_per_sample:
        #         data_aux += [0] * (max_features_per_sample - len(data_aux))
        # elif len(data_aux) > max_features_per_sample:
        #         data_aux = data_aux[:max_features_per_sample]

        # # data.append(data_aux)
        # # signs.append(dir_name)
            
        # prediction = model.predict([np.asarray(data_aux)])

        # predicted_character = prediction[0]

        # # cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 4)
        # # cv2.putText(frame, predicted_character, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3,
        # #             cv2.LINE_AA)
        # print(predicted_character)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    cv2.imshow("frame", image)
    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()