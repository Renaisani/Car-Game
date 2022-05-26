car_state = False
while True:
    user_input = input(">").lower()
    if user_input == "help":
        print("start - start your car")
        print("stop - stop your car")
        print("quit - quit the game")
        print("")
    elif user_input == "start":
        if car_state == False:
            print("Car started..Let's Go!")
            car_state = True
        else:
            print("Car is already on")
    elif user_input == "stop":
        if car_state == True:
            print("Car has stopped")
            car_state = False
        else:
            print("Car is already off")
    elif user_input == "quit":
        break
    else:
        print("I don't understand")
