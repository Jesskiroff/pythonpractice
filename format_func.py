def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    print (f"{formatted_f_name} {formatted_l_name}")
format_name(f_name= "geOrge", l_name="BUSH")


def function_1(text):
    return text + text

def function_2(text):
    return text.title()

output_1 = function_2(function_1("hello"))
output_2 = function_1(function_2("hello"))
print(output_1)
print(output_2)