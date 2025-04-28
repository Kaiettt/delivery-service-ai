import osmnx as ox
import matplotlib.pyplot as plt
import heapq
import json

def boundary_landmarks(G):
    nodes = list(G.nodes(data=True))
    lats = [data['y'] for _,data in nodes]
    lons = [data['x'] for _,data in nodes]
    min_lat, max_lat = min(lats), max(lats)
    min_lon, max_lon = min(lons), max(lons)
    
    sw = ox.distance.nearest_nodes(G, min_lon, min_lat)
    se = ox.distance.nearest_nodes(G, max_lon, min_lat)
    ne = ox.distance.nearest_nodes(G, max_lon, max_lat)
    nw = ox.distance.nearest_nodes(G, min_lon, max_lat)
    return [sw, se, ne, nw]

def UCS_landmarks(G, landmark):
    node = None
    frontier = [(0, landmark)]
    cost = {}
    explored = set()
    while frontier:
        node_cost, node = heapq.heappop(frontier)
        if node in explored:
            continue
        cost[str(node)] = node_cost
        explored.add(node)
        for neighbor in G.neighbors(node):
            if neighbor in explored:
                continue
            new_cost = node_cost + G.edges[node, neighbor, 0]['length']
            heapq.heappush(frontier, (new_cost, neighbor))
    return cost

# Đơn vị tính bằng mét
landmarks = []
landmarks_costs = []

# car
G = ox.load_graphml(filepath=f'graphs/car_graph_hcm.graphml')
landmarks = boundary_landmarks(G)
for landmark in landmarks:
    costs = UCS_landmarks(G, landmark)
    landmarks_costs.append(costs)
with open('graphs/car_landmarks.json', 'w') as f:
    json.dump(landmarks_costs, f)

# motorbike
G = ox.load_graphml(filepath=f'graphs/motorbike_graph_hcm.graphml')
landmarks = boundary_landmarks(G)
for landmark in landmarks:
    costs = UCS_landmarks(G, landmark)
    landmarks_costs.append(costs)
with open('graphs/motorbike_landmarks.json', 'w') as f:
    json.dump(landmarks_costs, f)

# truck
G = ox.load_graphml(filepath=f'graphs/truck_graph_hcm.graphml')
landmarks = boundary_landmarks(G)
for landmark in landmarks:
    costs = UCS_landmarks(G, landmark)
    landmarks_costs.append(costs)
with open('graphs/truck_landmarks.json', 'w') as f:
    json.dump(landmarks_costs, f)
