import pytest
from src.schiebeparkplatz import read_in_parkplatz
from src.schiebeparkplatz import read_first_line

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
