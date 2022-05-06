Simple, remove the spaces from the string, then return the resultant string.

Solution

def no_space(x):
    for char in x:
        text = x.replace(" ", "")
        print(text)
    return text
