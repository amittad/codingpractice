def even(num):
    for numa in num:
        if numa % 2 ==0:
            print(f"{numa} is even")
        else:
            print(f"{numa} is odd")


number: list[int] = [ 11,22,24,56,87,54,32,97,34]

even(number)