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

def solve_iterativ(parkplatz: list, quereAutos: dict, parkplatz_index: int, anzahlNormal: int):
    if parkplatz[parkplatz_index] is None:
        return None, None
    def versuchen(richtung: str):
        array = parkplatz.copy()
        autos_pos = quereAutos.copy()
        ergebnis = {}
        current_pos = parkplatz_index
        while array[current_pos] is not None:
            auto = array[current_pos]
            key_positions = find_key_positions(array, auto)
            next_pos = key_positions["left"] if richtung == "links" else key_positions["right"]
            status = analyze_key_position(array, next_pos)
            if status == "frei":
                delta = -1 if richtung == "links" else 1
                old_indices = [i for i, x in enumerate(array) if x == auto]
                for i in old_indices:
                    array[i] = None
                new_indices = [i + delta for i in old_indices]
                for i in new_indices:
                    array[i] = auto
                ergebnis[auto] = ergebnis.get(auto, 0) + 1
                current_pos = parkplatz_index
            elif status == "Außerhalb des Parkplatzes":
                return 10**6, None
            elif status == "blockiert":
                current_pos = next_pos
        total_moves = sum(ergebnis.values())
        return total_moves, ergebnis
    moves_links, ergebnis_links = versuchen("links")
    moves_rechts, ergebnis_rechts = versuchen("rechts")
    if moves_links <= moves_rechts:
        return ergebnis_links, "links"
    else:
        return ergebnis_rechts, "rechts"

def ausgabe_ergebnisse(parkplatz, quereAutos, anzahlNormal):
    outputs = []
    for i in range(anzahlNormal):
        ergebnis, richtung = solve_iterativ(parkplatz, quereAutos, i, anzahlNormal)
        label = chr(i + 65)
        if ergebnis is None:
            outputs.append(f"{label}:")
        else:
            moves = []
            keys = sorted(ergebnis.keys(), reverse=(richtung == "rechts"))
            for key in keys:
                moves.append(f"{key} {ergebnis[key]} {richtung}")
            outputs.append(f"{label}: " + ", ".join(moves))
    return outputs