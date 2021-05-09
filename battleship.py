'''
Ships:
Carrier (6)
Battleship (5)
Destroyer (4)
Submarine (3)
Smol boat (2)
'''

import os

class Player:
    def __init__(self, name, ships_won, ships_lost, no_of_hits):
        self.name = name
        self.ships_won = ships_won
        self.ships_lost = ships_lost
        self.no_of_hits = no_of_hits


class Ship:
    def __init__(self, ship_name, length, no_hit, x_1, y_1, x_2, y_2, dict_of_coor):
        self.ship_name = ship_name
        self.length = length
        self.no_hit = no_hit
        self.x_1 = x_1
        self.y_1 = x_1
        self.x_2 = x_2
        self.y_2 = x_2
        self.dict_of_coor = dict(dict_of_coor)

def setup():

    p1_name = input("Enter name ")
    p2_name = input("Enter name ")

    p1 = Player(p1_name, 0, 0, 0)
    p2 = Player(p2_name, 0, 0, 0)

def set_up_player_1():
    p1_carrier_start = input("Start point of carrier (x,y) ")
    p1_carrier_end = input("End point of carrier (x,y) ").split(',')
    p1_battleship_start = input("Start point of battleship (x,y) ").split(',')
    p1_battleship_end = input("End point of battleship (x,y) ").split(',')
    p1_destroyer_start = input("Start point of destroyer (x,y) ").split(',')
    p1_destroyer_end = input("End point of destroyer (x,y) ").split(',')
    p1_submarine_start = input("Start point of submarine (x,y) ").split(',')
    p1_submarine_end = input("End point of submarine (x,y) ").split(',')
    p1_smol_start = input("Start point of smol (x,y) ").split(',')     
    p1_smol_end = input("End point of smol (x,y) ").split(',')

    p1_carrier = Ship('carrier', 6, 0, p1_carrier_start[0], p1_carrier_start[1], p1_carrier_end[0], p1_carrier_end[1], {})
    p1_battleship = Ship('battleship', 5, 0, p1_battleship_start[0], p1_battleship_start[1], p1_battleship_end[0], p1_battleship_end[1], {})
    p1_destroyer = Ship('destroyer', 4, 0, p1_destroyer_start[0], p1_destroyer_start[1], p1_destroyer_end[0], p1_destroyer_end[1], {})
    p1_submarine = Ship('submarine', 3, 0, p1_submarine_start[0], p1_submarine_start[1], p1_submarine_end[0], p1_submarine_end[1], {})
    p1_smol = Ship('smol', 2, 0, p1_smol_start[0], p1_smol_start[1], p1_smol_end[0], p1_smol_end[1], {})
    global p1_ships
    #True means alive, False means sunk.
    p1_ships = {p1_carrier:True, p1_battleship:True, p1_destroyer:True, p1_submarine:True, p1_smol:True}
    

def set_up_player_2():
    #Player 2 ship placement
    p2_carrier_start = input("Start point of carrier (x,y) ").split(',')
    p2_carrier_end = input("End point of carrier (x,y) ").split(',')
    p2_battleship_start = input("Start point of battleship (x,y) ").split(',')
    p2_battleship_end = input("End point of battleship (x,y) ").split(',')
    p2_destroyer_start = input("Start point of destroyer (x,y) ").split(',')
    p2_destroyer_end = input("End point of destroyer (x,y) ").split(',')
    p2_submarine_start = input("Start point of submarine (x,y) ").split(',')
    p2_submarine_end = input("End point of submarine (x,y) ").split(',')
    p2_smol_start = input("Start point of smol (x,y) ").split(',')
    p2_smol_end = input("End point of smol (x,y) ").split(',')

    p2_carrier = Ship('carrier', 6, 0, p2_carrier_start[0], p2_carrier_start[1], p2_carrier_end[0], p2_carrier_end[1], {})
    p2_battleship = Ship('battleship', 5, 0, p2_battleship_start[0], p2_battleship_start[1], p2_battleship_end[0], p2_battleship_end[1], {})
    p2_destroyer = Ship('destroyer', 4, 0, p2_destroyer_start[0], p2_destroyer_start[1], p2_destroyer_end[0], p2_destroyer_end[1], {})
    p2_submarine = Ship('submarine', 3, 0, p2_submarine_start[0], p2_submarine_start[1], p2_submarine_end[0], p2_submarine_end[1], {})
    p2_smol = Ship('smol', 2, 0, p2_smol_start[0], p2_smol_start[1], p2_smol_end[0], p2_smol_end[1], {})
    global p2_ships
    #True means alive, False means sunk.
    p2_ships = {p2_carrier:True, p2_battleship:True, p2_destroyer:True, p2_submarine:True, p2_smol:True}

def setup_coordinates_p1():
    global p1_ships #attempt. This part i need to figure out how to use ship_type to call the class... y'know... cuz i dont
    for i in range(5):
        ship_type = p1_ships[i]
        if ship_type.x_1 == ship_type.x_2:
            ship_direction = "vertical"
        elif ship_type.y_1 == ship_type.y_1:
            ship_direction = "horizontal"
        
        if ship_direction == "horizontal":
            while ship_type.y_1 != ship_type.y_2:
                y_1 += 1
                coor = str(ship_type.x_1 + ',' + ship_type.y_1)
                ship_type.dict_of_coor[coor] = True #if this does not work try the update dictionary method

        if ship_direction == "vertical":
            while ship_type.x_1 != ship_type.x_2:
                ship_type.x_1 += 1
                coor = str(ship_type.x_1 + ',' + ship_type.y_1)
                print(coor) #debuggin
                ship_type.dict_of_coor[coor] = True

    
