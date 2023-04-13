import sys


def main():
    transition = [[[0, 1], [0]], [[4], [2]], [[4], [3]], [[4], [4]]]
    input = "enter the string: "
    input = list(input)
    for index in range(len(input)):
        if input[index] == "a":
            input[index] = "0"
        else:
            input[index] = "1"

    final = "3"
    i = 0

    print("rejected")


def trans(transition, input, final, state, i):
    for j in range(len(input)):
        for each in transition[state][int(input[j])]:
            if each < 4:
                state = each
                if j == len(input) - 1 and (str(state) in final):
                    print("accepted")
                    sys.exit()
                trans(transition, input[i + 1 :], final, state, i)
        i = i + 1


main()
