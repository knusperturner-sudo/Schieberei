def read_in_parkplatz(dateipfad):
    with open(dateipfad, 'r') as f:
        return [zeile.strip() for zeile in f]


def read_first_line(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        line = f.readline().strip()
        tokens = line.split()
        return tokens[1]


def char_to_num(char: str) -> int:
    char = char.upper()
    return ord(char) - ord("A") + 1

def read_rest(path: str) -> list[str]:
    with open(path, "r", encoding="utf-8") as f:
        f.readline()
        f.readline()
        rest = [line.strip() for line in f]
        return rest

def parkplatz_fuellen(array: list, lines: list[str]) -> list:
    for line in lines:
        auto, platz = line.split()
        index = int(platz)
        if 0 <= index < len(array):
            array[index] = auto
        if 0 <= index + 1 < len(array):
            array[index + 1] = auto
    return array

