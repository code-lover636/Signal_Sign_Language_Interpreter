import pickle

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np


data_dict = pickle.load(open('./data.pickle', 'rb'))

data = np.asarray(data_dict['data'])
signs = np.asarray(data_dict['signs'])

x_train, x_test, y_train, y_test = train_test_split(data, signs, test_size=0.2, shuffle=True, stratify=signs)

model = RandomForestClassifier()

model.fit(x_train, y_train)

y_predict = model.predict(x_test)

score = accuracy_score(y_predict, y_test)

print('{}% of samples were classified correctly !'.format(score * 100))

f = open('model.pickle', 'wb')
pickle.dump(model, f)
f.close()
