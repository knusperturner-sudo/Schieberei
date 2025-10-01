import pytest
from src.schiebeparkplatz import read_in_parkplatz
from src.schiebeparkplatz import read_first_line
from src.schiebeparkplatz import char_to_num
from src.schiebeparkplatz import read_rest
from src.schiebeparkplatz import parkplatz_fuellen
from src.schiebeparkplatz import find_key_positions
from src.schiebeparkplatz import analyze_key_position
from src.schiebeparkplatz import solve_iterativ
from src.schiebeparkplatz import ausgabe_ergebnisse
from src.schiebeparkplatz import fill_quere_autos_dict
from src.schiebeparkplatz import main


def test_read_in_parkplatz():
    result = (read_in_parkplatz("/Users/knusper_desktop/Desktop/Schieberei/parkplätze/parkplatz0.txt"))

    assert result[0] == [None, None, "H", "H", None, "I", "I"]
    assert result[1] == {"H": 2, "I": 5}
    assert result[2] == 7




def test_read_in_first_line(tmp_path):

    test_file = tmp_path / "test.txt"
    test_file.write_text("foo bar baz\nzweite zeile\n")

    result = read_first_line(str(test_file))

    assert result == "bar"

def test_char_to_num():
    assert char_to_num("A") == 1
    assert char_to_num("B") == 2
    assert char_to_num("Z") == 26
    assert char_to_num("a") == 1  # Teste auch Kleinbuchstaben

def test_read_rest(tmp_path):
    test_file = tmp_path / "test.txt"
    test_file.write_text("erste Zeile\nzweite Zeile\ndritte Zeile\nvierte Zeile\n")
    result = read_rest(str(test_file))
    assert result == ["dritte Zeile", "vierte Zeile"]

def test_parkplatz_fuellen():
    array = [None, None, None, None]
    lines = ["A 0", "B 2"]
    result = parkplatz_fuellen(array, lines)

    assert result == ["A", "A", "B", "B"]

    array = [None, None, None, None, None, None, None]
    lines = ["H 2", "I 5"]

    result = parkplatz_fuellen(array, lines)

    assert result == [None, None, "H", "H", None, "I", "I"]

def test_find_key_positions():
    parkplatz = ["A", "B", "B", "C", "D"]
    assert find_key_positions(parkplatz, "B") == {"left": 0, "right": 3}
    assert find_key_positions(parkplatz, "A") == {"left": None, "right": 1}
    assert find_key_positions(parkplatz, "D") == {"left": 3, "right": None}
    assert find_key_positions(parkplatz, "X") == {"left": None, "right": None}

def test_analyze_key_position():
    parkplatz = ["A", None, "B", None]
    assert analyze_key_position(parkplatz, None) == "Außerhalb des Parkplatzes"
    assert analyze_key_position(parkplatz, -1) == "Außerhalb des Parkplatzes"
    assert analyze_key_position(parkplatz, 4) == "Außerhalb des Parkplatzes"
    assert analyze_key_position(parkplatz, 1) == "frei"
    assert analyze_key_position(parkplatz, 0) == "blockiert"

def test_solve_iterativ():
    parkplatz = [None, "H", "H", None]
    quereAutos = {"H": 1}
    anzahlNormal = len(parkplatz)

    ergebnis, richtung = solve_iterativ(parkplatz, quereAutos, 1, anzahlNormal)
    assert ergebnis == {"H": 1}
    assert richtung in ("links", "rechts") #ist hier egal

    parkplatz = [None, None, "H", "H", None, "I", "I"]
    quereAutos = {"H": 2, "I": 5}

    ergebnis, richtung = solve_iterativ(parkplatz, quereAutos, 5, len(parkplatz))

    assert ergebnis["H"] >= 1
    assert ergebnis["I"] >= 1
    assert richtung in ("links", "rechts")

def test_ausgabe_ergebnisse():
    parkplatz = [None, None, "H", "H", None, "I", "I"]
    quereAutos = {"H": 2, "I": 5}
    anzahlNormal = len(parkplatz)

    expected = [
        "A:",
        "B:",
        "C: H 1 rechts",
        "D: H 1 links",
        "E:",
        "F: H 1 links, I 2 links",
        "G: I 1 links"
    ]

    assert ausgabe_ergebnisse(parkplatz, quereAutos, anzahlNormal) == expected

def test_fill_quere_autos_dict():
    lines = ["H 2", "I 5"]
    result = fill_quere_autos_dict(lines)
    assert result == {"H": 2, "I": 5}

def test_main():
    result = main("/Users/knusper_desktop/Desktop/Schieberei/parkplätze/parkplatz0.txt")

    expected = [
        "A:",
        "B:",
        "C: H 1 rechts",
        "D: H 1 links",
        "E:",
        "F: H 1 links, I 2 links",
        "G: I 1 links"
    ]
    assert result == expected

    result = main("/Users/knusper_desktop/Desktop/Schieberei/parkplätze/parkplatz2.txt")

    expected = [

    "A:",
    "B:",
    "C: O 1 rechts",
    "D: O 1 links",
    "E:",
    "F: O 1 links, P 2 links",
    "G: P 1 links",
    "H: R 1 rechts, Q 1 rechts",
    "I: P 1 links, Q 1 links",
    "J: R 1 rechts",
    "K: P 1 links, Q 1 links, R 1 links",
    "L:",
    "M: P 1 links, Q 1 links, R 1 links, S 2 links",
    "N: S 1 links"
]
    assert result == expected

    result = main("/Users/knusper_desktop/Desktop/Schieberei/parkplätze/parkplatz1.txt")

    expected = [

        "A:",
        "B: P 1 rechts, O 1 rechts",
        "C: O 1 links",
        "D: P 1 rechts",
        "E: O 1 links, P 1 links",
        "F:",
        "G: Q 1 rechts",
        "H: Q 1 links",
        "I:",
        "J:",
        "K: R 1 rechts",
        "L: R 1 links",
        "M:",
        "N:"
    ]

    assert result == expected