def validate_number(number, base):
    valid_characters = '0123456789ABCDEF'[:base]
    return all(digit.upper() in valid_characters for digit in number)

def decimal_to_base(decimal_number, base):
    digits = "0123456789ABCDEF"
    converted_number = ""
    
    if decimal_number == 0:
        return "0"

    while decimal_number > 0:
        remainder = decimal_number % base
        converted_number = digits[remainder] + converted_number
        decimal_number = decimal_number // base

    return converted_number

def base_to_decimal(number, base):
    digits = "0123456789ABCDEF"
    decimal_number = 0
    power = len(number) - 1

    for digit in number:
        decimal_number += digits.index(digit.upper()) * (base ** power)
        power -= 1

    return decimal_number

def main():
    print("Bem-vindo ao conversor de bases numéricas!")
    from_base = int(input("Digite a base de entrada (2 a 16): "))
    to_base = int(input("Digite a base de saída (2 a 16): "))

    if from_base < 2 or from_base > 16 or to_base < 2 or to_base > 16:
        print("Bases inválidas. As bases devem estar entre 2 e 16.")
        return

    number = input(f"Digite o número na base {from_base}: ")

    if not validate_number(number, from_base):
        print("Número inválido para a base informada.")
        return

    decimal_number = base_to_decimal(number, from_base)
    converted_number = decimal_to_base(decimal_number, to_base)
    print(f"O número {number} na base {from_base} é equivalente a {converted_number} na base {to_base}.")

if __name__ == "__main__":
    main()
