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