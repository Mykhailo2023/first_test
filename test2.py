def format_string(string, length):

    if len(string) >= length:
        return string
    else:
        spaces == " " * ((length - len(string)) // 2)
        formatted_string = spaces + string + spaces
        if len(formatted_string) < length:
            formatted_string = " " + formatted_string
            return formatted_string