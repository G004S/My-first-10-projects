def calculator():
    num_1 = input ("Enter first number: ")
    num_2 = input ("Enter second number: ")

    operation = input ("Enter operation (+, -, *, /): ")
    if operation == '+':
        result = float(num_1) + float(num_2)
    elif operation == '-':
        result = float(num_1) - float(num_2)   
    elif operation == '*':
        result = float(num_1) * float(num_2)
    elif operation == '/':
        if float(num_2) != 0:
            result = float(num_1) / float(num_2)
        else:
            result = "Error: Division by zero is not allowed."
    else:
        result = "Error: Invalid operation."
    print("Result:", result)
    with open("result.txt", "w") as file:
        file.write(str(result))
    return result
calculator(12, 8, '+')