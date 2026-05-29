# test_time_converter.py
import pytest
from time_converter import convert_to_time

def test_convert_to_time():
    assert convert_to_time(3661) == "1:01:01"
    assert convert_to_time(60) == "0:01:00"
    assert convert_to_time(0) == "0:00:00"
    assert convert_to_time(86399) == "23:59:59"

def test_convert_to_time_invalid_input():
    with pytest.raises(ValueError):
        convert_to_time(-1)
    with pytest.raises(TypeError):
        convert_to_time("invalid")
