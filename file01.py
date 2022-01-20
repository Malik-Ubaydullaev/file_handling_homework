def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f = open(data)
    stroka = f.read()
    list1 = stroka.split(',')
    return list1
# Read data from file
print(main('data01.txt'))
