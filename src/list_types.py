def types_count(array: list, type_in_array: type):
    result = []
    for element in array:
        if isinstance(element, type_in_array):
            result.append(element)
    return len(result)