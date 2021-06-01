def GetDistance(edges, route):
    global distance, first_node, to_node
    distance = 0
    route_step = 0
    first_node = route[route_step]
    from_node = route[route_step]
    to_node = route[route_step + 1]
    for edge in edges:
        if edge[0] is from_node:
            if edge[1] is to_node:
                distance += edge[2]
                route_step += 1
                from_node = route[route_step]
                to_node = route[route_step + 1]
                if to_node is route[len(route) - 1]:
                    to_node = route[len(route) - 2]
                    break


def PrintData():
    print("The starting node is: " + str(first_node))
    print("The ending node is: " + str(to_node))
    print("Distance from path A-B-C is: " + str(distance))


def main():
    edges = [['A', 'B', 5], ['B', 'C', 4], ['C', 'D', 8], ['D', 'C', 8], ['D', 'E', 6], ['A', 'D', 5], ['C', 'E', 2],
             ['E', 'B', 3], ['A', 'E', 7]]
    route = ['A', 'B', 'C', '']
    GetDistance(edges, route)
    PrintData()


main()
