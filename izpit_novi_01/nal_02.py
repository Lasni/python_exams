f1 = input(r"Enter file path 1")
f2 = input(r"Enter file path 2")

lines1 = [line.rstrip("\n") for line in open(f1)]
lines2 = [line.rstrip("\n") for line in open(f2)]

n1 = len(lines1)
n2 = len(lines2)


def compare_contents():
    same_contents = True
    line_count = 1
    character_count = 1
    for line in range(n1):
        if lines1[line] != lines2[line]:
            same_contents = False
            for char in range(len(lines1[line])):
                if lines1[line][char] != lines2[line][char]:
                    break
                else:
                    character_count += 1
            print("Line from file1: '{}'".format(lines1[line]))
            print("Line from file2: '{}'".format(lines2[line]))
            break
        else:
            line_count += 1
    if same_contents:
        print("The two files are the same")
    else:
        print("The two files differ at line {} in character at position {}".format(line_count, character_count))


compare_contents()
