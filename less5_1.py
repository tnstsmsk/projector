a2_bus = {
    'University Ave & 27th Ave SE': [0, 10, 20, 30, 40, 50],
    'University Ave & Oak St': [3, 13, 23, 33, 43, 53],
    'Washington Ave & Pleasant St SE': [6, 16, 26, 36, 46, 56],
    'Washington Ave SE & Union St SE': [7, 17, 27, 37, 47, 57],
    'Fulton St SE & Delaware St SE': [8, 18, 28, 38, 48, 58],
    'Harvard St SE & Delaware St SE': [9, 19, 29, 39, 49, 59],
}


def bus_timing(bus_stop, minutes):
    for bus_stops, minute in a2_bus.items():
        if bus_stops == bus_stop:
            for min in minute:
                if minutes <= min:
                    result = min - minutes
                    break
                
                elif minutes > max(minute):
                    result = -1

    return result


def test_bus_timing():
    result1 = bus_timing('University Ave & 27th Ave SE', 58)
    assert result1 == -1

    result2 = bus_timing('University Ave & 27th Ave SE', 10)
    assert result2 == 0

    result3 = bus_timing('Fulton St SE & Delaware St SE', 49)
    assert result3 == 9

    print('all tests passed')


test_bus_timing()
