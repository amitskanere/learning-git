def lbs_to_kg(weight):
    return weight*0.45

def kg_to_lbs(weight):
    return weight/0.45


def largest_number():
    numbers = [2, 4, 1, 7, 10, 9, 11]
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number

    return print(max)
