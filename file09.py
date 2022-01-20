def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    idx = 0
    Minimum = 0
    while idx < len(data):
        if data[idx].isdigit():
            if int(data[idx]) < Minimum:
                Minimum = int(data[idx])
        idx += 1
    
    return Minimum

# Read data from file