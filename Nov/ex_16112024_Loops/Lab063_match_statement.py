# Match statement -> #similar to switch in Java

# Write a program to ask the user which browser he wants to run automation

browser_name = input('Enter the browser Name:\n')
match browser_name:
    case "firefox":
        print("Starting Firefox!!!")
    case "chrome":
        print("Starting chrome!!!")
    case "edge":
        print("Starting edge!!!")
    case "safari":
        print("Starting safari!!!")
    case _: #default case
        print("Browser not found!")
