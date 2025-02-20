def add_everything_up(a, b):
    try:
        return round(a + b, 3)
    except TypeError:
        if isinstance(a, str) and isinstance(b, (int, float)):
            return a + str(b)
        if isinstance(a, (int, float)) and isinstance(b, str):
            return str(a) + b


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))