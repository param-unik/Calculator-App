from calc_func import *


def main():
    print("Welcome to Calculator App")
    print(
        """
          \nSelect the function from the given options
          1. Add
          2. Subtract
          """
    )

    user_input = input("Select the function..")

    input1 = int(input("Enter value of 1st number "))
    input2 = int(input("Enter value of 2nd number "))

    if user_input == "1":
        result = do_addition(input1, input2)
    elif user_input == "2":
        result = do_subtract(input1, input2)
    else:
        print("Wrong input. Rerun the app!")


if __name__ == "__main__":
    main()
