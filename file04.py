def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    list1 = data.split(',')
    list2 = []
    idx = 0
    while idx < len(list1):
        if not list1[idx].isdigit():
            list2 += list1[idx]
        idx += 1
    list2 = list(map(str,list2))
    return list2
# Read data from file