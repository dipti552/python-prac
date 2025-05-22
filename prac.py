#python calculator
operator=input("enter a operator(+ - * /)")
num1=int(input("enter first number "))
num2=int(input("enter second number "))
if operator == '+' :
  print("the calculation is: ",num1+num2)
elif operator == '-' :
  print("the calculation is: ",num1-num2)
elif operator == '*' :
  print("the calculation is: ",num1*num2)    
elif operator == '/' :
  print("the calculation is: ",num1/num2)
else:
  print("it is not a valid operator")