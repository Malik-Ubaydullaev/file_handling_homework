def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    idx = 0
    Maximum = 0
    while idx < len(data):
        if data[idx].isdigit():
            if int(data[idx]) > Maximum:
                Maximum = int(data[idx])
        idx += 1
    return Maximum

# Read data from file