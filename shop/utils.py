import math


def get_distance(inst, lat, long):
    """
    Function created to calculate distance between two latitude and longitude.
    """
    user_lat, user_long = math.radians(float(lat)), math.radians(float(long))
    shop_lat, shop_long = math.radians(inst.lat), math.radians(inst.long)
    delta_lon = shop_long - user_long
    delta_lat = shop_lat - user_lat
    a = (
        math.sin(delta_lat / 2) ** 2
        + math.cos(user_lat) * math.cos(shop_lat) * math.sin(delta_lon / 2) ** 2
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    # 6373.0 radios of earth.
    return 6373.0 * c
