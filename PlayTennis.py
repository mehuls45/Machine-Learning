# Outlook:
# 	Sunny : 0
# 	Overcast: 1
# 	Rainy : 2
# Temperature : 
# 	Hot : 0
# 	Mild : 1
# 	Cool : 2
# Humidity : 
# 	Normal : 0
# 	High : 1
# Wind : 
# 	Weak : 0
# 	Strong : 1

# Play Tennis : 
# 	No : 0
# 	Yes : 1

# Labels : [Outlook, Temperature, Humidity, Wind]
# Features: [Play Tennis]

from sklearn import tree
X = [[0,0,1,0],[0,0,1,1],[1,0,1,0],[2,1,1,0],[2,2,0,0],[2,2,0,1],[1,2,0,1],[0,1,1,0],[0,2,0,0],[2,1,0,0],[0,1,0,1],[1,1,1,1],[1,0,0,0]]
Y = [0,0,1,1,1,0,1,0,1,1,1,1,1]
clf = tree.DecisionTreeClassifier()
clf.fit(X,Y)
print(clf.predict([[2,1,1,1]]))