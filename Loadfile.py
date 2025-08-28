print("\n--- File Summary ---")
try:
    with open("File.txt", "r") as file:
        text = file.read()
        words = text.split()
        print("Total characters:", len(text))
        print("Total words:", len(words))
        print("Total lines:", text.count("\n") + 1)
except FileNotFoundError:
    print("File not found! Please create 'File.txt'")