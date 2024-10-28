# Lea Trueworthy
# October 27, 2024
# CSD 325 - Module 1.3 Assignment: On the Wall + Flowchart(s)
# Description: Create a program simulating the "100 Bottles of Beer" countdown song.
# Prompt the user for the number of bottles, implement a countdown function to display the lyrics, and remind the user to buy more beer at the end.

def counted_bottles (bottles):

    if bottles > 1:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        print(f"Take one down, pass it around, {bottles - 1} bottle(s) of beer on the wall. \n")
        counted_bottles (bottles - 1)

    elif bottles == 1:
        print("One bottle of beer on the wall, one bottle of beer.")
        print("Take one down pass it around, no more bottles of beer on the wall. \n")
        print("Go buy more beer!")
        
    else:
        print("No more bottles of beer on the wall. Time to buy more beer!")


def main():
    try:
        # Get input from the user
        bottles = int(input("Enter the number of bottles: "))

        # Check if input is positive
        if bottles < 0:
            print("Please enter a positive nuumber.")
        else:
            counted_bottles(bottles)

    except ValueError:
        print("Invalid input. Please enter a whole number.")


if __name__ == "__main__":
    main()