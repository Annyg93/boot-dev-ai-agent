from functions.run_python_file import run_python_file


def test() -> None:
    # Should print calculators usage instructions
    result = run_python_file("calculator", "main.py") 
    print(result)

    # Should run the calculator
    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print(result)

    # Should run the calculators tests successfully
    result = run_python_file("calculator", "tests.py")
    print(result)

    # Should return error
    result = run_python_file("calculator", "../main.py")
    print(result)

    # Should return error
    result = run_python_file("calculator", "nonexistent.py")
    print(result)
    
    # Should return error
    result = run_python_file("calculator", "lorem.txt")
    print(result)


if __name__ == "__main__":
    test()    