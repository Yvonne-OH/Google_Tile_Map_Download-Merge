from geopy.distance import geodesic

def calculate_xy_distance(lat1, lon1, lat2, lon2):
    # Use Vincenty formula to calculate distance
    coords_1 = (lat1, lon1)
    coords_2 = (lat2, lon2)

    # Calculate total distance
    total_distance = geodesic(coords_1, coords_2).meters

    # Calculate longitude direction (X direction) distance
    x_distance = geodesic((lat1, lon1), (lat1, lon2)).meters

    # Calculate latitude direction (Y direction) distance
    y_distance = geodesic((lat1, lon1), (lat2, lon1)).meters

    print(f"X direction distance: {x_distance:.2f} m")
    print(f"Y direction distance: {y_distance:.2f} m")
    print(f"Total distance: {total_distance:.2f} m")

    return x_distance, y_distance, total_distance


def calculate_midpoint(lat1, lon1, lat2, lon2):
    # Calculate average latitude and longitude
    mid_lat = (lat1 + lat2) / 2.0
    mid_lon = (lon1 + lon2) / 2.0
    print(f"Midpoint coordinates: Latitude {mid_lat:.6f}, Longitude {mid_lon:.6f}")

    return mid_lat, mid_lon

def calculate_xy_distance(lat1, lon1, lat2, lon2):
    # Calculate distance using the Vincenty formula
    coords_1 = (lat1, lon1)
    coords_2 = (lat2, lon2)

    # Calculate total distance
    total_distance = geodesic(coords_1, coords_2).kilometers

    # Calculate distance in the longitude direction (X direction)
    x_distance = geodesic((lat1, lon1), (lat1, lon2)).kilometers

    # Calculate distance in the latitude direction (Y direction)
    y_distance = geodesic((lat1, lon1), (lat2, lon1)).kilometers

    return x_distance, y_distance, total_distance