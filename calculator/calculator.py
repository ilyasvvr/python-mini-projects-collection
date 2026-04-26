print('hello to my calculator')

while True:

    number1 = int(input('\nChoose number> '))
    print("Choose number of the operation \n 1__+ \n 2__- \n 3__* \n 4__/ ")
    operation = int(input('Choose operation: '))
    number2 = int(input('Choose another number> '))

    if operation == 1:
        print("Result: ", number1 + number2)
    elif operation == 2:
        print("Result: ", number1 - number2)
    elif operation == 3:
        print("Result: ", number1 * number2)
    elif operation == 4:
        if number2 != 0:
            print("Result: ", number1 / number2)
        else:
            print("Error: Division by zero!")
    else:
        print('the number of the operation does not exist')


    recalculate = input("\nDo you want to recalculate? (Y/N): ").upper()
    if recalculate != 'Y':
        print("Goodbye!")
        break
