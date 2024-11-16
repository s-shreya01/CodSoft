# CALCULATOR PROGRAM IN PYTHON

print("choose operation:")
print("1.Subtraction")
print("2.Addition")
print("3.Divison")
print("4.Multiplication")


num1=int(input("enter 1st number:"))
num2=int(input("enter 2nd number:"))


while True:
 choice=(int(input("enter your choice:")))
 if choice == 1:
    print("output:",num1-num2)
 elif choice == 2:
    print("output:",num1+num2)
 elif choice == 3:
    print("output:",num1%num2)
 elif choice == 4:
    print("output:",num1*num2)
 else:
    print("invalid input")