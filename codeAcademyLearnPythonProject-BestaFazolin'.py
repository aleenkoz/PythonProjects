#The Business class:
class Business:
  def __init__ (self, name, franchises):
    self.name = name
    self.franchises = franchises

#The franchise class:
class Franchise:
  def __init__ (self,address,menues):
    self.address = address
    self.menues = menues
    
  def __repr__ (self):
    return "The address of this franchise is " + self.address

  def available_menues (self, time):
    available_menues=[]
    for menu in self.menues:
      if time >= menu.start_time  and time <= menu.end_time:
        available_menues.append(menu)
    return available_menues

#menus class:
class Menu:
  def __init__(self,name,items,start_time,end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return self.name + " is available from " + str(self.start_time) + " and to "+ str(self.end_time)

  def calculate_bill (self, purchased_items):
    bill=0
    for item in purchased_items:
      if item in self.items:
        bill+= self.items[item]
    return bill
#menus and thier items:
brunch_items = {
    'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee':1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50,
   } 
brunch = Menu("Brunch", brunch_items, 1100, 1600)
early_bird_items= {
    'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushrooms ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
   }
early_bird= Menu("Early Bird Dinner", early_bird_items, 1500, 1800)
dinner_items= {
 'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00, 
}
dinner= Menu('Dinner', dinner_items, 1700, 2300)
kids_items= {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
kids= Menu('Kids', kids_items, 1100, 2000)
take_a_arepa_items= {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
  }
take_a_arepa_menu= Menu('Take a\' Arepa', take_a_arepa_items,1000,1900)

#use of the "calculate bill" method:
print('Customer No.1 ordered for a price of ')
print(brunch.calculate_bill(['pancakes','home fries', 'coffee']))
print('Customer No.104 ordered for a price of ')
print(early_bird.calculate_bill(['salumeria plate', 'mushrooms ravioli (vegan)']))

# Two variables that fall under the 'Franchise' class.
flagship_store= Franchise('1232 West End Road',[brunch,early_bird,dinner,kids])
new_installment= Franchise('12 East Mulberry Street',[brunch,early_bird, dinner,kids])
arepas_place= Franchise('189 Fitzgerald Avenue',[take_a_arepa_menu])

#Trying the 'available menues' method.
print(flagship_store.available_menues(1600))
print(new_installment.available_menues(1700))
#Note that the times were reprsented in numbers to ease the comparision process.

#Some businesses under the 'Bussiness' class:
basta_fazoolin_with_my_heart= Business('Basta Fazoolin\' with my Heart',[flagship_store, new_installment])
take_a_arepa= Business('Take a\' Arepa',[arepas_place])