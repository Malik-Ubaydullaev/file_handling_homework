def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    idx = 0
    Summa = 0
    while idx < len(data):
        if data[idx].isdigit():
            Summa += int(data[idx])
        idx += 1
    return Summa
# Read data from file