import math
import pandas
import numpy as np

#the dimensions of the item as input
x = float(input())
y = float(input())

#reading the data from the csv file
data = pandas.read_csv("F:\Contest\Infra Mind\Excel and CSV\DatasetFinal.csv")

#store the dataset items in separate arrays for each column
iden = data["ID"].values
item = data["Item"].values
height = data["Height"].values
width = data["Width"].values

#the array data are now stored in separate lists
pid = np.array(iden).tolist()
pitem = np.array(item).tolist()
h = np.array(height).tolist()
w = np.array(width).tolist()

# n is the number of items present in the dataset
n = len(pitem)

#declare a list to store the error range
RangeErr = []

#calculate the error range for each item with the given input and store in the list
for i in range(0,n):
    temp = ((h[i] - x)**2) + ((w[i] - y)**2)
    temp1 = math.sqrt(temp)
    RangeErr.append(temp1)

#postion of the output
position = RangeErr.index(min(RangeErr))

#print the outputs
print("The item is ",end="")
print(pitem[position])
print("The product ID is ",end="")
print(pid[position])
