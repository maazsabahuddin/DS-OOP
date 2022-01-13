import numpy as np
import pandas as pd

from keras.models import Sequential
from keras.layers import Dense
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt


NO_OF_ROWS_TO_READ = 10000


df_questions = pd.read_csv("questions.csv", nrows=NO_OF_ROWS_TO_READ, usecols=['Id', 'Score', 'AnswerCount'],
                           encoding='latin1')
# df_questions = pd.read_csv("questions.csv", parse_dates=["ClosedDate", "CreationDate", "DeletionDate"])
df_questions = df_questions.dropna()
# print(df_questions.head(15))

X = df_questions.values.astype('float')

df_question_tags = pd.read_csv("question_tags.csv", nrows=NO_OF_ROWS_TO_READ, encoding='latin1')
df_question_tags = df_question_tags.dropna()
# print(df_question_tags.head(15))

y = df_question_tags.values

model = Sequential()
model.add(Dense(16, activation='relu', input_shape=(3,)))
model.add(Dense(8, activation='relu'))
model.add(Dense(4, activation='relu'))
model.add(Dense(2, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])
# model.compile(loss='binary_crossentropy', optimizer='adam')


encoder = LabelEncoder()
encoder.fit(y[:, 1])
encoded_Y = encoder.transform(y[:, 1])
print("Encoded Y1")
print(encoded_Y[1])

np_y = np.array([])
for _, tag in enumerate(encoded_Y):
    np_y = np.append(np_y, tag)

Y = np.column_stack((y[:, 0], np_y)).astype('float')

history = model.fit(X, Y, verbose=0,
                     epochs=100,
                     batch_size=128,
                     validation_split=0.4)

acc = history.history['acc']
loss = history.history['loss']
print(acc)
print(loss)

plt.plot(range(len(acc)), acc, 'b', label="training accuracy", color='g')
plt.plot(range(len(loss)), loss, 'b', label="training loss", color='r')
plt.show()
