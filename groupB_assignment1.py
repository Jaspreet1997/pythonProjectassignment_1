def shortest_path(edges):
    begining_node = "A"
    ending_node = "C"
    routeList = []
    stopsList = get_stops(begining_node, edges)
    get_routes(stopsList, ending_node, routeList, edges)
    if routeList[0][2] < routeList[1][2]:
        return begining_node + str(routeList[0][0]) + str(routeList[0][1])
    else:
        return begining_node + str(routeList[1][0]) + str(routeList[1][1])


def route_distance(route_input, edges):
    route = list(route_input)

    total_dist = 0
    for x in range(0, len(route) - 1):
        from_city = route[x]
        to_city = route[x + 1]
        distance = 0

        for edge in edges:
            if edge[0] == from_city and edge[1] == to_city:
                distance += int(edge[2])

        if distance > 0:
            total_dist += distance
        else:
            total_dist = 0

    return total_dist


def get_stops(start_node, edges):
    first_endNodes = []
    for edge in edges:
        if edge[0] == start_node:
            first_endNodes.append(edge[1])
    return first_endNodes


def get_routes(stopsList, end_node, routeList, edges):
    for x in range(len(stopsList) - 1):
        for edge in edges:
            if edge[0] == stopsList[x]:
                if edge[1] == end_node:
                    routeList.append(edge)


def group_B():
    edges = [['A', 'B', 5], ['A', 'D', 5], ['A', 'E', 7], ['E', 'B', 3], ['B', 'C', 4], ['C', 'D', 8], ['D', 'C', 8],
             ['E', 'D', 6], ['C', 'E', 2]]
    print("Let's find out the shortest path which goes to between A and C.")
    route = shortest_path(edges)
    dist = route_distance(route, edges)

    if dist > 0:
        print(f"Here is the Shortest route length is: {dist}")
    else:
        print("Sorry! no such route exists.")


group_B()