print("This is game of X and O")
print("this is a two player game Player1 :X Player2 :O")
square1=[1,2,3,4,5,6,7,8,9]
emp=[]
def board():
    for i in range(0,9):
        print(square1[i],end="")
        print("|",end="")  
        if (i+1)%3==0 :
            print("") 
            print("______") 
board()
def player1():
    i=int(input("Enter the postion to place X : "))
    if i not in emp:
        emp.append(i)
        i=i-1
        square1[i]="X"
    else:
        print("Use some other position since it is used by other player")
        player1()
def player2():
    i=int(input("Enter the postion to place O : "))
    if i not in emp:
        emp.append(i)
        i=i-1
        square1[i]="O"
    else:
        print("Use some other position since it is used by other player")
        player2()

for i in range(1,10):
    if i%2!=0:
        player1()
    else:
        player2()
    board()
    

    
        