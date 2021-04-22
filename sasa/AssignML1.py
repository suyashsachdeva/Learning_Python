#impoting
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd  

#file
local = r"C:\Users\suyash\Desktop\50_Startups.csv"
dataset=pd.read_csv(local)

#file to desired formate
x=dataset.iloc[:,:-1].values #input
Y=dataset.iloc[:,-1].values  #output  -1 refers to the last element
a=[]

#file optimization
for i in x[:,-1]:
    if i=="Florida":
        a.append(-0.5)
    elif i=="California":
        a.append(0)
    elif i=="New York":
        a.append(0.5)

ar = np.array(a)
arr = ar.reshape(50,1)                
xx = np.array(x)
xd = np.delete(xx , (3), axis= 1)
Array = np.concatenate((xd,arr), axis= 1)
print(Array)
YAR = np.array(Y)
y = YAR.reshape(50,1)

arr1, arr2 , arr3, arr4 = np.hsplit(Array, 4)
print(arr1)
print(arr3)


arri = (arr1 - np.mean(arr1))/(np.max(arr1)*2)
arrii = (arr2 - np.mean(arr2)/(np.max(arr2)*2)
#arriii = (arr3 - np.mean(arr3)/(np.max(arr3)*2)
array = np.concatenate((arri,arrii,arriii,arr), axis= 1)
#print(array)






"""
if i in range(3):
    f = np.max(array[:,i])
    m = np.mean(array[:,i])
    if j in range(50):
        array[j, i] = (array[j, i] - m)/f

print(array)



from sklearn.model_selection import train_test_split
array_train, array_test, y_train, y_test = train_test_split(array ,y, test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression 
regressor = LinearRegression()
regressor.fit(array_train, y_train)

y_pred = regressor.predict(array_test)




plt.scatter(array_train, y_train, color='red')
plt.plot(array_train, regressor.predict(array_train),color='blue')
plt.title("salary vs years of expreesion")
plt.xlabel("years of experience")
plt.ylabel("salary")
plt.show()
"""