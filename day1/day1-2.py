import datetime

given_input = []
start_time = datetime.datetime.now()


def solve():
    count, previous_sum = 0, 0
    for index, element in enumerate(given_input[:-2]):
        current_sum = element + given_input[index + 1] + given_input[index + 2]
        if current_sum > previous_sum != 0:
            count += 1
        previous_sum = current_sum

    print(count)


end_time = datetime.datetime.now()
print("μs: " + str((end_time - start_time).microseconds))

if __name__ == '__main__':
    solve()
