# Python program to illustrate 
# Append vs write mode 
file1 = open("dimen.txt","w") 
L = ["This is Delhi \n","This is Paris \n","This is London \n"] 
file1.writelines(L)
file1.close()

# Append-adds at last 
file1 = open("dimen.txt","r")#append mode 
print(file1.read()) 
file1.close() 
