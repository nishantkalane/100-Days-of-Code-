






traffic_light=input("What colour is seen in traiffic light: red, green or yellow?").strip().lower()
def what_to_do(traffic_light):
    if traffic_light != "green" and traffic_light != "red" and traffic_light != "yellow":
        return "undefined_input"
    if traffic_light == "green":
        return "drive"
    elif traffic_light =="red":
        return "stop"
    else:
        return "start the vehicle"
print(what_to_do(traffic_light))







# def format_name(f_name, l_name):
#     if f_name=="" or l_name=="":
#         return "You gave invalid inputs"
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"
#
#
# output = (format_name(input("What is your first name ? : "),input("What is your last name ? :")))
# print(output)