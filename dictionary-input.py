#### For Dictionary input
n=int(input("Enter the number of key-value pairs in the dict: "))
my_dict = {}
val=[]
for i in range (n):    
    key=input("Enter key :")
    z = int(input("Enter the number of values for key: "))
    for j in range(z):
        value=input("Enter values for this key:")
        val.append(value)
    my_dict.update({key: val})
print(my_dict) 
