subway_system = {
    'Station A': {'Station B'},
    'Station B': {'Station A', 'Station C', 'Station D'},
    'Station C': {'Station B', 'Station D', 'Station E'},
    'Station D': {'Station B', 'Station C', 'Station E', 'Station F'},
    'Station E': {'Station C', 'Station D', 'Station F'},
    'Station F': {'Station D', 'Station E'}
}

def shortest_route(subway_system, start_station, end_station):
    return


print(shortest_route(subway_system, 'Station A', 'Station F'))