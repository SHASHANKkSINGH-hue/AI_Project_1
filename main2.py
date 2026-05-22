def print_receipt(item_dict,total):
      print("\n---Final Report---")
      print("Receipt:")
             # print(purchased_items)   #unpacking dictionary horizontally

              # 1. The For Loop: Unpacking the dictionary vertically
      for item, price in item_dict.items():
           print(f"- {item}: {price}")
       
       
      print(f"Total spent:{total}")

print("---Expense tracker activated---")
print("Type'quit' anytime to exit! \n")

purchased_items={}
Amount_spent=0.0

item_count =1
while True:
       item_name= input(f"What is #{item_count} buy today?\n ")

       if item_name.lower()=="quit":
              
              print_receipt(purchased_items,Amount_spent)
             
              print("Saving Data...exiting")
              break
       

       item_price= float(input("What is the cost?\n "))

       purchased_items[item_name]=item_price   #this for dictionary- value attached to key


      # purchased_items.append(item_name)  ->This is for list
       Amount_spent += item_price   
       item_count +=1


       print(f"Success,you spent {item_price} on {item_name}")
