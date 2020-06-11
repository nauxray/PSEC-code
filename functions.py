# Display menu
def displayMenu(todaysMenu, menu, cartList):
    while True:
        dayDict = {
            0: "Monday",
            1: "Tuesday",
            2: "Wednesday",
            3: "Thursday",
            4: "Friday",
            5: "Saturday",
            6: "Sunday"
        }
        print(f'{"":=^38}')
        print(f'{"MENU FOR TODAY": ^38}')
        print(f'{"":=^38}')

        # Filtering the menu items
        for i in range(0, len(todaysMenu)):
            print(str(i+1)+".", todaysMenu[i]['Menu Item'].ljust(25),
                  ':\t$' + todaysMenu[i]['Price'].ljust(25))
        try:
            print(f'{"":=^38}')
            cartChoice = input(
                f'What would you like today?\nPlease enter the number of the item you would like\n\nEnter H to go back to the home page\nEnter M to view the menu for each day\n\n>> ')
            if cartChoice.lower() == "h":
                action = ""
                return action
                break
            elif cartChoice.lower() == "m":
                day = 7
                for i in range(0, len(menu)):
                    if day == int(menu[i]["Day"]):
                        print(
                            str(i+1)+".", menu[i]['Menu Item'].ljust(25), ':\t$' + menu[i]['Price'].ljust(25))
                    else:
                        day = int(menu[i]["Day"])
                        print(f'{"":=^38}')
                        print(f'{dayDict[day]: ^38}')
                        print(f'{"":=^38}')
                        print(
                            str(i+1)+".", menu[i]['Menu Item'].ljust(25), ':\t$' + menu[i]['Price'].ljust(25))
                print(f'{"":=^38}')
                menuAction = input(
                    "Enter any key to go back to today's menu\nEnter H to go back to the home page\n>> ")
                if menuAction.lower() == "h":
                    action = ""
                    return action
                    break
                else:
                    pass
            elif int(cartChoice) <= 0 or int(cartChoice) > len(todaysMenu):
                raise ValueError
            else:
                cartChoice = int(cartChoice)
                cartList.append(todaysMenu[cartChoice-1])
                print(f'{"":=^38}')
                print(
                    f'[{todaysMenu[cartChoice-1]["Menu Item"]}] has been added to your cart')
                continue
        except (ValueError):
            print(f'{"":-^38}')
            print(f'{"Invalid input. Please try again.": ^38}')
            continue

# Search menu
def searchMenu(todaysMenu,menu,cartList):
    while True:
        print(f'{"":=^38}')
        searchTerm = str(
            input("What are you looking for?\nEnter 1 to go back to the home page\n\n>> "))
        searchedMenu = []
        if searchTerm == "1":
            action = ''
            return action
            break
        else:
            for entry in todaysMenu:
                if searchTerm.lower() in (entry["Menu Item"]).lower():
                    searchedMenu.append(entry)
            if len(searchedMenu) == 0:
                print(f'{"":=^38}')
                searchAction = input(
                    "No search results found.\nEnter any key to try again\nEnter H to go back to the home page\n\n>> ")
                if searchAction.lower() == "h":
                    action = ''
                    return action
                    break
                else:
                    continue
            else:
                print(f'{"":=^38}')
                for i in range(0, len(searchedMenu)):
                    print(str(i+1)+".", searchedMenu[i]['Menu Item'].ljust(
                        25), ':\t', searchedMenu[i]['Price'].ljust(15))
                try:
                    print(f'{"":=^38}')
                    cartChoice = int(input(
                        f'What would you like today?\nPlease enter the number of the item you would like\n >> '))
                    cartList.append(searchedMenu[cartChoice-1])
                    print(f'{"":-^38}')
                    print(
                        f'[{searchedMenu[cartChoice-1]["Menu Item"]}] has been added to your cart')
                except (ValueError, IndexError):
                    print(f'{"":-^38}')
                    print(f'{"Invalid input. Please try again.": ^38}')
                continue
            break

