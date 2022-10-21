from mathoperations import add,substraction

if __name__=='__main__':
    user=input("which math operation do you want to achieve? Choose 1 for addition and 2 for substraction?")
    a = int(input("A:"))
    b = int(input("B:"))
    if user == "1":
        print(f"your total is {add(a,b)}")
    if user == "2":
        print(f"your total is {substraction(a,b)}")  