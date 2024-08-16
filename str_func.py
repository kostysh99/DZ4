
def capital_letters():
    """принимает на вход строку и возвращает ее со всеми заглавными буквами"""
    print("Введите текст")
    string = input()
    string_up = str.upper(string)
    return string_up


print(capital_letters())
