def extractValueFromLines():

    fName = input("Enter File Name: ")

    try:
         fhand = open(fName)
    except:
        print('File cannot be opened:', fName)
        quit()


    count = 0
    total = 0.0

    for line in fhand:
        # strip removes whitespace before and after text
        line = line.strip()
        # Look for lines that start with "X-DSPAM-Confidence:"
        if line.startswith("X-DSPAM-Confidence:"):
            # Split the line at the colon to extract the number
            parts = line.split(":")
            # Extract the floating point number and convert to float. 1 because it is the second part of the line
            # (it has been split)
            confidence_value = float(parts[1].strip())
            # Update the total and count
            total += confidence_value
            count += 1

    # Compute the average if any lines were found
    if count > 0:
        average_spam_confidence = total / count
        print(f"Average spam confidence: {average_spam_confidence}")
    else:
        print("No 'X-DSPAM-Confidence:' lines found.")


extractValueFromLines()