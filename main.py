i = 1
car_state = False
while i == 1:
    user_input = input(">")
    if user_input.lower() == "help":
        print("start - start your car")
        print("stop - stop your car")
        print("quit - quit the game")
        print("")
    elif user_input.lower() == "start":
        if car_state == False:
            print("Car started..Let's Go!")
            car_state = True
        else:
            print("Car is already on")
    elif user_input.lower() == "stop":
        if car_state == True:
            print("Car has stopped")
            car_state = False
        else:
            print("Car is already off")
    elif user_input.lower() == "quit":
        break
    else:
        print("I don't understand")
