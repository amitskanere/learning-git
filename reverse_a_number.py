def revers_number(num):
    result = 0
    while int(num / 10):
        last_digit = num % 10
        result = result * 10 + last_digit
        num = int(num / 10)

    result = result * 10 + num

    return result

print(revers_number(123))