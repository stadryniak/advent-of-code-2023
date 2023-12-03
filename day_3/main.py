
import re


def read_file(path: str) -> list[str]:
    with open(path) as f:
        return [line.strip() for line in f.readlines()]
    

def part_1(lines: list[str]):
    res = []
    for i in range(len(lines)):
        current = lines[i]
        numbers_in_line = re.findall(r'\d+', current)
        numbers_in_line.sort()
        prev = ""
        offset = 0
        for num in numbers_in_line:
            if prev != num:
                offset = 0
            for (pattern, extra_len) in {
                (f"[^a-zA-Z0-9]{num}[^a-zA-Z0-9]", 1), 
                (f"^{num}[^a-zA-Z0-9]", 0), 
                (f"[^a-zA-Z0-9]{num}$", 1)
                }:
                match = re.search(pattern, current[offset:])
                if match:
                    original_start_idx = match.start() + extra_len
                    break
            start_idx = original_start_idx + offset
                
            offset = start_idx + len(num)
            prev = num
            flag = True
            for c_idx in range(start_idx, start_idx + len(num)):
                moves = {-1, 0, 1}
                for dx in moves:
                    for dy in moves:
                        try:
                            considered_point = lines[i+dx][c_idx+dy]
                            if flag and not considered_point.isdigit() and considered_point != ".":
                                res.append(int(num))
                                flag = False
                        except IndexError:
                            pass
    print(sum(res))
    res = [str(r) for r in res]
    res.sort()
    print("\n".join(res))

def main():
    lines = read_file("./day_3/input.txt")

    part_1(lines)

if __name__ == '__main__':
    main()
