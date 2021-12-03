import datetime
import collections

given_input = []

start_time = datetime.datetime.now()


def solve():
    most_common = most_uncommon = ""
    for b in range(len(given_input[0])):
        sub_list = [i[b] for i in given_input]
        most_common += max(sub_list[::-1],
                           key=collections.Counter(sub_list).get)
        most_uncommon += min(sub_list[::-1],
                             key=collections.Counter(sub_list).get)
    print(int(most_common, 2) * int(most_uncommon, 2))


end_time = datetime.datetime.now()
print("μs: " + str((end_time - start_time).microseconds))

if __name__ == '__main__':
    solve()
