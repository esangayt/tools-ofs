def print_boxed_message(message):
    border = f"+{'-' * (len(message)+4)}+"
    print(border)
    print(f"|  {message}  |")
    print(border)
