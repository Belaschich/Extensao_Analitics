def print_1():
    try:
        x = 10/10
    except Exception as e: #tartamento de exceção
        print(e)


def hellow():
    print('Hello WOrld')


if __name__ == "__main__":
    try:
        x = 1
        print_1()
        if x != 0:
            try:
                print(x)
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)