subway_system = {
    'Station A': {'Station B'},
    'Station B': {'Station A', 'Station C', 'Station D'},
    'Station C': {'Station B', 'Station D', 'Station E'},
    'Station D': {'Station B', 'Station C', 'Station E', 'Station F'},
    'Station E': {'Station C', 'Station D', 'Station F'},
    'Station F': {'Station D', 'Station E'}
}

from collections import deque

def shortest_route(subway_system, start_station, end_station):
    search_queue = deque()
    search_queue.append((start_station, None))
    searched = {}

    while search_queue:
        station, prev = search_queue.popleft()
        if station not in searched:
            searched[station] = prev

        if end_station:
            result = []
            while station is not None:
                result.append(station)
                station = searched[station]
            return result[::-1]
        else:
            search_queue += [(neighbor, station) for neighbor in subway_system[station]]
    return []



print(shortest_route(subway_system, 'Station A', 'Station F'))