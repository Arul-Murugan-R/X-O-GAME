print("This is game of X and O")
print("this is a two player game Player1 :X Player2 :O")
square1=[1,2,3,4,5,6,7,8,9]
emp=[]
def board():
    for i in range(0,9):
        print(square1[i],end="")
        print("|",end="")  
        if (i+1)%3==0 and i+1!=9:
            print("") 
            print("_ _ _") 
board()
def player1():
    i=int(input("\nEnter the postion to place X : "))
    if i not in emp:
        emp.append(i)
        i=i-1
        square1[i]="X"
    else:
        print("\nUse some other position since it is used by other player")
        player1()
def player2():
    i=int(input("\nEnter the postion to place O : "))
    if i not in emp:
        emp.append(i)
        i=i-1
        square1[i]="O"
    else:
        print("\nUse some other position since it is used by other player")
        player2()
def check():
    n=0
    for i in range(0,9):
        if i+1==1 or i+1==4 or i+1==7:
            j=i+1
            k=i+2
            if (square1[i]==square1[k]) and (square1[i]==square1[j]):
                if square1[i]=="X":
                    print("\nPlayer1 is the winner")
                else:
                    print("\nPlayer2 is the winner ")
                n=1
        if i+1==1 or i+1==2 or i+1==3:
            j=i+3
            k=i+6
            if (square1[i]==square1[k]) and (square1[i]==square1[j]):
                if square1[i]=="X":
                    print("\nPlayer1 is the winner")
                else:
                    print("\nplayer2 is the winner ")
                n=1    
        if i+1==1:
            j=i+4
            k=i+8
            if (square1[i]==square1[k]) and (square1[i]==square1[j]):
                if square1[i]=="X":
                    print("\nPlayer1 is the winner")
                else:
                    print("\nplayer2 is the winner ")
                n=1
        if i+1==3:
            j=i+2
            k=i+4
            if (square1[i]==square1[k]) and (square1[i]==square1[j]):
                if square1[i]=="X":
                    print("\nPlayer1 is the winner")
                else:
                    print("\nplayer2 is the winner ")
                n=1
    return n 
      
for i in range(1,10):
    if i%2!=0:
        player1()
    else:
        player2()
    board()
    n=0
    if i>4:
        n=check()
    if n==1:
        break
if n!=1:
    print("\nThe Game is Draw ")

    
        
