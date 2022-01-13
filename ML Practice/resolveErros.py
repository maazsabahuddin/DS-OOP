import keras
import numpy as np
import pandas as pd
import tensorflow as tf

from keras.models import Sequential
from sklearn.preprocessing import LabelEncoder
from keras.layers import Dense, Dropout, Embedding, SpatialDropout1D, LSTM, SimpleRNN
from keras.layers.wrappers import Bidirectional
from keras.callbacks import ModelCheckpoint
# from keras.utils import to_categorical

from gensim import corpora

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

import re
import random


NO_OF_ROWS_TO_READ = 1000

df = pd.read_csv('questions.csv', delimiter=',', nrows=NO_OF_ROWS_TO_READ)
df2 = pd.read_csv('question_tags.csv', delimiter=',', nrows=NO_OF_ROWS_TO_READ)
df = df.merge(df2, left_on='Id', right_on='Id')
df['Created_year'] = pd.DatetimeIndex(df['CreationDate']).year
df['Created_month'] = pd.DatetimeIndex(df['CreationDate']).month
df['Deleted_year'] = pd.DatetimeIndex(df['DeletionDate']).year
df['Deleted_month'] = pd.DatetimeIndex(df['DeletionDate']).month
print(df.columns)


def replace_tags(list_of_tokens: list) -> list:
    treated_tokens = []
    for token in list_of_tokens:
        if token == '?':
            treated_tokens.append('<QST_MARK>')
        elif token == '!':
            treated_tokens.append('<EXC_MARK>')
        else:
            treated_tokens.append(token)

    return treated_tokens


def pad_sequence(list_of_treated_tokens: list, max_len: int) -> list:
    actual_len = len(list_of_treated_tokens)
    if actual_len < max_len:
        padded_list = ['<PAD>' for _ in range(max_len - actual_len)] + list_of_treated_tokens
    elif actual_len > max_len:
        padded_list = list_of_treated_tokens[:max_len]
    else:
        padded_list = list_of_treated_tokens

    return padded_list


def pre_processing(text: str) -> list:
    # print(text)
    text = re.sub('([!?])', r' \1 ', text)
    text = text.lower().split()

    #  adding tokens
    list_with_tokens = replace_tags(text)

    #  padding the sentence
    padded_list = pad_sequence(list_with_tokens, max_len=len(df.Tag.unique()))
    # print(padded_list)
    return padded_list


df['tags_title'] = df.Tag.apply(pre_processing)
encoder = corpora.Dictionary(df.tags_title)

x = np.array([encoder.doc2idx(s) for s in df.tags_title])

# x = tf.keras.utils.to_categorical([random.randint(0, len(df.Tag.unique())) for i in range(0, len(df.Tag.unique()))],
#                                   num_classes=len(df.Tag.unique()))
# print("Shape of X", x.shape)

y = df.Tag
_uniqueTagsValue = {}
count = 0
for val in df.Tag.unique():
    _uniqueTagsValue.update({val: count})
    count += 1

print(f"Length of unique Tags {len(df.Tag.unique())}")
y_ann = tf.keras.utils.to_categorical(y.map(_uniqueTagsValue), num_classes=len(df.Tag.unique()))
# print("Shape of Y", y_ann.shape)

x_train, x_valid, y_train, y_valid = train_test_split(x, y_ann, test_size=0.2)

# print("\n\nCROSS VAL SCORE: SVC")
# print(cross_val_score(SVC(), x, y, cv=20))
#
# print("\n\nCROSS VAL SCORE: RandomForestClassifier")
# print(cross_val_score(RandomForestClassifier(500), x, y, cv=20))

# Model: "sequential model 1"
# print("Model: 'sequential model 1'")
# model = Sequential()
# model.add(Embedding(x.shape[1], 64))
# model.add(SpatialDropout1D(0.2))
# model.add(Bidirectional(LSTM(256, dropout=0.2)))
# model.add(Dense(32, activation='relu'))
# model.add(Dense(16, activation='relu'))
# model.add(Dense(8, activation='relu'))
# model.add(Dense(5, activation='softmax'))
#
# model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# model.summary()

# model.fit(x_train, y_train, batch_size=32, epochs=10, validation_data=(x_valid, y_valid))

# print("X-Train", x_train)
# print("Y-Train", y_train)
# print("X-Train Shape", x_train.shape)
# print("Y-Train Shape", y_train.shape)
# print("X-Valid Shape", x_valid.shape)
# print("Y-Valid Shape", y_valid.shape)

# Model: "sequential model 2"
print("Model: 'sequential model 2'")
model2 = Sequential()
# model2.add(Embedding(x.shape[1], 64))
# model2.add(SpatialDropout1D(0.2))
# model2.add(SimpleRNN(256, dropout=0.2))
# model2.add(Dense(32, activation='relu'))
# model2.add(Dense(16, activation='relu'))
# model2.add(Dense(8, activation='relu'))
# model2.add(Dense(5, activation='softmax'))
model2.add(Dense(100, input_dim=2, activation='relu'))
model2.add(Dense(1, activation='sigmoid'))

model2.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model2.summary()

history = model2.fit(x_train, y_train, validation_data=(x_valid, y_valid), epochs=3, verbose=0)
# model2.fit(x_train, y_train, batch_size=32, epochs=3, validation_data=(x_valid, y_valid))
