import pytest
from src.schiebeparkplatz import read_in_parkplatz
from src.schiebeparkplatz import read_first_line
from src.schiebeparkplatz import char_to_num
from src.schiebeparkplatz import read_rest
from src.schiebeparkplatz import parkplatz_fuellen
from src.schiebeparkplatz import find_key_positions
from src.schiebeparkplatz import analyze_key_position
from src.schiebeparkplatz import solve_iterativ

def test_read_in_parkplatz(tmp_path):

    test_file = tmp_path / "parkplatz.txt"
    test_file.write_text("Parkplatz A\nParkplatz B\n")

    result = read_in_parkplatz(str(test_file))

    assert result == ["Parkplatz A", "Parkplatz B"]



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
