def headline(text, centered = False):
    #type: (str, bool) -> str
    if not centered:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f" {text.title()} ".center(50, "o")

def headline2(
    text,
    width=80,
    fill_char='-',
):
    return f" {text.title()} ".center(width, fill_char)

if __name__=='__main__':
    print(headline2("these type comments also work", width=70))
    print(headline("python type checking"))
    print(headline("use mypy", centered=True))

    pi = 3.142 # type: float

    try:
        print(headline(pi))  # will throw an error
    except Exception as err:
        print(f'error! {err}')