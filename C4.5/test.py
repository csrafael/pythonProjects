import pandas as pd
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation

feature_cols = ['Fever','Tiredness','Dry-Cough','Difficulty-in-Breathing','Sore-Throat']

dataFrame = pd.read_csv("Cleaned-Data.csv")

dataFrame.drop("Country",axis=1,inplace=True)
dataFrame.drop("Contact_No",axis=1,inplace=True)
dataFrame.drop("Age_0-9",axis=1,inplace=True)

X = dataFrame[feature_cols]
y = dataFrame.Contact_Yes

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) # 70% training and 30% test

clf = DecisionTreeClassifier(criterion="entropy")

# Train Decision Tree Classifer
clf = clf.fit(X_train,y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
tree.plot_tree(clf)
