import sys
import os


class Player:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.attack = 10

class Tool:
    def __init__(self, name):
        self.name = name



def main():
    os.system('clear')
    print"Welcome to my game!\n"
    print "1.) Start"
    print "2.) Load"
    print "3.) Exit"
    option = raw_input("->")
    if option == "1":
        start()
    elif option == "2":
        pass
    elif option == "3":
        sys.exit()
    else:
        main()


def start():
    os.system('clear')
    print "Hello, what is your name?"
    option = raw_input("->")
    global PlayerIG  # means you can use this outside of local functions
    PlayerIG = Player(option)
    start1()


def start1():
    os.system('clear')

    print("Where would you like to go, "+ PlayerIG.name+"?\n")
    print('To the mountain')
    print('To the ocean')
    print("To the mine")
    option = raw_input(">>")
    if option == ("mountain"):
        startm()
    elif option == ("ocean"):
        starto()
    elif option == ("mine"):
        startmi()
    else:
        start1()
def startm():
    os.system('clear')
    print("Here at the base of the mountain, we are preparing")
    print("to ascend to the peak. Before we depart, plese select your gear")
    print("select 3 of the following to go into your pack:")
    print("sleeping bag, flare gun, dried fruit, ")
    optionm1 = raw_input('>>')
    global ToolIG
    ToolIG = Tool(optionm1)
    optionm2 = raw_input('>>')
    global ToolIG2
    ToolIG2 = Tool(optionm2)
    optionm3 = raw_input('>>')
    global ToolIG3
    ToolIG3 = Tool(optionm3)
    print('are you ready to climb the mountain '+ PlayerIG.name + '?')
    preoption = raw_input(">>")
    if preoption == "no":
        main()
    else:
        startprem()
def startprem():
    os.system('clear')
    print('We are ascending the mountain as...')

    if ToolIG.name or ToolIG2.name or ToolIG3.name == "dried fruit":
        startm2a()
    #elif option2 == "dried fruit":
     #   startm2a()
    #elif option3 == "dried fruit":
        #startm2a()
    else:
        print('looks like we have a problem... lets go back')
        optpre = raw_input("press return dummy")
        startm()
def startm2a():
    print("a bear attacks!!")
    print("quick! what would you like to do?!\n")
    print("1.) use " + ToolIG.name)
    print("2.) use " + ToolIG2.name)
    print("3.) use " + ToolIG3.name)
    use = raw_input("use: ")
    if use == "dried fruit":
        startm3b()
    else:
        startm2a()

def startm3b():
    print("looks like that all the bear wanted... Let\'s keep going up the mountain")





main()