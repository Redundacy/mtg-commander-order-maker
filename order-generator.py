import sys

def main():
    file1 = []
    with open(sys.argv[1]) as file:
        file1 = [line.rstrip() for line in file]
    file2 = []
    with open(sys.argv[2]) as file:
        file2 = [line.rstrip() for line in file]
    output = [x for x in file1 if x not in file2]
    sys.stdout = open("output.txt", 'w')
    for line in output:
        print(line)


if __name__ == '__main__':
    # print(sys.argv)
    main()