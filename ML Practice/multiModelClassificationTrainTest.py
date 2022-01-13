# Python imports
import pandas as pd

# Framework imports
from numpy import mean
from numpy import std
from sklearn.datasets import make_multilabel_classification
from sklearn.model_selection import RepeatedKFold
from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import accuracy_score


NO_OF_ROWS_TO_READ = 1000
K_MEANS_REPETITIONS_EPOCH = 3
K_MEANS_SPLIT_COUNT = 3


def get_dataset():
    """
    This function will return the dataset frame after preprocessing
    :return:
    """
    df1 = pd.read_csv('questions.csv', delimiter=',', nrows=NO_OF_ROWS_TO_READ)
    df1.dataframeName = 'questions.csv'
    rows_count, columns_count = df1.shape
    print(f'Fetched {rows_count} rows and found {columns_count} columns')
    # print(df1.columns)

    df2 = pd.read_csv('question_tags.csv', delimiter=',', nrows=NO_OF_ROWS_TO_READ)
    df2.dataframeName = 'question_tags.csv'
    rows_count2, columns_count2 = df2.shape
    print(f'Fetched {rows_count2} rows and found {columns_count2} columns')
    # print(df2.columns)

    df1 = df1.merge(df2, left_on='Id', right_on='Id')
    df1['Created_year'] = pd.DatetimeIndex(df1['CreationDate']).year
    df1['Created_month'] = pd.DatetimeIndex(df1['CreationDate']).month
    df1['Deleted_year'] = pd.DatetimeIndex(df1['DeletionDate']).year
    df1['Deleted_month'] = pd.DatetimeIndex(df1['DeletionDate']).month
    print(f"Dataset: \n{df1}")
    return make_multilabel_classification(n_samples=NO_OF_ROWS_TO_READ if NO_OF_ROWS_TO_READ else 1000, n_features=10,
                                          n_classes=3, n_labels=2, random_state=1)


def get_model(n_inputs, n_outputs):
    """
    This function will return the model
    :param n_inputs:
    :param n_outputs:
    :return:
    """
    model = Sequential()
    model.add(Dense(20, input_dim=n_inputs, kernel_initializer='he_uniform', activation='relu'))
    model.add(Dense(n_outputs, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam')
    return model


def evaluate_model(x=None, y=None):
    """
    This function will apply KMeans algorithm on the dataset according the given split_count and repetitions
    KMeans split the dataset into 3 states (2 of them for training and 1 of them for testing).
    This will be done according to the no_of_repetitions defined. For each repetition it will store the accuracy of the
    dataset with respect to the model, and in the end it will get the mean of all the accuracies.
    :param x:
    :param y:
    :return:
    """
    if len(x) < 0 or len(y) < 0:
        print("Invalid length")
        return 0.00

    if K_MEANS_SPLIT_COUNT == 0 or K_MEANS_REPETITIONS_EPOCH == 0:
        print("Invalid KMeans Value Count or Invalid KMeans Epoch")
        return 0.00

    _results = list()
    n_inputs, n_outputs = x.shape[1], y.shape[1]

    # define evaluation procedure
    cv = RepeatedKFold(n_splits=K_MEANS_SPLIT_COUNT, n_repeats=K_MEANS_REPETITIONS_EPOCH, random_state=1)

    # enumerate folds
    for train_ix, test_ix in cv.split(x):
        # prepare data
        x_train, x_test = x[train_ix], x[test_ix]
        y_train, y_test = y[train_ix], y[test_ix]

        # define model
        model = get_model(n_inputs, n_outputs)

        # fit model
        model.fit(x_train, y_train, verbose=0, epochs=100)

        # make a prediction on the test set
        yhat = model.predict(x_test)
        # round probabilities to class labels
        yhat = yhat.round()

        # calculate accuracy
        acc = accuracy_score(y_test, yhat)

        # appending results to calculate mean
        print('>>> {0:.3f}'.format(acc))
        _results.append(acc)
    return _results


# Get the dataset
x1, y1 = get_dataset()

# Applying KMeans Algorithm and waiting ot get the results by n number of epochs
print(">>> Evaluating model now...")
result = evaluate_model(x1, y1)

print('>>> Accuracy: %.3f (%.3f)' % (mean(result), std(result)))
