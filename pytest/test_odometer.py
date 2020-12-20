def test_is_ascending():
    odo = Odometer(3)
    assert odo.is_ascending(2) == True
    assert odo.is_ascending(523) == False
    assert odo.is_ascending(522) == False


def test_next_reading():
    pass


def test_previous_reading():
    pass


def test_diff():
    pass
