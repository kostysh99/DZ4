print("Введите текст")
line = input()
def capital_letters():
    """ принимает на вход строку и возвращает ее со всеми заглавными буквами"""
    string_up = str.upper(line)
    return string_up

def first_capital():
    """делает заглавными первые буквы каждого слова в строке, поступившей на вход функции"""
    first_up = str.capitalize(line)
    return first_up


print(capital_letters())
print (first_capital())