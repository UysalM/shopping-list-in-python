import os
def clear():
  os.system('cls')

shopping_list = []
loop_condition = True

def add_item():
  clear()
  item = input('Enter item name or press enter to return to operation menu: ')
  if len(item) > 0:
    shopping_list.append(item + '\n')
    print(item + ' is added to the list')
  else:
    print('No items were added, returning to operation menu')

def remove_item():
  clear()
  for i in range(len(shopping_list)):
      print(shopping_list[i])
  item = input('Enter item name you wish to remove from the list or press enter to return to operation menu: ')
  if len(item) > 0:
    shopping_list.remove(item + '\n')
    print(item + ' is removed.')
  else:
    print("No items were removed")

def show_list():
  clear()
  for i in range(len(shopping_list)):
      print(str(i+1) +' - ' + shopping_list[i])

def save_exit():
    clear()
    print("Saving list to a text file.")
    list_file = open("Shopping_List.txt", "w")
    list_file.writelines(shopping_list)
    list_file.close()

while loop_condition:
  print("You have " + str(len(shopping_list)) + " items in your list.")
  print('Select operation or press enter to exit')
  print("""
  1) Add new item to the list
  2) Remove an item from the list
  3) Show list of items
  4) Save list to a text file and exit""")
  operation = input()
  if len(operation) > 0:
    if int(operation) == 1:
      add_item()
    elif int(operation) == 2:
      remove_item()
    elif int(operation) == 3:
      show_list()
    elif int(operation) == 4:
      save_exit()
      break
  else:
    print('Exiting')
    loop_condition = False
