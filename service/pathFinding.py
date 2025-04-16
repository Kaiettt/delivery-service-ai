# from models.model import Location
import math
import osmnx as ox
import heapq
import matplotlib.pyplot as plt

class PathFinding:
    @staticmethod
    def find_path(start:tuple, destination:tuple, vehicle_type = 'CAR'):
        """
        Nhận 2 tuple tọa độ và loại xe TRUCK, MOTORBIKE, CAR (mặc định).
        """
        newPathSearch = PathFinding(vehicle_type)
        return newPathSearch.a_star_search(start, destination)
        # return newPathSearch.nodes_to_edges(newPathSearch.a_star_search(start, destination))
    
    def __init__(self, vehicle_type = 'CAR'):
        self.G = ox.load_graphml(filepath=f'graphs/{vehicle_type.lower()}_graph_hcm.graphml')

    def haversine(self, node1, node2):
        """
        Heuristic khoảng cách 2 node.
        """
        # Lấy vĩ độ và kinh độ của 2 node
        lat1, lon1 = self.G.nodes[node1]['y'], self.G.nodes[node1]['x']
        lat2, lon2 = self.G.nodes[node2]['y'], self.G.nodes[node2]['x']

        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.asin(math.sqrt(a))
        # Nhân với bán kính trái đất (khoảng 6371 km)
        distance = 6371 * c
        return distance

    def a_star_search(self, start_coord: tuple, destination_coord: tuple):
        """
        Tìm đường dùng A*, trả về danh sách các tọa độ (lat, lon).
        """
        start = ox.distance.nearest_nodes(self.G, X=start_coord[1], Y=start_coord[0])
        goal = ox.distance.nearest_nodes(self.G, X=destination_coord[1], Y=destination_coord[0])

        frontier = [(self.haversine(start, goal), start)]
        explored = set()
        parents = {start: None}
        costs = {start: 0}

        while frontier:
            f_value, current = heapq.heappop(frontier)

            if current == goal:
                path = []
                while current is not None:
                    path.append(current)
                    current = parents[current]
                path.reverse()

                # ✅ Convert node IDs to (lat, lon) tuples
                latlon_path = [(self.G.nodes[node]['y'], self.G.nodes[node]['x']) for node in path]
                return latlon_path

            if current in explored:
                continue
            explored.add(current)

            for neighbor in self.G.neighbors(current):
                if neighbor in explored:
                    continue
                shortest_edge = min(self.G.get_edge_data(current, neighbor).values(), key=lambda x: x['length'])
                new_cost_neighbor = costs[current] + shortest_edge['length']
                if (neighbor not in costs) or (new_cost_neighbor < costs[neighbor]):
                    costs[neighbor] = new_cost_neighbor
                    f_value = new_cost_neighbor + self.haversine(neighbor, goal)
                    heapq.heappush(frontier, (f_value, neighbor))
                    parents[neighbor] = current

        return None

    
    def straight_path(path:list):
        """
        Xóa các đường đi vòng.
        """
        i = 0
        while i < len(path):
            j = len(path) - 1
            while j > i:
                if path[i] == path[j]:
                    path = path[:i] + path[j:]
                    break
                j -= 1
            i += 1
        return path

    def nodes_to_edges(self, node_path:list):
        """
        Chuyển đổi danh sách các node thành danh sách các edge.
        """
        edge_path = []
        # Lấy node và node kế tiếp
        for u, v in zip(node_path[:-1], node_path[1:]):
            edge_data = self.G.get_edge_data(u, v)
            if edge_data is None:
                continue
            # Lấy key của edge ngắn nhất
            key, attr = min(edge_data.items(), key=lambda x: x[1].get('length', float('inf')))
            length = float(attr['length'])
            edge_path.append((u, v, key, length))
        return edge_path

    def nodes_to_coord(self, node_path:list):
        """
        Chuyển đổi danh sách các node thành danh sách các tọa độ (lat, lon).
        """
        coords = []
        for node in node_path:
            lat = self.G.nodes[node]['y']
            lon = self.G.nodes[node]['x']
            coords.append((lat, lon))
        return coords


start_coord = (10.85974479875821, 106.78019379789899)
end_coord = (10.850807473074543, 106.77127365080172)
G = PathFinding('CAR').G
route = PathFinding.find_path(start_coord, end_coord, 'CAR')

print(route)

# fig, ax = ox.plot_graph_route(G, route, route_linewidth=4, node_size=0)
# plt.show()

# # Plot the route
# fig, ax = ox.plot_graph_route(G, route, route_linewidth=4, node_size=0, show=False, close=False)

# # Add node labels to the route
# for node in route:
#     x = G.nodes[node]['x']
#     y = G.nodes[node]['y']
#     ax.text(x, y, str(node), fontsize=8, color='red', ha='center', va='center')

# plt.show()