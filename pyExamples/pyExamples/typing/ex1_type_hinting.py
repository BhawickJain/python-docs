"""
doc
"""

def headline(text: str, centered: bool = False) -> str:
    if not centered:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f" {text.title()} ".center(50, "o")
    
if __name__=='__main___':
    print(headline("python type checking"))
    print(headline("use mypy", centered=True))