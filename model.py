import pickle
from sklearn.ensemble import RandomForestClassifier
import numpy as np


data_dict = pickle.load(open('./data.pickle', 'rb'))
data = np.asarray(data_dict['data'])
labels = np.asarray(data_dict['labels'])

model = RandomForestClassifier()
model.fit(data, labels)

f = open('model.p', 'wb')
pickle.dump(model, f)
f.close()
