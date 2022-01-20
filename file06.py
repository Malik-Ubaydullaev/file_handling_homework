def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    list1 = data.split()
    list2 = []
    idx = 0
    while idx < len(list1):
        print(list1[idx])
        list2.append(len(list1[idx]))
        #list1.pop()
        idx += 1
    
    return list2
    
# Read data from file