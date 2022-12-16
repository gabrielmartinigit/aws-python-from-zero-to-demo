def soma(n1, n2):
    return n1+n2


def main():
    n1 = input("Número 1: ")
    n2 = input("Número 2: ")

    n3 = soma(n1, n2)

    print(f'Soma: {n3}')


if __name__ == '__main__':
    main()
