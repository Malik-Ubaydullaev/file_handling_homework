def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    idx = 0
    number_count = 0
    string_count = 0
    while idx < len(data):
        if data[idx].isdigit():
            number_count += 1
        else:
            string_count += 1
        idx += 1
    list2 = [number_count, string_count]
    return list2
        
# Read data from file