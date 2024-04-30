# This code should be able to ask a user to choose a shape, the code then will calculate the area of the specified shape.

print("Welcome to the Humble Calculator.")
print("The Calculator is ready to take information.")
shape= input("What shape would you like us to calculate the area of? (please type C for Circle or T for Triangle): ")
if shape=='C':
  Circle_radius= float(input("Enter the radius of the circle: "))
  area_of_circle= Circle_radius**2*3.14159
  print("Area of the Circle with the radius ",Circle_radius, "is ", area_of_circle)
elif shape=='T':
  base= float(input("Enter the base of the triangle: "))
  height= float(input("Enter the height of thr triangle: "))
  area_of_traingle= 0.5*base*height
  print("The area of the triangle with the base ", base," and the hieght ",height," is ",area_of_traingle)
else:
  print("Apologies, you have entered invalid input.")
print("Thank you for using the Calculator! Good luck on your further calculations.")