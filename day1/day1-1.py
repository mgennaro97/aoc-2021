import datetime

given_input = []
start_time = datetime.datetime.now()


def solve():
    count = 0
    for index, element in enumerate(given_input):
        if element > given_input[index - 1]:
            count += 1
    print(count)


end_time = datetime.datetime.now()
print(end_time - start_time)

solve()
