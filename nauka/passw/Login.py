#Login example
import time
import pickle
import os

target = 'hasla.txt'

MyUsers = {'admin':'admin'}

if os.path.getsize(target) > 0:
    with open(target, 'rb') as f:
        MyUsers = pickle.load(f)
        print(type(MyUsers))

def login(name,passw):
    if name in MyUsers.keys():
        if MyUsers[name] == passw:
            print("SUCCESS@")
            time.sleep(4)
        else:
            print("FALSE")
            time.sleep(3)
            return loginOrReg()
    else:
        print("NAME not appear as our USER")
        return loginOrReg()

def register():
    regname = str(input("Your name:"))
    if regname in MyUsers.keys():
        print("This name is already in use. Change name please...")
        time.sleep(3)
        return register()
    regpassw = str(input("Your passw"))
    MyUsers[regname] = regpassw
    with open(target, 'wb') as f:
        pickle.dump(MyUsers, f, pickle.HIGHEST_PROTOCOL)
        return loginOrReg()


def loginOrReg(): 
    #lor = LoginOrReg option
    lor= int(input("Type 1 for Login, or type 2 for register:"))
    if lor == 1:
        name = str(input("Name:"))
        passw = str(input("Password:"))
        return login(name,passw)
    elif lor == 2:
        return register()
    elif lor == 7:
        print("Znajdujesz się w mega tajnym miejscu. Dane chronione!")
        time.sleep(3)
        print(MyUsers)
        time.sleep(5)
        return loginOrReg()


loginOrReg()
