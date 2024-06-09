# greeting.py

def main():
    try:
        # Ask for user's name
        name = input("What is your name? ")

        # Ask for user's age and convert it to an integer
        age = int(input("How old are you? "))

        # Calculate the birth year
        current_year = 2024
        birth_year = current_year - age

        # Print the greeting and birth year
        print(f"Hello, {name}! You were born in {birth_year}.")

    except ValueError:
        print("Please enter a valid age.")
        main()


# Entry point of the application
if __name__ == "__main__":
    main()
