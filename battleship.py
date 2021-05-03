'''
Ships:
Carrier (6)
Battleship (5)
Destroyer (4)
Submarine (3)
Smol boat (2)
'''

#apaplemaofuyjmccvb

class Player:
    def __init__(self, name, ships_won, ships_lost, no_of_hits):
        self.name = name
        self.ships_won = ships_won
        self.ships_lost = ships_lost
        self.no_of_hits = no_of_hits


class Ship:
    def __init__(self, ship_name, length, no_hit, x_1, y_1, x_2, y_2, list_of_coor):
        self.ship_name = ship_name
        self.length = length
        self.no_hit = no_hit
        self.x_1 = x_1
        self.y_1 = x_1
        self.x_2 = x_2
        self.y_2 = x_2
        self.list_of_coor = list(list_of_coor)

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

    p1_carrier = Ship('carrier', 6, 0, p1_carrier_start[0], p1_carrier_start[1], p1_carrier_end[0], p1_carrier_end[1], [])
    p1_battleship = Ship('battleship', 5, 0, p1_battleship_start[0], p1_battleship_start[1], p1_battleship_end[0], p1_battleship_end[1], [])
    p1_destroyer = Ship('destroyer', 4, 0, p1_destroyer_start[0], p1_destroyer_start[1], p1_destroyer_end[0], p1_destroyer_end[1], [])
    p1_submarine = Ship('submarine', 3, 0, p1_submarine_start[0], p1_submarine_start[1], p1_submarine_end[0], p1_submarine_end[1], [])
    p1_smol = Ship('smol', 2, 0, p1_smol_start[0], p1_smol_start[1], p1_smol_end[0], p1_smol_end[1], [])
    global p1_ships
    p1_ships = [p1_carrier, p1_battleship, p1_destroyer, p1_submarine, p1_smol]
    

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

    p2_carrier = Ship('carrier', 6, 0, p2_carrier_start[0], p2_carrier_start[1], p2_carrier_end[0], p2_carrier_end[1], [])
    p2_battleship = Ship('battleship', 5, 0, p2_battleship_start[0], p2_battleship_start[1], p2_battleship_end[0], p2_battleship_end[1], [])
    p2_destroyer = Ship('destroyer', 4, 0, p2_destroyer_start[0], p2_destroyer_start[1], p2_destroyer_end[0], p2_destroyer_end[1], [])
    p2_submarine = Ship('submarine', 3, 0, p2_submarine_start[0], p2_submarine_start[1], p2_submarine_end[0], p2_submarine_end[1], [])
    p2_smol = Ship('smol', 2, 0, p2_smol_start[0], p2_smol_start[1], p2_smol_end[0], p2_smol_end[1], [])
    global p2_ships
    p2_ships = [p2_carrier, p2_battleship, p2_destroyer, p2_submarine, p2_smol]

def setup_coordinates_p1(): #attempt. This part i need to figure out how to use ship_type to call the class... y'know... cuz i dont
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
                ship_type.list_of_coor.append(coor)

        if ship_direction == "vertical":
            while ship_type.x_1 != ship_type.x_2:
                ship_type.x_1 += 1
                coor = str(ship_type.x_1 + ',' + ship_type.y_1)
                ship_type.list_of_coor.append(coor)
    
def setup_coordinates_p2(): #attempt
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
                ship_type.list_of_coor.append(coor)

        elif ship_direction == "vertical":
            while ship_type.x_1 != ship_type.x_2:
                ship_type.x_1 += 1
                coor = str(ship_type.x_1 + ',' + ship_type.y_1)
                ship_type.list_of_coor.append(coor)

def p1_checking_phase(): #try using pop if remove does not work and also try using a dictionary to tell the status of ships (sunk/float)
    if len(p1_carrier.list_of_coor) == 0:
        print("Carrier sunk ")
        p1_ships.remove(p1_carrier)
    elif len(p1_battleship.list_of_coor) == 0:
        print("Battleship sunk ")
        p1_ships.remove(p1_battleship)
    elif len(p1_destroyer.list_of_coor) == 0:
        print("Destroyer sunk ")
        p1_ships.remove(p1_destroyer)
    elif len(p1_submarine.list_of_coor) == 0:
        print("Submarine sunk ")
        p1_ships.remove(p1_submarine)
    elif len(p1_smol.list_of_coor) == 0:
        print("Smol sunk ")
        p1_ships.remove(p1_smol)
    
def p2_checking_phase():
    if len(p2_carrier.list_of_coor) == 0:
        print("Carrier sunk ")
        p2_ships.remove(p2_carrier)
    elif len(p2_battleship.list_of_coor) == 0:
        print("Battleship sunk ")
        p2_ships.remove(p2_battleship)
    elif len(p2_destroyer.list_of_coor) == 0:
        print("Destroyer sunk ")
        p2_ships.remove(p2_destroyer)
    elif len(p2_submarine.list_of_coor) == 0:
        print("Submarine sunk ")
        p2_ships.remove(p2_submarine)
    elif len(p2_smol.list_of_coor) == 0:
        print("Smol sunk ")
        p2_ships.remove(p2_smol)

def attack(p, pos_x, pos_y):
    attack_pos = input("Attack! (x,y) ")
    if p == "1":
        #checking if the coordinates are in p2's battleship list
        if attack_pos in p2_carrier.list_of_coor:
            print("Hit! ")
            p2_carrier.list_of_coor.remove(attack_pos)
            
        elif attack_pos in p2_battleship.list_of_coor:
            print("Hit! ")
            p2_battleship.list_of_coor.remove(attack_pos)

        elif attack_pos in p2_destroyer.list_of_coor:
            print("Hit! ")
            p2_destroyer.list_of_coor.remove(attack_pos)
        
        elif attack_pos in p2_submarine.list_of_coor:
            print("Hit! ")
            p2_submarine.list_of_coor.remove(attack_pos)
        
        elif attack_pos in p2_smol.list_of_coor:
            print("Hit! ")
            p2_smol.list_of_coor.remove(attack_pos)

        else:
            print("Miss ")
    
    
    if p == "2":
        #checking if the coordinates are in p2's battleship list
        if attack_pos in p1_carrier.list_of_coor:
            print("Hit! ")
            p1_carrier.list_of_coor.remove(attack_pos)
            
        elif attack_pos in p1_battleship.list_of_coor:
            print("Hit! ")
            p1_battleship.list_of_coor.remove(attack_pos)

        elif attack_pos in p1_destroyer.list_of_coor:
            print("Hit! ")
            p1_destroyer.list_of_coor.remove(attack_pos)
        
        elif attack_pos in p1_submarine.list_of_coor:
            print("Hit! ")
            p1_submarine.list_of_coor.remove(attack_pos)
        
        elif attack_pos in p1_smol.list_of_coor:
            print("Hit! ")
            p1_smol.list_of_coor.remove(attack_pos)

        else:
            print("Miss ")    


def main():  
    global p1
    global p2
    print("This code runs a game of battleship. When putting in inputs ensure that the x and y positions of the ships are not above 8, as the field of the battleships game is 8X8")
    setup()
    set_up_player_1()
    set_up_player_2()
    setup_coordinates_p1()
    setup_coordinates_p2()
    attack("1", None, None)
    p2_checking_phase()
    attack("2", None, None)
    p1_checking_phase()



main()