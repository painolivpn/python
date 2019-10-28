import list;
# function without parameter

def printt():
  print("hi")

print("hh")
printt();

# function with parameter

def para(a,b):
   c=a+b  
   return c

a= int(input("enter a no: "))
b= int(input("enter another no: "))

print("sum is",para(a,b))
