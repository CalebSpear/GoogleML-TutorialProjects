# -*- coding: utf-8 -*-
"""
Created on Sat May 23 14:55:16 2020

@author: caleb
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.metrics import confusion_matrix

# Loading the spam data
# ham is the label for non-spam messages
spam = pd.read_csv('spam.csv', encoding = "latin-1")
spam = spam[['v1', 'v2']]
spam = spam.rename(columns = {'v1': 'label', 'v2': 'text'})

def review_messages(msg):
    # converting messages to lowercase
    msg = msg.lower()
    return msg

spam['text'] = spam['text'].apply(review_messages)

X_train, X_test, y_train, y_test = train_test_split(spam['text'], spam['label'], test_size = 0.3, random_state = 1)
# training the vectorizer 
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(X_train)


svm = svm.SVC(C=1000,gamma = "auto")
svm.fit(X_train, y_train)

X_test = vectorizer.transform(X_test)
y_pred = svm.predict(X_test)

print(confusion_matrix(y_test, y_pred))

