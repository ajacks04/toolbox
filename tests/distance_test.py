# tests/distance_test.py
from toolbox.distance import haversine

def test_return():
    assert haversine(48.865070, 2.380009, 48.235070, 2.393409) != None


def test_type():
    distance = haversine(48.865070, 2.380009, 48.235070, 2.393409)
    assert type(distance) == float