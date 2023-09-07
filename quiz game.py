import ctypes
print("Welcome to my quiz game")
x=0
playing = input("Do you want to play? ")
if playing.upper() != "YES":
    quit()
print("Okay let's play")
answer=input("what is the capital of ALGERIA? ")
if answer.lower()!= "alger":
    print("wrong")
if answer.lower() == "alger":
    print("right")
    x=x+1
answer=input("what is my name? ")
if answer.lower()!= "akram":
    print("wrong")
if answer.lower() == "akram":
    print("right")
    x=x+1
print(x) 
   

