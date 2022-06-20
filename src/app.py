import sys
import os


def prime(s):
    # your code goes here
    flag=False
    if s>1:
        for i in range(2, s):
            if (s % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break
    if flag == True:
        print("number is not prime")
    else:
        print("number is prime")
def solution(s):
    return prime(s)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(os.error("Argument required"))

    print(solution(sys.argv[1]))
