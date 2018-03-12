def food_fight(done):

    print("Welcome to the lunch room, you're just in time for the food fight! Choose the food with the corresponding number in the correct order so that you can stay alive.")
    print ("")
    print ("    .-'-.        "  +   "   .-'   '-.   "   +   "       \||/        ")
    print ("  .'     '.      "  +   "  /        \   "   +   "       \||/        ")
    print (" /         \     "  +   "  |        |   "   +   "     .<><><>.      ")
    print (":           ;    "  +   "  /'---'--`\   "   +   "    .<><><><>.     ")
    print ("|           |    "  +   " |          |  "   +   "    '<><><><>'     ")
    print (":           :    "  +   " \_.--._.-._/  "   +   "     '<><><>'      ")
    print (" \         /     "  +   "   \=-=-=-/    "   +   "                   ")
    print ("  `.     .'      "  +   "    \=-=-/     "   +   "                   ")
    print ("    '~~~`        "  +   "     \=-/      "   +   "                   ")
    print ("                 "  +   "      \/       "   +   "                   ")
    print ("")



    fight = input("Which item would you like to throw? An egg(1), ice-cream(2) ,or pineapple(3) ")
    if fight == "3":
        print ("    .-'-.        "  +   "   .-'   '-.   "   +   "       \||/        ")
        print ("  .'     '.      "  +   "  /        \   "   +   "       \||/        ")
        print (" /         \     "  +   "  |        |   "   +   "     .<><><>.      ")
        print (":           ;    "  +   "  /'---'--`\   "   +   "    .<><><><>.     ")
        print ("|           |    "  +   " |          |  "   +   "    '<><><><>'     ")
        print (":           :    "  +   " \_.--._.-._/  "   +   "     '<><><>'      ")
        print (" \         /     "  +   "   \=-=-=-/    "   +   "                   ")
        print ("  `.     .'      "  +   "    \=-=-/     "   +   "       HIT         ")
        print ("    '~~~`        "  +   "     \=-/      "   +   "                   ")
        print ("                 "  +   "      \/       "   +   "                   ")
        print ("")
    else:
        print ("You missed ")
        restart = input("Keeping throwing until you hit or quit?  Restart(y) Quit(n)")
        if restart == "y":
            food_fight(done)
        elif restart == "n":
            print ("You will now be attacked by hormonal teenagers after making it so far. Sorry. ")
            done = 'quit'
            return (done)

    fight_2 = input("Which item would you like to throw next? ")

    if fight_2 == "1":
        print ("    .-'-.        "  +   "   .-'   '-.   "   +   "       \||/        ")
        print ("  .'     '.      "  +   "  /        \   "   +   "       \||/        ")
        print (" /         \     "  +   "  |        |   "   +   "     .<><><>.      ")
        print (":           ;    "  +   "  /'---'--`\   "   +   "    .<><><><>.     ")
        print ("|           |    "  +   " |          |  "   +   "    '<><><><>'     ")
        print (":           :    "  +   " \_.--._.-._/  "   +   "     '<><><>'      ")
        print (" \         /     "  +   "   \=-=-=-/    "   +   "                   ")
        print ("  `.     .'      "  +   "    \=-=-/     "   +   "       HIT         ")
        print ("    '~~~`        "  +   "     \=-/      "   +   "                   ")
        print ("     HIT         "  +   "      \/       "   +   "                   ")
        print ("")
    else:
        print ("You missed ")
        print ("    .-'-.        "  +   "   .-'   '-.   "   +   "       \||/        ")
        print ("  .'     '.      "  +   "  /        \   "   +   "       \||/        ")
        print (" /         \     "  +   "  |        |   "   +   "     .<><><>.      ")
        print (":           ;    "  +   "  /'---'--`\   "   +   "    .<><><><>.     ")
        print ("|           |    "  +   " |          |  "   +   "    '<><><><>'     ")
        print (":           :    "  +   " \_.--._.-._/  "   +   "     '<><><>'      ")
        print (" \         /     "  +   "   \=-=-=-/    "   +   "                   ")
        print ("  `.     .'      "  +   "    \=-=-/     "   +   "       HIT         ")
        print ("    '~~~`        "  +   "     \=-/      "   +   "                   ")
        print ("                 "  +   "      \/       "   +   "                   ")
        print ("")
        restart_2 = input("Keeping throwing until you hit or quit?  Restart(y) Quit(n)")
        if restart_2 == "y":
            food_fight(done)
        elif restart_2 == "n":
            print ("You will now be attacked by hormonal teenagers after making it so far. Sorry. ")
            done = 'quit'
            return (done)

    fight_3 = input ("Which is the last item that you would like to throw? ")
    if fight_3 == "2":
        print ("    .-'-.        "  +   "   .-'   '-.   "   +   "       \||/        ")
        print ("  .'     '.      "  +   "  /        \   "   +   "       \||/        ")
        print (" /         \     "  +   "  |        |   "   +   "     .<><><>.      ")
        print (":           ;    "  +   "  /'---'--`\   "   +   "    .<><><><>.     ")
        print ("|           |    "  +   " |          |  "   +   "    '<><><><>'     ")
        print (":           :    "  +   " \_.--._.-._/  "   +   "     '<><><>'      ")
        print (" \         /     "  +   "   \=-=-=-/    "   +   "                   ")
        print ("  `.     .'      "  +   "    \=-=-/     "   +   "       HIT         ")
        print ("    '~~~`        "  +   "     \=-/      "   +   "                   ")
        print ("     HIT         "  +   "      HIT      "   +   "                   ")
        print ("")
        print ("Congrats! You finally made it out of that dumpster. Hope you had fun!")
        done = 'quit'
        return (done)
        
    else:
        print("For some reason, you missed your last shot.. You will now be attacked by hormonal teenagers after making it so far. Sorry.")
        print ("    .-'-.        "  +   "   .-'   '-.   "   +   "       \||/        ")
        print ("  .'     '.      "  +   "  /        \   "   +   "       \||/        ")
        print (" /         \     "  +   "  |        |   "   +   "     .<><><>.      ")
        print (":           ;    "  +   "  /'---'--`\   "   +   "    .<><><><>.     ")
        print ("|           |    "  +   " |          |  "   +   "    '<><><><>'     ")
        print (":           :    "  +   " \_.--._.-._/  "   +   "     '<><><>'      ")
        print (" \         /     "  +   "   \=-=-=-/    "   +   "                   ")
        print ("  `.     .'      "  +   "    \=-=-/     "   +   "       HIT         ")
        print ("    '~~~`        "  +   "     \=-/      "   +   "                   ")
        print ("     HIT         "  +   "      \/       "   +   "                   ")
        print ("")
        restart_3 = input("Keeping throwing until you hit or quit?  Restart(y) Quit(n)")
        if restart_3 == "y":
            food_fight(done)
        elif restart_3 == "n":
            print ("You will now be attacked by hormonal teenagers after making it so far. Sorry.")
            done = 'quit'
            return (done)
    
    
    

    




