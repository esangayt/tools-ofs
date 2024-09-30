def print_boxed_message(message):
    border = f"+{'-' * (len(message)+4)}+"
    print(border)
    print(f"|  {message}  |")
    print(border)


def print_boxed_message_custom(message, border_char='+', padding=2):
    lines = message.split('\n')
    max_length = max(len(line) for line in lines)
    border = f"{border_char}{'-' * (max_length + padding * 2)}{border_char}"

    print(border)
    for line in lines:
        print(f"{border_char}{' ' * padding}{line.ljust(max_length)}{' ' * padding}{border_char}")
    print(border)