import datetime

given_input = []
start_time = datetime.datetime.now()


def solve():
    count = 0
    for index, element in enumerate(given_input):
        if element > given_input[index - 1]:
            count += 1
    print(count)


def solve_pythonic():
    count = 0
    print(sum(
        [count + 1 if element > given_input[index - 1]
         else count + 0 for index, element in enumerate(given_input)]))


end_time = datetime.datetime.now()
print("μs: " + str((end_time - start_time).microseconds))

if __name__ == '__main__':
    solve()
