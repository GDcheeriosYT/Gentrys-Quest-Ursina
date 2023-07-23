def repeat_string(string: str, amount: int) -> str:
    text = ""
    for i in range(amount):
        text += string

    return text


def int_to_roman(num: int) -> str:
    if not 0 < num < 4000:
        raise ValueError("Input must be an integer between 1 and 3999.")

    roman_numerals = {5: 'V', 4: 'IV', 1: 'I'}

    roman_str = ""
    for value, numeral in roman_numerals.items():
        while num >= value:
            roman_str += numeral
            num -= value

    return roman_str
