



import pandas as pd
from sklearn.tree import  export_graphviz
import pydotplus
from  sklearn.model_selection import  train_test_split
from  sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from  BestFeatureFunction import bestFunction


df = pd.read_csv('videodata.csv')

columns = df.columns

x = df[columns[0:len(columns)-1]].values
y = df[columns[len(columns)-1]].values

print(list(set(y)))

xtrain, xtest, ytrain, ytest =  train_test_split(x,y,random_state=0)


clf  = DecisionTreeClassifier()

clf.fit(xtrain,ytrain)

ypred_train = clf.predict(xtrain)
ypred_test = clf.predict(xtest)

features = columns[0:len(columns)-1]


dot_data = export_graphviz(clf,out_file=None,feature_names=columns[0:len(columns)-1],class_names=['Yes','No'])
total, best = bestFunction(dot_data,features)
print("Total data of features : ",total)
print("Best feature in split : ",best)
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_pdf("video.pdf")




print("\nconfusion matrix for train data\n",confusion_matrix(ytrain,ypred_train))
print("\nconfusion matrix for test data\n",confusion_matrix(ytest,ypred_test))

print("\nScore for classifier : ",clf.score(xtest,ypred_test))

# print("\nGini index : ",clf.tree_.impurity)
import matplotlib.pyplot as plt


labels = total.keys()
sizes = list(total.values())


fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
















