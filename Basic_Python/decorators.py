def outer_upper(func):
    def inner_upper(text):
        f=func(text)
        text=f.upper()
        return text
    return inner_upper

@outer_upper
def show(text):
    return text

print(show("araz shah"))