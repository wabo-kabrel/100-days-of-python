# Docstrings are used to create little pieces of documentation which describe what a function does.

# Format
# A docstring is created by writing a comment at the first line after the function declaration,
# describing what the function does. The comment must be in triple quotation marks ("""""").

# Example

def format_name(f_name, l_name):
    """Take a first and last name and format it to return the title case
    version of the name."""
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

formatted_name = format_name("Trevor", "Philips")