print(f"\n-----------LAB 10: EXERCISE------------")

colorlist = ['red', 'orange', 'olive', 'magenta', 'green']

continuer = True
while continuer:
    user_color = input("Enter a color: ") 
    user_color = user_color.strip()
    user_color = user_color.lower()
    
    if user_color in colorlist:
        print(f"{user_color} is in the list")
    else:
        print(f"{user_color} IS NOT in the list")
    
    # Optional: add a way to exit the loop
    continue_response = input("Do you want to check another color? (yes/no): ")
    if continue_response.lower() != "yes":
        continuer = False
