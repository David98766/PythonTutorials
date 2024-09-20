def convertNumberToPrice(price):
    decimal_places = 2
    formatted_number = f"{price:.{decimal_places}f}"
    return formatted_number