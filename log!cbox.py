Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
while True:
    print("\nWelcome to the Pattern Generator and Number Analyzer!")
    print("\nSelect an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        rows = int(input("Enter the number of rows for the pattern: "))

        print("\nPattern:")
        for i in range(1, rows + 1):
            print("*" * i)

    elif choice == 2:
        start = int(input("\nEnter the start of the range: "))
        end = int(input("Enter the end of the range: "))

        total = 0

        for num in range(start, end + 1):
            if num % 2 == 0:
                print(f"Number {num} is Even")
            else:
                print(f"Number {num} is Odd")

            total += num

        print(f"Sum of all numbers from {start} to {end} is: {total}")

    elif choice == 3:
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")

        

Welcome to the Pattern Generator and Number Analyzer!

Select an option:
1. Generate a Pattern
2. Analyze a Range of Numbers
3. Exit
Enter your choice: 1
Enter the number of rows for the pattern: 6

Pattern:
*
**
***
****
*****
******

Welcome to the Pattern Generator and Number Analyzer!

Select an option:
1. Generate a Pattern
2. Analyze a Range of Numbers
3. Exit
Enter your choice: 2

Enter the start of the range: 8
Enter the end of the range: 13
Number 8 is Even
Number 9 is Odd
Number 10 is Even
Number 11 is Odd
Number 12 is Even
Number 13 is Odd
Sum of all numbers from 8 to 13 is: 63

Welcome to the Pattern Generator and Number Analyzer!

Select an option:
1. Generate a Pattern
2. Analyze a Range of Numbers
3. Exit
Enter your choice: 3
Exiting the program. Goodbye!
