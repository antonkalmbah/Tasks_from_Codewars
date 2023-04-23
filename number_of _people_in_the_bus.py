bus_stops = [[10,0],[3,5],[5,9]]


def number(bus_stops):
    num_people = 0
    for i, u in bus_stops:
        num_people += + i - u

    print(num_people)


number(bus_stops)