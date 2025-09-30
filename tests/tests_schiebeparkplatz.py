import pytest
from src.schiebeparkplatz import read_in_parkplatz

def test_read_in_parkplatz(tmp_path):

    test_file = tmp_path / "parkplatz.txt"
    test_file.write_text("Parkplatz A\nParkplatz B\n")

    result = read_in_parkplatz(str(test_file))

    assert result == ["Parkplatz A", "Parkplatz B"]