import datetime

given_input = []

start_time = datetime.datetime.now()


def solve():
    horizontal_position = 0
    aim = 0
    depth = 0
    for strings in given_input:
        direction, value = strings.split()
        if direction == "forward":
            horizontal_position += int(value)
            depth += aim * int(value)
        elif direction == "up":
            aim -= int(value)
        elif direction == "down":
            aim += int(value)
    print(depth * horizontal_position)


end_time = datetime.datetime.now()
print(end_time - start_time)

solve()
