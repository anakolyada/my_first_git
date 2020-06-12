def math(self, number):
    numbers = []
    my_list = [a for a in range(0, 100)]
    for number in my_list:
        if number in range(20, 50):
            my_list.append(number)
            return 100