def easterEggFunction():
    while True:
        fName = input("Enter File Name (or type 'exit' to quit): ")

        # Check for the exit command to break the loop
        if fName.lower() == "exit":
            print("Exiting the program.")
            break

        # Easter egg check
        if fName.lower() == "na na boo boo":
            print("NA NA BOO BOO TO YOU - You have been punk'd!")
            continue  # Skip to the next iteration of the loop

        # Try to open the file
        try:
            fhand = open(fName)
        except:
            print("Cannot Open File")
            continue  # Skip to the next iteration of the loop

        # Count the subject lines
        count = 0
        for line in fhand:
            if line.startswith('Subject:'):
                count += 1
        print('There were', count, 'subject lines in', fName)

        # Close the file
        fhand.close()

# Call the function
easterEggFunction()