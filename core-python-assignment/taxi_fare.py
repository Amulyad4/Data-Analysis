BASE_FARE = 50
DISTANCE_FARE = 10

def calculate_fare(distance):
    return BASE_FARE + distance * DISTANCE_FARE

def total_fare(trips):
    fares = [calculate_fare(d) for d in trips]
    total = sum(fares)
    return fares, total

trips = [5, 10, 3]
fares, total = total_fare(trips)
for i, fare in enumerate(fares, 1):
    print(f"Trip {i}: ${fare}")
print("Total Fare:", f"${total}")
