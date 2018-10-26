item_1 = int (input ('Enter price of first item:  ')[:-1]) # item prices are whole numbers integers and

item_2 = int (input ('Enter price of second item: ')[:-1])  #'[:-1]' removes the pence from the phrase

item_3 = int (input ('Enter price of third item:  ')[:-1])

item_4 = int (input ('Enter price of fourth item: ')[:-1])

item_5 = int (input ('Enter price of fifth item:  ')[:-1])

tuple_1 = (item_1, item_2, item_3, item_4, item_5) # tuple used to clearly list the price of items entered

print ('The prices of the items being displayed as integers are:'+ str(tuple_1)) # tuple is printed to display the list

total_price = sum(tuple_1) # the sum of the tuple is to generate a total price

average_price = total_price / len(tuple_1) # len is length and is used as length of tuple in single numbers
print ('The total price: ' + str (total_price) + 'p.' )
print ('The average price is: ' + str (average_price) + 'p.')
print ('The highest priced item: ' + str(max(tuple_1)) + 'p.') #max tuple = biggest number from the tuple
print ('The lowest priced item: ' + str(min(tuple_1)) + 'p.') # min tuple = lowest number from the tuple