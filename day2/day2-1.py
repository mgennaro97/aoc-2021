import datetime

given_input = []

start_time = datetime.datetime.now()


def solve():
    horizontal_position, depth = 0, 0
    for strings in given_input:
        direction, value = strings.split()
        if direction == "forward":
            horizontal_position += int(value)
        elif direction == "up":
            depth -= int(value)
        elif direction == "down":
            depth += int(value)
        else:
            print("Invalid direction")
    print(depth * horizontal_position)


end_time = datetime.datetime.now()
print("μs: " + str((end_time - start_time).microseconds))

if __name__ == '__main__':
    solve()
