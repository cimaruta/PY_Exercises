def get_formatted_name(first_name, last_name, middle_name=""):
    """Takes first and last name and formats it"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('aaron', 'johnson',)
print(musician)