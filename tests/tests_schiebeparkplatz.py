import pytest
from src.schiebeparkplatz import read_in_parkplatz
from src.schiebeparkplatz import read_first_line
from src.schiebeparkplatz import char_to_num
from src.schiebeparkplatz import read_rest

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