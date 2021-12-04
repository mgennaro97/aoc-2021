import datetime
import numpy as np

given_input = []
bingo_boards = []

start_time = datetime.datetime.now()


def solve():
    bingo_reshaped = []
    for board in bingo_boards:
        bb = np.array(board)
        reshaped = bb.reshape(5, 5)
        bingo_reshaped.append(reshaped)

    for num in given_input:
        for reshaped in bingo_reshaped:
            result = np.where(reshaped == num)
            if len(result[0]) > 0 and len(result[1]) > 0:
                reshaped[int(result[0])][int(result[1])] = -1
            else:
                pass
            if any(np.equal(reshaped, [-1, -1, -1, -1, -1]).all(1)) \
                    or any(np.equal(reshaped, [-1, -1, -1, -1, -1]).all(0)):
                print(sum(reshaped[reshaped != -1]) * num)
                return


end_time = datetime.datetime.now()
print("μs: " + str((end_time - start_time).microseconds))

if __name__ == '__main__':
    solve()
