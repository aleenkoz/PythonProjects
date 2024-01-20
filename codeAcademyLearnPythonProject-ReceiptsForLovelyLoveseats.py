loveley_loveseat_discription="Loveley Loveseat. Tufted polyster blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
loveley_loveseat_price=254.00
stylish_settee_discription=" Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches deep. Black."
stylish_settee_price=180.50
luxurios_lamp_discription=" Luxurios Lamp. Glass and iron. 36 inches tall. Brown with cream shade"
luxurios_lamp_price=52.15
sales_tax=0.088
customer_one_total=0
customer_one_itemization=""
customer_one_total+=loveley_loveseat_price
customer_one_itemization+=loveley_loveseat_discription
customer_one_total+=luxurios_lamp_price
customer_one_itemization+=luxurios_lamp_discription
customer_one_tax=customer_one_total*sales_tax
customer_one_total+=customer_one_tax
print("Customer One Items: ")
print(customer_one_itemization)
print("Customer One Total: ")
print(customer_one_total)