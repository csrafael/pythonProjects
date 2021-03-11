import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn import metrics

feature_cols = ['Fever','Tiredness','Dry-Cough','Difficulty-in-Breathing','Sore-Throat']

dataFrame = pd.read_csv("Cleaned-Data.csv")

dataFrame.drop("Country",axis=1,inplace=True)
dataFrame.drop("Contact_No",axis=1,inplace=True)
dataFrame.drop("Age_0-9",axis=1,inplace=True)
dataFrame.drop("Age_10-19",axis=1,inplace=True)
dataFrame.drop("Age_20-24",axis=1,inplace=True)
dataFrame.drop("Age_25-59",axis=1,inplace=True)
dataFrame.drop("Age_60+",axis=1,inplace=True)
dataFrame.drop("None_Sympton",axis=1,inplace=True)
dataFrame.drop("None_Experiencing",axis=1,inplace=True)
dataFrame.drop("Gender_Female",axis=1,inplace=True)
dataFrame.drop("Gender_Male",axis=1,inplace=True)
dataFrame.drop("Gender_Transgender",axis=1,inplace=True)

X = dataFrame[feature_cols]
y = dataFrame.Contact_Yes

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

clf = DecisionTreeClassifier(criterion="entropy")

clf = clf.fit(X_train,y_train)

y_pred = clf.predict(X_test)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
tree.plot_tree(clf)
