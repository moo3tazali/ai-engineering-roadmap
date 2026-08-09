shipments = [
    "Alexandria",
    "Cairo",
    "Jeddah",
    "Dammam",
    "Riyadh",
]

print(shipments[0])
print(shipments[-1])
shipments[1] = "Cairo Airport"
shipments.append("Dubai")
gulf_shipments = ["Jeddah", "Dammam", "Riyadh"]
routes = [shipments, gulf_shipments]
print(routes[1][1])
print(shipments)

shipments.append("Doha")

print(routes[0])
