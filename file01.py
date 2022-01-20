def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    stroka = data.read()
    list1 = stroka.split()
    return list1
# Read data from file
f = open('data01.txt')
#txt = f.read()
print(main(f))
