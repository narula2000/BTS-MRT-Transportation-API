from .models import Station, Station_Link


class Graph:
    def __init__(self):
        self.path = -1
        self.all_path = []
        self.graph = dict()
        self.createMapping()

    def createMapping(self):
        def addEdge(current_node, next_node):
            if current_node not in self.graph:
                self.graph[current_node] = set()
            self.graph[current_node].add(next_node)

        stations_links = Station_Link.objects.all()
        for station in stations_links.iterator():
            current_station_id = station.start_station_id
            current_station_info = Station.objects.get(
                station_id=current_station_id)
            current_station_name = current_station_info.station_name
            next_station_id = station.end_station_id
            next_station_info = Station.objects.get(station_id=next_station_id)
            next_station_name = next_station_info.station_name
            addEdge(current_station_name, next_station_name)
            addEdge(next_station_name, current_station_name)

    def dfs(self, source_node, destination_node):
        def dfsHelper(current_node, destination_node,
                       visited_set, path_lst):
            current_path = path_lst.copy()
            visited_set.add(current_node)
            current_path.append(current_node)
            if current_node == destination_node:
                self.path = current_path
            for station in self.graph[current_node]:
                if station not in visited_set:
                    dfsHelper(station, destination_node,
                                    visited_set, current_path)
        path_lst = []
        visited_set = set()
        dfsHelper(source_node, destination_node, visited_set, path_lst)
        return self.path
