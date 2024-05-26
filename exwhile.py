available_exit = "UpRight"

chosen_exit = ""
while chosen_exit != available_exit:
    
    chosen_exit = input("Too ye to bta hai kidhar  :  ")
    if available_exit == chosen_exit:
        print(f"You are at right direction {chosen_exit}")
        break
    else:
        print("samj nai a rahi yar dobara bta to kidhar hai")

