#INTRO AND DECLARING OPENING VAR

name = input("Enter your character name: ")

print("Welcome to the Dungeon " + name + ".")

print("You enter a large cave with dwindling light.")

print("How long can you survive and what skills can you gain!")

#CHOICE AND ENCOUNTER FRIENDLY OR FOW

def first_encounter():

    ork = 2
    health = 5
    block = 2

    print("Two mine shafts lie before you both similar in looks but a horrible smell is coming from the LEFT shaft! The RIGHT one is well lit up and seems normal.")

    shaft_one = input("CHOOSE: ")

    if shaft_one == "LEFT":
        print("An sleeping ork is blocking a doorway you need to open to proceed!")
        door = input("OPEN or TURN AWAY: ")
        if door == "OPEN":
            print("The ORK jumps to his feet and grabs his battleaxe!")
            while ork > 0:
                    turn = input("ATTACK or BLOCK/OFFENCE?")
                    if turn == "ATTACK":
                        ork = ork - 1
                        health = health - 1
                    elif turn == "BLOCK/OFFENCE":
                        block = block - 1
                        ork = ork - 1
            if health == 0:
                print("You have been defeated!")
                print("GAME OVER!!")
            if ork == 0:
                print("Hes lies defeated his torso carved in two!")
                print("You Win!!!")    
        elif door == "TURN AWAY":
            print("The ORK shashes his axe into your skull!")
            print("GAME OVER!!!!")
    if shaft_one == "RIGHT":
        print("A large dark figure aproaches in a dark robes.")
        print("In his hand a stange glow ammits from his fist!.")
             
first_encounter()