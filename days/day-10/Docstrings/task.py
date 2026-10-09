def format_name(f_name, l_name):
    """Returns a neat and clean formated name upon given messy first and last name"""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")
print(formatted_name)
length = len(formatted_name)



