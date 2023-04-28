Users = {}

# Функція-декоратор для обробки виключень від користувача


def input_error(func):
    def wrapper(*args):
        try:
            result = func(*args)
            return result
        except KeyError:
            return "Contact not found"
        except ValueError:
            return "Please provide a name and phone number"
        except IndexError:
            return "Please provide a name"
    return wrapper

# Функція для відображення привітання


def hello(_):
    return "How can I help you?"


def unknown_command(_):
    return "Invalid command. Please try again."


def exit(_):
    return


# Функція для додавання нового контакту


@input_error
def add(args):
    name, phone = args
    Users[name] = phone
    return f"{name} has been added to your contacts"

# Функція для зміни номера телефону існуючого контакту


@input_error
def change(args):
    name, phone = args
    old_phone = Users[name]
    Users[name] = phone
    return f"{name}'s phone number has been updated"

# Функція для відображення номера телефону для зазначеного контакту


@input_error
def phone(args):
    name = args[0]
    if name not in Users:
        return "Contact not found"
    return f"{name}'s phone number is {Users[name]}"

# Функція для відображення всіх збережених контактів


def show_all(_):
    result = "Your contacts:\n"
    for name, phone in Users.items():
        result += f"{name}: {phone}\n"
    return result


HANDLERS = {
    'hello': hello,
    'add': add,
    'change': change,
    'show all': show_all,
    'exit': exit,
    'good bye': exit,
    'close': exit,
    'phone': phone
}


def parse_input(user_input):
    command, *args = user_input.split()
    command = command.lstrip()

    try:
        handler = HANDLERS[command.lower()]
    except KeyError:
        if args:
            command = command + ' ' + args[0]
            args = args[1:]
        handler = HANDLERS.get(command.lower(), unknown_command)
    if command.lower() == "change" and len(args) == 2:
        args = [args[0], args[1]]
    return handler, args

# Головна функція, що виконується у безкінечному циклі та чекає команди користувача


def main():
    print("Welcome to the contacts bot!")
    while True:
        user_input = input('Please enter command and args: ')
        handler, args = parse_input(user_input)
        result = handler(args)
        if not result:
            print('Exit')
            break
        print(result)


# Запуск головної функції
if __name__ == "__main__":
    main()
