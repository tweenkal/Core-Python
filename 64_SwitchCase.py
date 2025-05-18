# 👉Switch Case:-

def switch_case_example(value):
    match value:
        case 1:
            print("You chose One")
        case 2:
            print("You chose Two")
        case 3:
            print("You chose Three")
        case _:
            print("Invalid choice")

# Example usage:
choice = int(input("Enter a number (1-3): "))
switch_case_example(choice)
