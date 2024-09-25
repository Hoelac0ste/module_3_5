def get_multiplied_digits(number):
    str_number = str(number)
    
    if len(str_number) == 1:
        return number
    else:
        a = len(str_number)
        b = str_number[a - 1]
        if int(b) == 0:
            str_number = str_number[0:a - 1]
        else:
            str_number = str_number
            
        first = int(str_number[0])
        return first * get_multiplied_digits(int(str_number[1:]))

print(get_multiplied_digits(42050))