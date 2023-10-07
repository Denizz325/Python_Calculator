def main(a, b, some_command):
    if some_command == 1:
        return add_function(a, b)
    elif some_command == 2:
        return subtract_function(a,b)
    elif some_command == 3:
        return multiplication_function(a,b)
    elif some_command == 4:
        return division_function(a, b)


def add_function(a, b: float) -> float:
    return a + b


def subtract_function(a, b: float) -> float:
    return a - b


def multiplication_function(a, b: float) -> float:
    return a * b


def division_function(a, b: float) -> float:
    return a / b


while True:
    print("Menu:")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Quit")
    command = int(input("Enter your choice (1/2/3/4/5):"))
    if command == 5:
            break
    first_number = float(input("Enter the first number:"))
    second_number = float(input("Enter the second number:"))
    print(f"Result: {round(main(first_number, second_number, command))}")


print("Goodbye!")






