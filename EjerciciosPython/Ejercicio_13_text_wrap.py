import textwrap
#Create function with string, and max_with as parameterd.
def wrap(string, max_width):
    #Wraps the single paragraph in text (a string) so every line is at most width characters long
    #In this case the out string is 4 characters long.
    return '\n'.join(textwrap.wrap(string, max_width))
