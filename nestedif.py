#if we have one condition which depends on another codition then we used nested if statment like

firstLocation = input("Please Enter Your First Location:  ")
secondLocation= input("Please Enter Your Second Location:  ")

if firstLocation == "Right":
    if secondLocation == "Up":
        print(f"Your are at {firstLocation}  {secondLocation} Direction")
    elif secondLocation == "Down":
        print(f"You are at {firstLocation} {secondLocation} Direction")
    else:
        print("Please check your location and Enter again. Your direction is invalid")

else:
    if secondLocation == "Up":
        print(f"Your are at {firstLocation}  {secondLocation} Direction")
    elif secondLocation == "Down":
        print(f"You are at {firstLocation} {secondLocation} Direction")
    else:
        print("Please check your location and Enter again. Your direction is invalid")