def format_name(f_name, l_name):
    """ Take first name and last name and format it to return the title
    case version of the name.
    """
    if f_name == "" or l_name == "":
        return "You did not provided valid inputs"
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

print(format_name(input('Enter your First Name: '), input("Enter your Last Name: ")))