# Edit cart
def editCart(todaysMenu,menu,cartList):
    while len(cartList) != 0:
        print(f'{"":=^38}')
        print(f'{"EDIT CART": ^38}')
        print(f'{"This is your cart now:": ^38}')
        print(f'{"":=^38}')
        for i in range(0, len(cartList)):
            print(str(i+1)+".", cartList[i]['Menu Item'].ljust(25),
                  ':\t', cartList[i]['Price'].ljust(15))
        print(f'{"":=^38}')
        try:
            removeItem = input(
                "Please enter the number of the item you would like to remove\nEnter H to go back to the home page\n>> ")
            if removeItem.lower() == "h":
                action = ''
                return action
                break
            elif len(cartList) != 0:
                if int(removeItem) <= 0:
                    print(f'{"":-^38}')
                    print(f'{"Invalid input. Please try again.": ^38}')
                    print(f'{"":-^38}')
                    continue
                else:
                    removeItem = int(removeItem)
                    del cartList[removeItem-1]
            else:
                continue
        except (IndexError, ValueError):
            print(f'{"":-^38}')
            print(f'{"Invalid input. Please try again.": ^38}')
            print(f'{"":-^38}')
            continue
        pass
    else:
        while len(cartList) == 0:
            print(f'{"":=^38}')
            print(f'{"Your cart is empty.": ^38}')
            print(f'{"":=^38}')
            EmptyCartAction = input(
                "Enter H to go back to the home page\nEnter Q to exit the program\n>> ")
            if EmptyCartAction.lower() == "h":
                action = ""
                return action
                break
            elif EmptyCartAction.lower() == "q":
                action = "q"
                return action
                break
            else:
                print(f'{"":-^38}')
                print(f'{"Invalid input. Please try again.": ^38}')
                print(f'{"":-^38}')

# Display cart
def displayCart(todaysMenu,menu,cartList):
    while len(cartList) == 0:
        print(f'{"":=^40}')
        print(f'{"Your cart is empty.": ^38}')
        print(f'{"":=^40}')
        emptyCartAction = input(
            "Enter H to go back to the home page\nEnter Q to exit the program\n>> ")
        if emptyCartAction.lower() == "h":
            action = ""
            return action
            break
        elif emptyCartAction.lower() == "q":
            action = "q"
            return action
            break
        else:
            print(f'{"":-^40}')
            print(f'{"Invalid input. Please try again.": ^38}')
            print(f'{"":-^40}')
            continue
    while len(cartList) > 0:
        print(f'{"":=^38}')
        print(f'{"This is your cart now:": ^38}')
        print(f'{"":=^38}')
        for i in range(0, len(cartList)):
            print(str(i+1)+".", cartList[i]['Menu Item'].ljust(25),
                  ':\t$' + cartList[i]['Price'].ljust(15))
        print(f'{"":=^38}')
        cartAction = input(
            f'Enter H to go back to the home page\nEnter C to go to the check out page\nIn order to edit your cart, enter E\n>> ')
        print(f'{"":=^38}')
        if cartAction.lower() == "h":
            action = ""
            return action
            break
        elif cartAction.lower() == "c":
            action = "4"
            return action
            break
        elif cartAction.lower() == "e":
            action = "5"
            return action
            break
        else:
            print(f'{"":-^38}')
            print(f'{"Invalid input. Please try again.": ^38}')
            print(f'{"":-^38}')
            continue

# Check out
def checkOut(todaysMenu,menu,cartList):
    if len(cartList) != 0:
        print(f'{"":=^38}')
        print(f'{"This is your cart now:": ^38}')
        print(f'{"":=^38}')
        for i in range(0, len(cartList)):
            print(str(i+1)+".", cartList[i]['Menu Item'].ljust(25),
                  ':\t$'+cartList[i]['Price'].ljust(15))
            print(f'{"":=^38}')     
        total = 0
        for i in range(0, len(cartList)):
            total += float(cartList[i]['Price'])
        print(f"Your total is ${total:.2f}")
        print(f'{"":=^38}')
        while True:
            try:
                check = input(
                    f'Enter C to check out or H to go back to the home page\n>> ')
                if check.lower() == "c":
                    action = "q"
                    return action
                    break
                elif check.lower() == "h":
                    action = ""
                    return action
                    break
            except KeyError:
                print(f'{"":-^38}')
                print(f'{"Invalid input. Please try again.": ^38}')
                print(f'{"":-^38}')
                continue
            pass
        pass
    else:
        while len(cartList) == 0:
            print(f'{"":=^38}')
            print(f'{"Your cart is empty.": ^38}')
            print(f'{"":=^38}')
            emptyCartAction = input(
                "Enter H to go back to the home page\nEnter Q to exit the program\n>> ")
            if emptyCartAction.lower() == "h":
                action = ""
                return action
                break
            elif emptyCartAction.lower() == "q":
                action = "q"
                return action
                break
            else:
                print(f'{"":-^38}')
                print(f'{"Invalid input. Please try again.": ^38}')
                print(f'{"":-^38}')
            break
        pass
    pass

# Show home page
def showHome():
    print(f'{"":=^38}')
    print(f'{"Welcome to SPAM": ^38}')
    print(f'{"":=^38}')
    print("1. Display Today's Menu \n2. Search Menu\n3. Display Cart\n4. Check Out\n5. Edit Cart")
    action = input(
        f'======================================\n{"Enter Q to quit": ^38}\n======================================\n>> ')
    return action

# Prevent functions from running automatically when imported into client.py
if __name__ == "__main__":
    displayMenu(),
    searchMenu(),
    editCart(),
    displayCart(),
    checkOut(),
    showHome()