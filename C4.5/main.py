import csv
import arvore_decisao
from sklearn import tree

dataMatrix = []
colInfos = {}
colNames = []

Y = [0, 9]

with open('Cleaned-Data.csv', 'r',) as file:
    reader = csv.reader(file, delimiter = '\t')

    i = 0
    for row in reader:
        if i>0:
            dataMatrix.append(row)

        for att in row:
            if i==0:
                colNames.append(att)
        i += 1


clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)
tree.plot_tree(clf)
