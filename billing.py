stock ={}
prices ={}
purchase={}
total=0
stock["Banana"]=5
stock["Apple"]=7
stock["Orange"]=9

prices["Banana"]=2
prices["Apple"]=6
prices["Orange"]=4


while True:
  item=input("Item: ")
  if item.upper()=="DONE":
    break
  if item not in stock:
    print("Item  not in stock")
    continue
  else:
    while True:
      quantity=input("Quantity: ")
      try:
        quantity=int(quantity)
        break
      except:
        print("Enter valid quantity")
        continue
    if quantity>stock[item]:
      print ("We can't match that order, we only have",stock[item],item,"left")
    else:
      stock[item]=stock[item]-quantity
      purchase[item]=purchase.get(item,0)+quantity
      bill=purchase[item]*prices[item]  
      total+=bill
    if stock[item]<3 and stock[item]!=0:
      print("Restock",item,"fast!!! Only",stock[item],"left.")
    elif stock[item]==0:
      print("Now you're out of", item,"'s")
print ("Customer Bill")
for good,unit in purchase.items():
  print("Item:",good, "Quantity:",unit,"Amount:",unit*prices[good])
print ("Total bill:",total)
