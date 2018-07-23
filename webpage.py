a1 = ("Nothing...")
b2 = ("Hello")
c3 = ("Hello, I'm in need")
d4 = ("...")
e5 = ("Some days I feel empty") #yellow
f6 = ("I am having suicidal thoughts/tendencies") #red
g7 = ("")
h8 = ("")
choices = (a1, b2, c3, d4, e5,f6, g7, h8)

e6 = ("my family")
e7 = ("my Job")
e8 = ("school")
choices2 = (e6, e7, e8)

e1 = ("good")
e2 = ("bad")
choices2_2 = (e1, e2)

e3 = ("Stressfully")
e4 = ("Overworked")
e9 = ("Meaningless")
choices2_0 = (e3, e4, e9)

e10 = ("Workload")
e11 = ("Classes too hard")
e12 = ("Classes too easy")
choices2_1 = (e10, e11, e12)

f1 = ("")
f2 = ("")
f3 = ("")
choice3 = (f1, f2, f3)

str(choices, choices2, chocies2_2, choices2_0, choices2_1)
print("Welcome to our online help line, please wait to be directed to a counselor")

#code corraspondes with the inputs e to h
#connects
print("Hello and good day what seems to be the matter?")
    input(choices = a1, b2, c3, d4)
    if input(choices = a1):
        print("Are you sure then why are you here?")
    elif input(choices = b2):
        print("Hello how are you?")
    elif input(choices = c3):
        print("Thats what im here for. How may i be of assistence?")
    elif input(choices = d4):
        print("I understand you may be nervous take your time")
print(choices = e5, f6, g7, h8),
input(choices = e5, f6, g7, h8):
    if(input(choices = e5)):    #yellow
        print(e5)
        print("Are there any factors in your life that makes you feel this way?")
        print(choices2)
            input(choices2 = e6, e7, e8)
                if(input(choices2 = e6)):
                    print("How is your relation with your family?")
                    print(choices2_2)
                    input(choices2_2 = e1, e2):
                        print(input())
                if(input(choices2 = e7)):
                    print("What about your job is the issue?")
                    print(choices2_0)
                    input(choices2_0 = e3, e4, e9):
                        print(input())
                if(input(choices2 = e8)):
                    print("Are the classes challenging or is the workload too much?")
                    print(choices2_1)
                    input(choices2_1 = e10, e11, e12)
                    print(input())
    elif(input(chocies = f6)):       #red
        print(f6)
        print("Any major points in your life that could have lead up to this?")
        print(choice3)
