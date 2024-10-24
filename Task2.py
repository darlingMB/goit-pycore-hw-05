import re


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."





def generator_numbers(text):
    pattern = r'\b-?\d+\.?\d*\b'
    numbers = re.findall(pattern, text)

    for num in numbers:
        yield float(num)


def sum_profit(text, func):
    
    return sum(func(text))



def main():
    res = sum_profit(text=text, func=generator_numbers)
    print(res)

if __name__ == '__main__':
    main()