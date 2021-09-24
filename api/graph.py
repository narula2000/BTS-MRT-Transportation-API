from typing import Dict, List, Set, Union

from .models import Station, Station_Link


class Graph:
    def __init__(self):
        self.path = -1
        self.graph: Dict[str, Set[str]] = dict()
        self.createMapping()

    def createMapping(self) -> None:
        def addEdge(current_node: str, next_node: str):
            if current_node not in self.graph:
                self.graph[current_node] = set()
            self.graph[current_node].add(next_node)

        stations_links = Station_Link.objects.all()
        for station in stations_links.iterator():
            current_station_id: str = station.start_station_id
            current_station_info = Station.objects.get(
                station_id=current_station_id)
            current_station_name: str = current_station_info.station_name
            next_station_id: str = station.end_station_id
            next_station_info = Station.objects.get(station_id=next_station_id)
            next_station_name: str = next_station_info.station_name
            addEdge(current_station_name, next_station_name)
            addEdge(next_station_name, current_station_name)

    def dfsByName(self, source_node: str, destination_node: str) -> Union[int, List[str]]:
        def dfsHelper(current_node: str, destination_node: str, visited_set: Set[str], path_lst: List[str]) -> None:
            current_path = path_lst.copy()
            visited_set.add(current_node)
            current_path.append(current_node)
            if current_node == destination_node:
                self.path = current_path
            for station in self.graph[current_node]:
                if station not in visited_set:
                    dfsHelper(station, destination_node,
                              visited_set, current_path)
        path_lst: List[str] = []
        visited_set: Set[str] = set()
        dfsHelper(source_node, destination_node, visited_set, path_lst)
        return self.path

    def dfsById(self, source_node: str, destination_node: str) -> Union[int, List[str]]:
        def dfsHelper(current_node: str, destination_node: str, visited_set: Set[str], path_lst: List[str]) -> None:
            current_path = path_lst.copy()
            visited_set.add(current_node)
            current_path.append(current_node)
            if current_node == destination_node:
                self.path = current_path
            for station in self.graph[current_node]:
                if station not in visited_set:
                    dfsHelper(station, destination_node,
                              visited_set, current_path)
        path_lst: List[str] = []
        visited_set: Set[str] = set()
        source_obj = Station.objects.get(station_id=source_node)
        destination_obj = Station.objects.get(station_id=destination_node)
        dfsHelper(source_obj.station_name,
                  destination_obj.station_name,  visited_set, path_lst)
        return self.path
