import osmnx as ox
import matplotlib.pyplot as plt

place = "Ho Chi Minh City, Vietnam"

# Truck
G_truck = ox.load_graphml(filepath="graphs/truck_graph_hcm.graphml")
print("Số lượng nút (nodes) của G_truck:", len(G_truck.nodes))
# Car
G_car = ox.load_graphml(filepath="graphs/car_graph_hcm.graphml")
print("Số lượng nút (nodes) của G_car:", len(G_car.nodes))

# Motorbike
G_motorbike = ox.load_graphml(filepath="graphs/motorbike_graph_hcm.graphml")
print("Số lượng nút (nodes) của G_motorbike:", len(G_motorbike.nodes))

# Vẽ đồ thị
fig, ax = plt.subplots(1, 3, figsize=(18,6))
ox.plot_graph(G_truck, ax=ax[0], node_size=5, edge_color="red", show=False, close=False)
ax[0].set_title("Graph dành cho Truck")
ox.plot_graph(G_car, ax=ax[1], node_size=5, edge_color="blue", show=False, close=False)
ax[1].set_title("Graph dành cho Car")
ox.plot_graph(G_motorbike, ax=ax[2], node_size=5, edge_color="green", show=False, close=False)
ax[2].set_title("Graph dành cho Motorbike")
plt.show()