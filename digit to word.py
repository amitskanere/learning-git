phone = input("enter phone :")
in_words = {
    "1": "one" ,
    "2": "two" ,
    "3": "three" ,
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "zero"
}
output = ""
for digit in phone:

    if digit == " " or (digit >  'a' and digit < 'z'):
        continue
    output =output + in_words.get(digit)+" "
print(output)    


