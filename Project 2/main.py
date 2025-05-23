import random
n = random.randint(1, 100)
a= -1
guesses = 0
while(a!=n):
    print
    
    a  = int(input("Guess a number: "))
    if(a>n):

        print("lower number please")
        guesses +=1
    elif(a<n):
        print("Higher number please")
        guesses +=1

print(f"you have guessed the  number {n} corectly in {guesses} attempts ")