import logging
import re

def read_file(path: str) -> list[str]:
    with open(path) as f:
        return [line.strip() for line in f.readlines()]

def part_1(lines: list[str]) -> None:
    numbers_in_line = [re.sub("[a-zA-Z]", "", line) for line in lines]
    res = 0
    for n in numbers_in_line:
        if len(n) == 1:
            res += int(n) * 10 + int(n)
        else: 
            res += int(n[0]) * 10 + int(n[-1])

    print(res)

def part_2(lines: list[str]) -> None:
    str_to_digit_mapping = {
        "one":  "1", 
        "two":  "2", 
        "three":"3",
        "four": "4", 
        "five": "5", 
        "six": "6", 
        "seven": "7", 
        "eight": "8", 
        "nine": "9"
    }

    def replacer(line: str) -> str:
        new_str = ""
        for i in range(len(line)):
            if line[i].isnumeric():
                new_str += line[i]
            else:
                for k, v in str_to_digit_mapping.items():
                    if line[i:].find(k) == 0:
                        new_str += v
        return new_str

    only_numbers = list(map(replacer, lines))
    part_1(only_numbers)


def main():
    lines = read_file("./day_1/input.txt")
    # part_1(lines)
    part_2(lines)


if __name__ == "__main__":
    main()
    