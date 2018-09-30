# Age:
# 	<=30 : 0
# 	31..40 : 1
# 	>40 : 2
# Income : 
# 	Low : 0
# 	Medium : 1
# 	High : 2
# Student:
# 	No : 0
# 	Yes : 1
# Credit : 
# 	Fair : 0
# 	Excellent : 1
# Buys_Comp : 
# 	No : 0
# 	Yes : 1

from sklearn import tree
clf = tree.DecisionTreeClassifier()
X = [[0,2,0,0],[0,2,0,1],[1,2,0,0],[2,1,0,0],[2,0,1,0],[2,0,1,1],[1,0,1,1],[0,1,0,0],[0,0,1,0],[2,1,1,1],[0,1,1,1],[1,1,0,1],[1,2,1,1],[2,1,0,1]]
Y = [0,0,1,1,1,0,1,0,1,1,1,1,1,0]
clf.fit(X,Y)
print(clf.predict([[0,1,1,0]]))
