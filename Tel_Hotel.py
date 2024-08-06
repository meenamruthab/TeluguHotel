#defining the dict of menu as a list of Items the customer 
Menu = {
    "Dosa" : 40,
    "Idly" : 25,
    "Poori" : 35,
    "Roti": 45,
    "Upma" : 30,
    }
#Printing the welcoming and available foods
print("Welocome to the Telugu Hotel :)")
print("Dosa: Rs.40\nIdly: Rs.25\nPoori: Rs.35\nRoti: Rs.45\nUpma: Rs.35\n ")

#price of order is 0 at the beginning
order_total = 0

#about item1
item_1 = input("Enter the name of the iteam that u want to order: ")
if item_1 in Menu:
    order_total += Menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not available yet!!")

#If another item is ordered or not then, that item
another_order = input("Do you want to add another item ? (Yes/No)- ")
if another_order == "Yes":
    item_2 = input("Enter the name of second item that you want to order:")
    if item_2 in Menu:
        order_total += Menu[item_2]
        print(f"Your order {item_2} has been successfully added")
    else:
        print(f"Ordered iteam {item_2} has not availble!")

#showing the total Cost/Price
print(f"the total amount of items that you ordered is :{order_total}")