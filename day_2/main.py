from dataclasses import dataclass


MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

def read_file(path: str) -> list[str]:
    with open(path) as f:
        return [line.strip() for line in f.readlines()]
    

@dataclass
class Cube:
    color: str
    n: int

def part_2(lines: list[str]) -> list[list[Cube]]:
    res = []
    for game in lines:
        # print(game)
        header, sets = game.split(": ")
        game_id = int(header.split(" ")[1])
        single_set = sets.split("; ")
        cubes_in_set = [s.split(", ") for s in single_set]
        for i in range(len(cubes_in_set)):
            for j in range(len(cubes_in_set[i])):
                n, color = cubes_in_set[i][j].split(" ")
                cubes_in_set[i][j] = Cube(color=color, n=int(n))

        flat = [c for s in cubes_in_set for c in s]
        maxes = {
            "red": -1,
            "green": -1,
            "blue": -1
        }
        for item in flat:
            if maxes[item.color] < item.n or maxes[item.color] == -1:
                maxes[item.color] = item.n

        power = maxes["red"] * maxes["green"] * maxes["blue"]
        res.append(power)

    print(sum(res))

def part_1(lines: list[str]) -> None:
    res = []
    for game in lines:
        # print(game)
        header, sets = game.split(": ")
        game_id = int(header.split(" ")[1])
        single_set = sets.split("; ")
        cubes_in_set = [s.split(", ") for s in single_set]
        for i in range(len(cubes_in_set)):
            for j in range(len(cubes_in_set[i])):
                n, color = cubes_in_set[i][j].split(" ")
                cubes_in_set[i][j] = Cube(color=color, n=int(n))
        
        print(cubes_in_set)
        flag = True
        for se in cubes_in_set:
            sum_red = sum([c.n for c in se if c.color == "red"])
            sum_green = sum([c.n for c in se if c.color == "green"])
            sum_blue = sum([c.n for c in se if c.color == "blue"])
            if not(sum_red <= MAX_RED and sum_green <= MAX_GREEN and sum_blue <= MAX_BLUE):
                flag = False

        if flag:
            res.append(game_id)
    
    print(sum(res))


def main():
    lines = read_file("./day_2/input.txt")
    # part_1(lines)
    part_2(lines)


if __name__ == "__main__":
    main()
    
