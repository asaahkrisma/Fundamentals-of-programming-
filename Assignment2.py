print("You're welcome to the CATUC POST")
sum_items = int(input("\nPlease enter the number of items bought:"))
items_SN =[]
items_name=[]
items_quantity= []
items_cost = []

for item in range(1,sum_items+1):
  SN = int(input(f"\n Please enter the Serial number {item}:"))
  items_SN.append(SN)
  name = input("\nPlease the  item name {item}:")
  items_name.append(name)
  quantity = int(input("\nPlease enter the item quantity of item {item}:"))
  items_quantity.append(quantity)
  cost = float(input(f"\nPlease input the cost if item {item}:"))
  items_cost.append(cost)
items_cost_total = sum(items_cost)
if items_cost_total > 10000:
  discount = 0.30*items_cost_total
  total_cost = items_cost_total-discount
  print(f"\nTotal purchase = {total_cost}frs\n Thanks for your patronage")
elif(len({items_cost}) > 5) and
(items_cost_total > 4000):
  discount = 0.15*items_cost_total
  total_cost = items_cost_total-discount
  print(f"\nTotal purchase = {total_cost}frs\n Thanks for your patronage")
elif items_cost > 5000:
  discount = 0.10*items_cost_total
  total_cost = items_cost_total-discount
  print(f"\nTotal purchase = {total_cost}frs\n Thanks for your patronage")
else:
  total_cost = items_cost_total
  print(f"\nTotal purchase = {total_cost}frs\n Thanks for your patronage")
        
