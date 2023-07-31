def main():
    numerals = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    decimals = [1000, 500, 100, 50, 10, 5, 1]
    count = 0
    result = ''

    number = int(input('Dezimalzahl > '))
    while number > 0:
        if (number >= decimals[count]):
            result += numerals[count]
            number = number - decimals[count]
        else:
            count = count + 1
    print(result)
    return numerals, decimals


if __name__ == '__main__':
    main()
