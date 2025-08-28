print("\n--- Temperature Converter ---")
choice = input("Convert to (C/F)? ").upper()
temp = float(input("Enter temperature: "))

if choice == "C":
    print("In Celsius:", (temp - 32) * 5 / 9)
elif choice == "F":
    print("In Fahrenheit:", (temp * 9 / 5) + 32)
else:
    print("Invalid choice")