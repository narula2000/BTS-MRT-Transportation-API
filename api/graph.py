from .models import Station


class Graph:
    def __init__(self):
        self.path = -1
        self.all_path = []
        self.graph = dict()
        self.createMapping()

    def createMapping(self):
        stations = list(Station.objects.all())
        number_of_stations = len(stations)
        for idx in range(number_of_stations):
            station_info = stations[idx]
            # 'BSKMC' ==> BTS Sukhumvit line Mo Chit
            station_id = station_info.station_id
            # 'Mo Chit'
            station_name = station_info.station_name
            if idx == 0:
                prev_station_name = station_name
                prev_station_id = station_id
            # Change of line i.e. Sukhumvit line to Silom line
            elif prev_station_id[:3] != station_id[:3]:
                prev_station_id = station_id
                prev_station_name = station_name
            else:
                self.addEdge(prev_station_name, station_name)
                self.addEdge(station_name, prev_station_name)
                prev_station_name = station_name
                prev_station_id = station_id

    def addEdge(self, current_node, next_node):
        if current_node not in self.graph:
            self.graph[current_node] = set()
        self.graph[current_node].add(next_node)

    def dfs(self, source_node, destination_node):
        path_lst = []
        visited_set = set()
        self.dfs_helper(source_node, destination_node, visited_set, path_lst)
        return self.path

    def dfs_helper(self, current_node, destination_node,
                   visited_set, path_lst):
        current_path = path_lst.copy()
        visited_set.add(current_node)
        current_path.append(current_node)
        if current_node == destination_node:
            self.path = current_path
        for station in self.graph[current_node]:
            if station not in visited_set:
                self.dfs_helper(station, destination_node,
                                visited_set, current_path)
