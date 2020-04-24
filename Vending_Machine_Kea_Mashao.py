#Program By: Keamogetswe Mashao
#This program will simulate the experience at a vending machine
#This program also incorporates menu optiions within its if-statements

import time

print ("Welcome to the Python Vending Machine.")
# Asking the user how much money they wish to enter.
number_of_50c = int(input("How many 50 cent coins would you like to insert? "))
while number_of_50c < 0:
    number_of_50c = int(input("Please enter a positive number."))
number_of_R1 = int(input("How many R1 coins would you like to insert? "))
while number_of_R1 < 0:
    number_of_R1 = int(input("Please enter a positive number."))

number_of_R2 = int(input("How many R2 coins would you like to insert? "))
while number_of_R2 < 0:
    number_of_R2 = int(input("Please enter a positive number."))
number_of_R5 = int(input("How many R5 coins would you like to insert? "))
while number_of_R5< 0:
    number_of_R5 = int(input("Please enter a positive number."))
#Creating a variable to store the total amount of money inserted into the vending machine.
change = round(((number_of_50c * 0.50) + (number_of_R1 * 1.00) + (number_of_R2 * 2.00) + (number_of_R5 * 5.00)),2)
#Informing the user how much they have entered in total.
print ("\nIn total you have entered R", change)
time.sleep(2)
#Creating variables for the 5 products and their respective prices. 
product_1, product_1_price = "Crisps", 8.00
product_2, product_2_price = "Chocolate", 11.00
product_3, product_3_price = "ColdDrink", 10.00
product_4, product_4_price = "Sweets", 8.00
product_5, product_5_price = "HealthySnack", 10.00
#Creating variables to track the number of each items bought,
Crisps_bought = 0
Chocolate_bought = 0
ColdDrink_bought = 0
Sweets_bought = 0
HealthySnack_bought = 0
#Informing the user of the choices available and the price of each item.
print ("There are 5 products available to pick from;\n")
time.sleep(2)
print ("Item: {}, Price {} ".format(product_1, product_1_price))
print ("Item: {}, Price {} ".format(product_2, product_2_price))
print ("Item: {}, Price {} ".format(product_3, product_3_price))
print ("Item: {}, Price {} ".format(product_4, product_4_price))
print ("Item: {}, Price {} ".format(product_5, product_5_price))
print ("")
#Asking the user to make a selection.
while change > 0:
    customer_choice = input("What would you like to buy? Type N when you are finished \n")
    if customer_choice == "Crisps" or customer_choice == "crisps" and change >= product_1_price:
        print ("You have chosen a", product_1, "these cost", product_1_price, "each,")
        change = round((change - product_1_price),2)
        Crisps_bought = (Crisps_bought + 1)
        print ("You have this much money remaining: R", change)
        #Giving the user further choices
        menu2= """
            Please select one of following options s-e):
            s) Simba
            l) Lays
            cc) Cheesecurls
            n) Niknaks
            p) Pretzels
            e) Exit
            """
        option = str(input(menu2))
        while option != "e":
            if option == "s":
                print("Enjoy your simba crisps!")
                break
            if option == "l":
                print("Enjoy your lays crisps!")
                break
            if option == "cc":
                print("Enjoy your cheesecurls!")
                break
            if option == "n":
                print("Enjoy your niknaks!")
                break
            if option == "p":
                print("Enjoy your pretzels!")
                break
    elif customer_choice == "Chocolate" or customer_choice == "chocolate" and change >= product_2_price:
        print ("You have chosen a", product_2, "these cost", product_2_price, "each,")
        change = round((change - product_2_price),2)
        Chocolate_bought = (Chocolate_bought + 1)
        print ("You have this much money remaining: R", change)
        #Giving the user further choices
        menu3= """
            Please select one of following options A-e):
            A) Aero
            B) Bar-One
            K) Kit-Kat
            LB) LunchBar
            T) Tex
            e) Exit
            """
        option = str(input(menu3))
        while option != "e":
            if option == "A":
                print("Enjoy your aero!")
                break
            if option == "B":
               print("Enjoy your bar-one!")
               break
            if option == "K":
                print("Enjoy your Kit-Kat!")
                break
            if option == "LB":
                print("Enjoy your LunchBar!")
                break
            if option == "T":
                print("Enjoy your Tex!")
                break
    elif customer_choice == "ColdDrink" or customer_choice == "colddrink" and change >= product_3_price:
        print ("You have chosen a", product_3, "these cost", product_3_price, "each,")
        change = round((change - product_3_price),2)
        ColdDrink_bought = (ColdDrink_bought + 1)
        print ("You have this much money remaining: R", change)
        #Giving the user further choices
        menu3= """
            Please select one of following options CK-e):
            CK) Coke
            F) Fanta
            S) Sprite
            ST) Stoney
            M) Mountain-Dew
            e) Exit
            """
        option = str(input(menu3))
        while option != "e":
            if option == "CK":
                print("Enjoy your Coke!")
                break
            if option == "F":
                print("Enjoy your Fanta!")
                break
            if option == "S":
                print("Enjoy your Sprite!")
                break
            if option == "ST":
                print("Enjoy your Stoney!")
                break
            if option == "M":
                print("Enjoy your Mountain-Dew!")
                break
    elif customer_choice == "Sweets" or customer_choice == "sweets" and change >= product_4_price:
        print ("You have chosen a", product_4, "these cost", product_4_price, "each,")
        change = round((change - product_4_price),2)
        Sweets_bought = (Sweets_bought + 1)
        print ("You have this much money remaining: R", change)
        #Giving the user further choices
        menu4= """
            Please select one of following options W-e):
            W) WineGums
            J) JellyBabies
            SE) SpeckledEggs
            MT) Mints
            FT) Fruities
            e) Exit
            """
        option = str(input(menu4))
        while option != "e":
            if option == "W":
                print("Enjoy your WineGums!")
                break
            if option == "J":
                print("Enjoy your JellyBabies!")
                break
            if option == "SE":
                print("Enjoy your SpeckledEggs!")
                break
            if option == "MT":
                print("Enjoy your Mints!")
                break
            if option == "FT":
                print("Enjoy your Fruties!")
                break
    elif customer_choice == "HealthySnack" or customer_choice == "healthysnack" and change >= product_5_price:
        print ("You have chosen a", product_5, "these cost", product_5_price, "each,")
        change = round((change - product_5_price),2)
        HealthySnack_bought = (HealthySnack_bought + 1)
        print ("You have this much money remaining: R", change)
        #Giving the user further choices
        menu5= """
            Please select one of following options N-e):
            N) Nuts
            D) Dried Fruit
            MT) Mints
            FT) Fruities
            e) Exit
            """
        option = str(input(menu5))
        while option != "e":
            if option == "N":
                print("Enjoy your Nuts!")
                break
            if option == "D":
                print("Enjoy your Dried!")
                break
            if option == "MT":
                print("Enjoy your mints!")
                break
            if option == "FT":
                print("Enjoy your Fruties!")
                break
            
        #Once user has finished with their purchases and left the menu, a print out of their transaction details
    elif customer_choice == "N" or customer_choice == "n":
        print ("\nHere is your transaction details:\n")
        print ("You purchased: ")
        print (product_1, "x", Crisps_bought)
        print (product_2, "x", Chocolate_bought)
        print (product_3, "x", ColdDrink_bought)
        print (product_4, "x", Sweets_bought)
        print (product_5, "x", HealthySnack_bought)
        #Change remaining that the user has
        print ("You have R", change, "remaining.")
        break
    #condition if user has run out of funds
    elif change <= 0:
        print ("You have run out of money.")
        print ("\nHere is your transaction details:\n")
        print ("You purchased: ")
        print (product_1, "x", Crisps_bought)
        print (product_2, "x", Chocolate_bought)
        print (product_3, "x", ColdDrink_bought)
        print (product_4, "x", Sweets_bought)
        print (product_5, "x", HealthySnack_bought)
        break
    #error statement
    else:
        print ("There has been an error or you may not have enough credit.")