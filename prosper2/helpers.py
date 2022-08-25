def list_to_string_comma_delimited(list: list[any]):
    """
    Takes a list and returns a string containing the list
    members as their string representations delimited by commas
    Ex: ["a", "b", 1] -> "a, b, 1" 
    """
    return str(list)[1:-1].replace("'", "")