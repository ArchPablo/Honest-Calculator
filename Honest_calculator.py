MSG_ = [
    "Enter an equation",
    "Do you even know what numbers are? Stay focused!",
    "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
    "Yeah... division by zero. Smart move...",
    "Do you want to store the result? (y / n):\n",
    "Do you want to continue calculations? (y / n):\n",
    " ... lazy",
    " ... very lazy",
    " ... very, very lazy",
    "You are",
    "Are you sure? It is only one digit! (y / n)\n",
    "Don't be silly! It's just one number! Add to the memory? (y / n)\n",
    "Last chance! Do you really want to embarrass yourself? (y / n)\n"
]


def is_one_digit(v):
    if -10 < v < 10 and v.is_integer():
        return True
    else:
        return False


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += MSG_[6]
    if v1 == 1 or v2 == 1:
        msg += MSG_[7]
    if (v1 == 0 or v2 == 0) and v3 != "/":
        msg += MSG_[8]
    if msg != "":
        msg = MSG_[9] + msg
        print(msg)


operations = {
    "+": (lambda x, y: x + y),
    "-": (lambda x, y: x - y),
    "*": (lambda x, y: x * y),
    "/": (lambda x, y: x / y),
}

memory = 0

while True:
    print(MSG_[0])
    x, oper, y = input().split()
    try:
        x = memory if x == "M" else float(x)
        y = memory if y == "M" else float(y)
        check(x, y, oper)
        result = operations[oper](x, y)
        print(result)
        if input(MSG_[4]) == "y":
            if not is_one_digit(result):
                memory = result
            else:
                msg_index = 10
                while msg_index < 13:
                    answer = input(MSG_[msg_index])
                    if answer == 'y':
                        if msg_index < 13:
                            msg_index += 1
                            if msg_index == 12:
                                memory = result
                    elif answer == 'n':
                        break

        if input(MSG_[5]) == "n":
            break

    except ValueError:
        print(MSG_[1])
    except KeyError:
        print(MSG_[2])
    except ZeroDivisionError:
        print(MSG_[3])

