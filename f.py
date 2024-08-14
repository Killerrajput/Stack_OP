def Empty(s):
    if s ==[]:
        return True
    else:
        return False
def push(s,item):
    s.append(item)
    t = len(s)-1
def pop(s):
    if isEmpty(s):
        return "UnderFlow"
    else:
        item = s.pop()
        if len(s) == 0:
            t= None
        else:
            t = len(s) - 1
        return item
def Peek(s):
    if isEmpty(s):
        return "Underflow"
    else:
        t = len(s)-1
        return s[t]
def Display(s):
    if isEmpty(s):
        print("Stack Empty: ")
    else:
        t = len(s)-1
        print(s[t],"<-t")
        for a in range(top-1,-1,-1):
            print(s[a])

s = []
t = None
while True:
    print(" Stack Operations.")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display Stack")
    print("5. Exit ")
    ch = int(input("Enter your choice(1-5): "))
    if ch== 1:
        item = int(input("Enter item: "))
        push(s,item)
    elif ch ==2:
        item = pop(s)
        if item == "Underfolw":
            print("Underfolw! Stack is empty!")
        else :
            print("Popped item is", item)            
    elif ch == 3:
        item = Peek(s)
        if item =="Underflow":
            print("Underflow! Stack is empty!")
        else:
            print("Topmost item is", item)
    elif ch==4:
        Display(s)
    elif ch==5:
        break
    else:
        print("Invaild Choise!")
        
                