def setup_coordinates_p2(): #attempt
    global p2_ships
    for o in range(5):
        ship_type = p2_ships[o]
        if ship_type.x_1 == ship_type.x_2:
            ship_direction = "vertical"
        elif ship_type.y_1 == ship_type.y_1:
            ship_direction = "horizontal"
        
        if ship_direction == "horizontal":
            while ship_type.y_1 != ship_type.y_2:
                ship_type.y_1 += 1
                coor = str(ship_type.x_1 + ',' + ship_type.y_1)
                ship_type.dict_of_coor.append(coor)
                ship_type.dict_of_coor[coor] = True

        elif ship_direction == "vertical":
            while ship_type.x_1 != ship_type.x_2:
                ship_type.x_1 += 1
                coor = str(ship_type.x_1 + ',' + ship_type.y_1)
                ship_type.dict_of_coor[coor] = True

def p1_checking_phase(): #try using pop if remove does not work and also try using a dictionary to tell the status of ships (sunk/float)
    if all(stat == False for stat in p1_carrier.dict_of_coor.values()):
        print("Carrier sunk ")
        p1_ships[p1_carrier] = False
    elif all(stat == False for stat in p1_battleship.dict_of_coor.values()):
        print("Battleship sunk ")
        p1_ships[p1_battleship] = False
    elif all(stat == False for stat in p1_destroyer.dict_of_coor.values()):
        print("Destroyer sunk ")
        p1_ships[p1_destroyer] = False
    elif all(stat == False for stat in p1_submarine.dict_of_coor.values()):
        print("Submarine sunk ")
        p1_ships[p1_submarine] = False
    elif all(stat == False for stat in p1_smol.dict_of_coor.values()):
        print("Smol sunk ")
        p1_ships[p1_smol] = False


def p2_checking_phase(): #try using pop if remove does not work and also try using a dictionary to tell the status of ships (sunk/float)
    if all(stat == False for stat in p2_carrier.dict_of_coor.values()):
        print("Carrier sunk ")
        p2_ships[p2_carrier] = False
    elif all(stat == False for stat in p2_battleship.dict_of_coor.values()):
        print("Battleship sunk ")
        p2_ships[p2_battleship] = False
    elif all(stat == False for stat in p2_destroyer.dict_of_coor.values()):
        print("Destroyer sunk ")
        p2_ships[p2_destroyer] = False
    elif all(stat == False for stat in p2_submarine.dict_of_coor.values()):
        print("Submarine sunk ")
        p2_ships[p2_submarine] = False
    elif all(stat == False for stat in p2_smol.dict_of_coor.values()):
        print("Smol sunk ")
        p2_ships[p2_smol] = False


def attack(p):
    global p2_carrier
    global p2_battleship
    global p2_destroyer
    global p2_submarine
    global p2_smol

    global p1_carrier
    global p1_battleship
    global p1_destroyer
    global p1_submarine
    global p1_smol
    attack_pos = str(input("Attack! (x,y) "))
    

    #WORK ON THIS PART NEXT
    if p == "1":
        #checking if the coordinates are in p2's battleship list while using dictionary
        if attack_pos in p2_carrier.dict_of_coor:
            print("Hit! ")
            p2_carrier.dict_of_coor[attack_pos] = False
            
        elif attack_pos in p2_battleship.dict_of_coor:
            print("Hit! ")
            p2_battleship.dict_of_coor[attack_pos] = False

        elif attack_pos in p2_destroyer.dict_of_coor:
            print("Hit! ")
            p2_destroyer.dict_of_coor[attack_pos] = False
        
        elif attack_pos in p2_submarine.dict_of_coor:
            print("Hit! ")
            p2_submarine.dict_of_coor[attack_pos] = False
        
        elif attack_pos in p2_smol.dict_of_coor:
            print("Hit! ")
            p2_smol.dict_of_coor[attack_pos] = False

        else:
            print("Miss ")
    
    
    if p == "2":
        #checking if the coordinates are in p2's battleship list
        if attack_pos in p1_carrier.dict_of_coor:
            print("Hit! ")
            p1_carrier.dict_of_coor[attack_pos] = False
            
        elif attack_pos in p1_battleship.dict_of_coor:
            print("Hit! ")
            p1_battleship.dict_of_coor[attack_pos] = False

        elif attack_pos in p1_destroyer.dict_of_coor:
            print("Hit! ")
            p1_destroyer.dict_of_coor[attack_pos] = False
        
        elif attack_pos in p1_submarine.dict_of_coor:
            print("Hit! ")
            p1_submarine.dict_of_coor[attack_pos] = False
        
        elif attack_pos in p1_smol.dict_of_coor:
            print("Hit! ")
            p1_smol.dict_of_coor[attack_pos] = False

        else:
            print("Miss ")    

def winner(w):
    if w == 1:
        if all(stats == False for stats in p1_ships.values()):
            print("Player Two Wins!")
            d +=1 
    
    elif w == 2:
        if all(stats == False for stats in p2_ships.values()):
            print("Player One Wins!")
            d += 1

def main():
    global p1
    global p2
    d = 9
    print("This code runs a game of battleship. When putting in inputs ensure that the x and y positions of the ships are not above 8, as the field of the battleships game is 8X8")
    setup()
    set_up_player_1()
    set_up_player_2()
    setup_coordinates_p1()
    os.system("ls")
    setup_coordinates_p2()
    os.system("ls")
    while d == 9:
        attack("1")
        p2_checking_phase()
        winner(2)
        attack("2")
        p1_checking_phase()
        winner(1)



main()