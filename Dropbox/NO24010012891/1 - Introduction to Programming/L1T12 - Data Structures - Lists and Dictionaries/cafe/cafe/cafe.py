menu_list = ["Coffee","Tea","Bread","Eggs"] #list of the items in the stock

#Defining dictionary for the value of each stock
stock_dict = {'Coffee':23,
              'Tea':34,
              'Bread':44,
              'Eggs':54}

#Defining dictionary for the price of each stock
price_dict = {'Coffee':12.40,
              'Tea':13.00,
              'Bread':17.50,
              'Eggs':38.90}

total_stock = 0 #Defining a variable for storing total stock
#looping through the the disctionary of the stock
for items in stock_dict:
        #Calculate the value of each item in price dictionary and value dictionary
        item_value = stock_dict[items] * price_dict[items]
        #printing the value of each items available in the Cafe
        if items == "Coffee": 
            print("Item value of coffee is " + str(item_value))
        elif items == "Tea": 
            print("Item value of tea is " + str(item_value))
        elif items == "Bread": 
            print("Item value of bread is " + str(item_value))
        else:
            print("Item value of eggs is " + str(item_value))
        total_stock += item_value #Calculating the total stock in the whole cafe
print("Cafe total stock " + str(total_stock)) #displaying the total stock of the cafe