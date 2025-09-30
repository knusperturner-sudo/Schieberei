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

def find_key_positions(parkplatz: list, auto: str) -> dict:
    indices = [i for i, x in enumerate(parkplatz) if x == auto]
    if not indices:
        return {"left": None, "right": None}
    left_pos = min(indices) - 1
    right_pos = max(indices) + 1
    if left_pos < 0:
        left_pos = None
    if right_pos >= len(parkplatz):
        right_pos = None
    return {"left": left_pos, "right": right_pos}

def analyze_key_position(parkplatz: list, pos: int) -> str:
    if pos is None:
        return "Außerhalb des Parkplatzes"
    if pos < 0 or pos >= len(parkplatz):
        return "Außerhalb des Parkplatzes"
    if parkplatz[pos] is None:
        return "frei"
    return "blockiert"