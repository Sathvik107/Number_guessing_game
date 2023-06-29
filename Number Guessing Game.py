from random import randint
class guess_number:
    def generate(self)
    def inputting(self):
        n=int(input("\nIn how many turns you will be able to guess the number between 1 to 100\n"))
        score=20
        a=randint(1,100)
        print("START")
        for i in range(0,n):
            s=int(input("ENTER YOUR GUESS\n"))
            if(s==a):
                print("******CORRECT GUESS******")
                score=score+1
                print("score=",score)
                print("total score ={}/20".format(score))
                break
            elif(s>a):
                print("*******INCORRECT GUESS*******")
                print("Your guess is greater than number")
                score=score-1
                print("score=",score)
                print("total score ={}/20".format(score))
                if(a%s==0 and s!=a):
                    print("clue: your guess is divisible by the number")
                if(s%2!=0 and a%2==0):
                    print("clue: It is a even number")
                if(a>50):
                    print("clue: Number is greater than 50")
                if(a<50):
                    print("clue: Number is less than 50")
            elif(s<a):
                print("*******INCORRECT GUESS********")
                print("Your guess is less than number")
                score=score-1
                print("score=",score)
                print("total score ={}/20".format(score))
                if(a%2==0):
                    print("clue: It is a even number")
                else:
                    print("clue: It is an odd number")
                if(a>50 and s<50):
                    print("clue: Number is greater than 50")
                if(a<50 and s>50):
                    print("clue: Number is less than 50")
            else:
                print("******INCORRECT GUESS*******")
           
        return 

g_N=guess_number()
print("READY TO PLAY\n")
print("INSTRUCTIONS:\n1)IT IS SINGLE PLAYER GAME\n2)GUESS THE NUMBER BETWEEN 1 TO 100, WHICH IS CHOSEN BY THE PC IN RANDOM\n3)INITIAL SCORE:20")
print("4)FOR EVERY WRONG GUESS ONE POINT WILL BE DEDUCTED FROM THE INITIAL SCORE")
g_N.inputting()
print("*******Game Over*******")
print("WELL PLAYED")
print("THANKS FOR PLAYING")


