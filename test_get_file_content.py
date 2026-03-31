from functions.get_file_content import get_file_content


def test():
    result = get_file_content("calculator", "lorem.txt")
    print(len(result))
    print(result[-50:])  # print the last 50 characters

    result = get_file_content("calculator", "main.py")
    print(len(result))
    print(result)  

    result = get_file_content("calculator", "pkg/calculator.py")
    print(len(result))
    print(result)  

    result = get_file_content("calculator", "/bin/cat")
    print(len(result))
    print(result)  

    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print(len(result))
    print(result)  

if __name__ == "__main__":
    test()
