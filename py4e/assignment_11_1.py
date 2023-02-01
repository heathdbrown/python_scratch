import re


def lines_of_file(file: str) -> str:
    with open(file, "r") as f:
        lines = f.read()
    return lines


def sum_numbers_from_lines(lines: str) -> int:
    integers_from_file = re.findall("[0-9]+", lines)
    return sum([int(integer) for integer in integers_from_file])


file = input("Enter file name: ")
print(sum_numbers_from_lines(lines_of_file(file)))
