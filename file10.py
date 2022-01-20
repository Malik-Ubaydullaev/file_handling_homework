def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    list1 = data.split()
    idx = 0
    Maximum = 0
    while idx < len(list1):
        if Maximum < len(list1[idx]):
            Maximum = len(list1[idx])
        idx += 1
        
    return 15
        

# Read data from file