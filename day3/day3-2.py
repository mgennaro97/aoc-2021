import datetime
import collections

given_input = []

start_time = datetime.datetime.now()


def solve():
    oxygen_generator_given_input = co2_scrubber_given_input = given_input
    bit_length = len(given_input[0])

    og = solve_oxygen_generator_rating(bit_length,
                                       oxygen_generator_given_input)
    csg = solve_co2_scrubber_rating(bit_length,
                                    co2_scrubber_given_input)

    print(int(og, 2) * int(csg, 2))


def solve_oxygen_generator_rating(bit_length, oxygen_generator_given_input):
    for b in range(bit_length):
        sub_list = [i[b] for i in oxygen_generator_given_input]
        if collections.Counter(sub_list).get('0') == \
                collections.Counter(sub_list).get('1'):
            most_common = '1'
        else:
            most_common = \
                max(sub_list[::-1], key=collections.Counter(sub_list).get)
        if len(oxygen_generator_given_input) == 1:
            break
        else:
            filtered_list = \
                [element for element in oxygen_generator_given_input
                 if element[b] == most_common]
            oxygen_generator_given_input = filtered_list
    return ''.join(oxygen_generator_given_input)


def solve_co2_scrubber_rating(bit_length, co2_scrubber_given_input):
    for b in range(bit_length):
        sub_list = [i[b] for i in co2_scrubber_given_input]
        if collections.Counter(sub_list).get('0') == \
                collections.Counter(sub_list).get('1'):
            most_uncommon = '0'
        else:
            most_uncommon = \
                min(sub_list[::-1], key=collections.Counter(sub_list).get)
        if len(co2_scrubber_given_input) == 1:
            break
        else:
            filtered_list = \
                [element for element in co2_scrubber_given_input
                 if element[b] == most_uncommon]
            co2_scrubber_given_input = filtered_list
    return ''.join(co2_scrubber_given_input)


end_time = datetime.datetime.now()
print("μs: " + str((end_time - start_time).microseconds))

if __name__ == '__main__':
    solve()
