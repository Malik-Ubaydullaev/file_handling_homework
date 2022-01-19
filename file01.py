def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f = open(data)
    txt = f.read()
    list1 = txt.split()
    return list1
# Read data from file