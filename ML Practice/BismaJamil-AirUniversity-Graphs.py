import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


NO_OF_ROWS_TO_READ = None

df1 = pd.read_csv('questions.csv', delimiter=',', nrows=NO_OF_ROWS_TO_READ)
df1.dataframeName = 'questions.csv'
rowsCount, columnsCount = df1.shape
print(f'There are {rowsCount} rows and {columnsCount} columns')
print(df1.columns)


df2 = pd.read_csv('question_tags.csv', delimiter=',', nrows=NO_OF_ROWS_TO_READ)
df2.dataframeName = 'question_tags.csv'
rowsCount2, columnsCount2 = df2.shape
print(f'There are {rowsCount2} rows and {columnsCount2} columns')
print(df2.columns)


df1 = df1.merge(df2, left_on='Id', right_on='Id')
df1['Created_year'] = pd.DatetimeIndex(df1['CreationDate']).year
df1['Created_month'] = pd.DatetimeIndex(df1['CreationDate']).month
df1['Deleted_year'] = pd.DatetimeIndex(df1['DeletionDate']).year
df1['Deleted_month'] = pd.DatetimeIndex(df1['DeletionDate']).month


def created_year_tags():
    """
    This will check that how many tags has been created with the axis of years
    :return:
    """
    plt.figure(figsize=(10, 6))
    sns.countplot(df1['Created_year'])
    plt.show()


def month_wise_count():
    """
    This will check that how many tags has been created in a particular month in the whole dataset
    :return:
    """
    plt.figure(figsize=(10, 8))
    ax = sns.countplot(y=df1['Created_month'])
    plt.yticks(range(12), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    for i, j in enumerate(df1['Created_month'].value_counts().reset_index().sort_values('index')['Created_month']):
        ax.text(10, i, j)
    plt.show()


def top_20_tags():
    """
    This will show the top 20 tags
    :return:
    """
    top20tags = df1['Tag'].value_counts().reset_index().head(20)
    top20tags.columns = ['Tag', 'Counts']

    plt.figure(figsize=(10, 10))
    ax = sns.barplot(x='Counts', y='Tag', data=top20tags)
    for i, j in enumerate(top20tags['Counts']):
        ax.text(100000, i, j)
    plt.show()


def tags_search_by_year():
    """
    Year by year tag searches
    :return:
    """
    plot_group = df1.groupby(['Tag', 'Created_year'])['Created_year'].count()
    plot_group.plot(kind='barh', figsize=(10, 50))
    plt.show()


created_year_tags()
month_wise_count()
top_20_tags()
tags_search_by_year()
