#Kimberly Orozco, Module 1.3 Assignment, June 7, 2025
#Purpose: Create the Reverse counting song "100 Bottles of beer on the wall"

def countdown(n):
    while n > 1:
        print(f"{n} bottles of beer on the wall, {n} bottles of beer.")
        print(f"Take one down, pass it around, {n-1} bottles of beer on the wall.\n")
        n -= 1  
  
    if n == 1:
        print("1 bottle of beer on the wall, 1 bottle of beer.")
        print("Take one down, pass it around, no more bottles of beer on the wall.\n")

def main():
    user_input = input("How many bottles of beer on the wall? ")
    
    try:
        start = int(user_input)
        if start < 1:
            print("Please enter a positive integer.")
            return
    except ValueError:
        print("That's not a valid number.")
        return

    countdown(start)

    print("Go to the store and buy more beer!")

if __name__ == "__main__":
    main()