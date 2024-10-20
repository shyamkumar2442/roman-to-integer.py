def roman_to_integer(s):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0

    for char in s:
        value = roman_dict[char]
        if value > prev_value:
            total += value - 2 * prev_value  # Adjust for the previous subtraction
        else:
            total += value
        prev_value = value

    return total

s = input("Enter a Roman numeral: ")
print(roman_to_integer(s))
