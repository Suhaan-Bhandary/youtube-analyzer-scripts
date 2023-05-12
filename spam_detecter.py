import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB


def isTextSpam(text):
    data = pd.read_csv("./assets/Youtube01.csv")
    # print(data.sample(5)) #This will print 5 random rows from the dataset

    # print(data.isnull().sum())

    # Since we only require content and class columns, we will update our existing datafram to the following
    data = data[['CONTENT', 'CLASS']]

    # We will map 0 to not spam and 1 to span in class column
    data["CLASS"] = data['CLASS'].map({0: "not spam", 1: "spam"})
    # print(data.sample(5))

    x = np.array(data['CONTENT'])
    y = np.array(data['CLASS'])

    """
    As the output of this problem will either be 0 or 1,i.e, the problem of binary classification,
    we can use the Bernoulli Naive Bayes algorithm to train the model:
    """

    cv = CountVectorizer()
    x = cv.fit_transform(x)
    xtrain, xtest, ytrain, ytest = train_test_split(
        x, y, train_size=0.8, random_state=42)

    model = BernoulliNB()
    model.fit(xtrain, ytrain)

    # Its time to check the model by giving spam and non-spam comments
    d = cv.transform([text]).toarray()

    return model.predict(d)[0] == "spam"
