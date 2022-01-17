print("welcome to Remi's first game called choices!")
name = input("what is your name? ")
print(name)
age = int(input("what is your age? "))


health = 10


if age >= 18:
    print("you are old enough to play this game!")

    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("Let's play!")
        print("you are starting with", health, "health")

        up_or_down = input("First choice... up or down (up/down)? ")
        if up_or_down == "up":
            ans = input("Nice, you follow the path and reach a lake...Do you swim across or go around (across/around)? ")

            if ans == "around":
                print("you went around and reached the other side of the lake")

            elif ans == "across":
                print("You managed to get across but ran into an alligator who bit your leg and lost 5 health")
                health -= 5

            ans = input("You noticed a house and a river. Which do you go to (river/house? ")
            if ans == "house":
                print("you go to the house and are greated by the owner who shows his shot gun and shoots you in the arm and you lose 5 health")
                health -= 5

                if health <= 0:
                    print("you now have 0 health and you lose the game...boohoo")
                else:
                    print("you have survived...so far, but lets work on that.")

                    ans = input("You run away from the house and see a car and a boat, where do you go (car/boat)? ")

                    if ans == "car":
                        print("You find the car keys inside and drive home. You survived and won the game...this time.")

                    else:
                        print("You jump on the boat but the man from the house comes out with a bazooka and blows up the boat with you in it. Got ya....Game Over")


            else:
                print("you found a canoe at the river and used it to cross safely...you have survived, you win!")

           

        else:
            print("you went down into the pits of hell and lost...try again")

    else:
        print("you suck...")
else:
    print("you are not old enough to play, get out of here now!")
