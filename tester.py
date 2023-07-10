import requests

def pusher(id, n):
    response = requests.post(f"http://localhost:8000/calc/{id}/push/{n}")
    if response.status_code == 200:
        value = response.json()
        print(f'Sucessfully pushed number on to stack {value}')
    else:
        print(f"Error: {response.text}")

def popper(id):
    response = requests.post(f'http://localhost:8000/calc/{id}/pop')

    if response.status_code == 200:
        value = response.json()
        print(f'Succesfully deleted last value {value}')
    else:
        print(f"Error: {response.text}")

def peeker(id):
    response = requests.get(f"http://localhost:8000/calc/{id}/peek")

    if response.status_code == 200:
        value = response.json()
        print(f"Top value on stack: {value}")
    else:
        print(f"Error: {response.text}")

def adder(id):
    response = requests.post(f"http://localhost:8000/calc/{id}/add")

    if response.status_code == 200:
        value = response.json()
        print(f"Result: {value}")
    else:
        print(f"Error: {response.text}")

def subtracter(id):
    response = requests.post(f"http://localhost:8000/calc/{id}/subtract")

    if response.status_code == 200:
        value = response.json()
        print(f"Result: {value}")
    else:
        print(f"Error: {response.text}")

def multiplier(id):
    response = requests.post(f"http://localhost:8000/calc/{id}/multiply")

    if response.status_code == 200:
        value = response.json()
        print(f"Result: {value}")
    else:
        print(f"Error: {response.text}")

def divider(id):
    response = requests.post(f"http://localhost:8000/calc/{id}/divide")

    if response.status_code == 200:
        value = response.json()
        print(f"Result: {value}")
    else:
        print(f"Error: {response.text}")


def menu():
    while True:
        expression = input('''Select 1 for Pusher
Select 2 for Popper
Select 3 for Peeker
Select 4 for Adder
Select 5 for Subtracter
Select 6 for Multiplier
Select 7 for Divider
Select q to quit
''')
        if expression == '1':
            exp = input('Please supply id and number like this: examplestack1 5 ')
            if exp == 'b':
                continue
            split = exp.split(' ')
            cnv1 = str(split[0])
            cnv2 = int(split[1])
            pusher(cnv1, cnv2)
        elif expression == '2':
            exp2 = input('Please supply id: ')
            if exp2 == 'b':
                continue
            cnv1 = str(exp2)
            popper(cnv1)
        elif expression == '3':
            exp3 = input('Please supply id: ')
            if exp3 == 'b':
                continue
            cnv1 = str(exp3)
            peeker(cnv1)
        elif expression == '4':
            exp4 = input('Please supply id: ')
            if exp4 == 'b':
                continue
            cnv1 = str(exp4)
            adder(cnv1)
        elif expression == '5':
            exp5 = input('Please supply id: ')
            if exp5 == 'b':
                continue
            cnv1 = str(exp5)
            subtracter(cnv1)
        elif expression == '6':
            exp6 = input('Please supply id: ')
            if exp6 == 'b':
                continue
            cnv1 = str(exp6)
            multiplier(cnv1)
        elif expression == '7':
            exp7 = input('Please supply id: ')
            if exp7 == 'b':
                continue
            cnv1 = str(exp7)
            divider(cnv1)
        elif expression == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

menu()
