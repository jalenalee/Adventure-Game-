'''
-------------------------------------------------------------------------------
Name:		adventure-game.py
Purpose:
This is a program is a game that takes place in a school. Your goal is to get to
the lunch room.

Author:		lee.J

Created:    19/06/2017
------------------------------------------------------------------------------
'''
#importing files 
import FoodFight
import Minesweeper
import Hangman
import random
import re
import time
from string import ascii_lowercase

#Variables
done = 'x'

#creating lists for rooms                  
room_list = []

room = ["You are in phySucks. There is a passage to the north.",1, None, None, None]
room_list.append(room)

room = ["You are in LiF3. There is a passage to the north, east, and south.",2, 4,0, None]
room_list.append(room)

room = ["You are in M3th. There is a passage to the east and south.", None,3,1,None]
room_list.append(room)

room = ["You are in SiGhence. There is a passage to the east, south, and west.", None,5,4,2]
room_list.append(room)

room = ["You are in bYeology. There is a passage to the north and east, and west.", 3,6,None,1]
room_list.append(room)

room = ["You are in Endlish. There is a passage to the south and west.",None, None,6,3]
room_list.append(room)

room = ["You are in cRiemistry. There is a passage to the west, north, and east.",5,7, None,4]
room_list.append(room)

room = ["You are in Lunch. There is a passage to the west.", None, None, None,6]
room_list.append(room)

current_room = 0






while done != 'quit':
    #if statements to assign rooms to games 
    if current_room == 5:
        Hangman.main()
    elif current_room == 7:
        done=FoodFight.food_fight(done)
    elif current_room == 3:
        Minesweeper.playgame()
 



    #if statements to ask where the user wants to go 
    if done != 'quit':
    
        print (room_list[current_room][0])
        direction = input("What direction would you like to go? ")
        print ('\n')

        if direction == 'n':
            next_room = room_list[current_room][1]
            if next_room == None:
                    print ("You can't go that way.")
            else:
                current_room = next_room
        elif direction == 'e':
            next_room = room_list[current_room][2]
            if next_room == None:
                    print ("You can't go that way.")
            else:
                current_room = next_room
        elif direction == 's':
            next_room = room_list[current_room][3]
            if next_room == None:
                    print ("You can't go that way.")
            else:
                current_room = next_room
        elif direction == 'w':
            next_room = room_list[current_room][4]
            if next_room == None:
                    print ("You can't go that way.")
            else:
                current_room = next_room
        else:
            print ("I don't understand what you are saying. Please re-type your instructions. ")







