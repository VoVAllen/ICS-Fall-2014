pocket = int(input("Which roulette pocket would you like to check (0-36)? - "))

if (pocket >= 1 and pocket <= 10) or (pocket >= 19 and pocket <= 28):

    if pocket % 2 == 1:
        print("That pocket is red!")
    else:
        print("That pocket is black!")


elif (pocket >= 11 and pocket <= 18) or (pocket >= 29 and pocket <= 36):

    if pocket % 2 == 1:
        print("That pocket is black!")
    else:
        print("That pocket is red!")

elif pocket == 0:
    print("That pocket is green!")

else:
    print("There has been an error.")
