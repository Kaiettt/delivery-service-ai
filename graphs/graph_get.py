import osmnx as ox

place = "Ho Chi Minh City, Vietnam"

# Truck
custom_filter_truck = '["highway"~"trunk|trunk_link|primary|primary_link|secondary|secondary_link|tertiary|unclassified|residential|service|road|track"]'
G_truck = ox.graph_from_place(place, custom_filter=custom_filter_truck)

# Car
custom_filter_car = '["highway"~"motorway|motorway_link|trunk|trunk_link|primary|primary_link|secondary|secondary_link|tertiary|unclassified|residential|living_street|service|road|track"]'
G_car = ox.graph_from_place(place, custom_filter=custom_filter_car)

# Motorbike
custom_filter_motorbike = '["highway"~"trunk|trunk_link|primary|primary_link|secondary|secondary_link|tertiary|unclassified|residential|living_street|service|road|track"]'
G_motorbike = ox.graph_from_place(place, custom_filter=custom_filter_motorbike)

ox.save_graphml(G_truck, filepath="graphs/truck_graph_hcm.graphml")
ox.save_graphml(G_car, filepath="graphs/car_graph_hcm.graphml")
ox.save_graphml(G_motorbike, filepath="graphs/motorbike_graph_hcm.graphml")