import regex as re

def get_altitud(altitud: str):
    number_pat = "\d+"
    nums = re.findall(number_pat, altitud)
    alt_values = [float(nums[0]),float(nums[1])]
    if len(nums) > 2:
        isdig = [len(x) for x in nums]
        one_index = isdig.index(1)
        new_num = nums[one_index] + nums[one_index + 1]
        alt_values = [float(nums[one_index - 1]), float(new_num)]
    alt_values.sort()
    return alt_values

def add_text_at_list(u : list, text: str):
    n = len(u)
    for i in range(n):
        u[i] = str(u[i]) + text

def grade_to_real(coord: str):
    number_pattern = "(\d+)°\s(\d+)’?"
    coord = re.findall(number_pattern, coord)[0]
    real_coords = 0
    for i in range(len(coord)):
        real_coords += float(coord[i]) * 60 ** (-i)
    return real_coords 

coords_sign = {
    'norte': 1,
    'sur' : -1,
    'este': -1,
    'oeste': 1
}

def get_latlong(latlong: str):
    latitud, longitud = latlong.split(";")[:2]
    coords_pattern = "\d+°\s\d+’?" # 
    direction_pattern = "norte|sur|este|oeste"
    lat_coords = re.findall(coords_pattern, latitud)
    lat_dir = re.findall(direction_pattern, latitud)[0]
    lon_coords = re.findall(coords_pattern, longitud)
    lon_dir = re.findall(direction_pattern, longitud)[0]
    lat1 = grade_to_real(lat_coords[0])
    lat2 = grade_to_real(lat_coords[1])
    lon1 = grade_to_real(lon_coords[0])
    lon2 = grade_to_real(lon_coords[1])
    latitud = [lat1 * coords_sign[lat_dir],lat2 * coords_sign[lat_dir]]
    latitud.sort()
    longitud = [lon1 * coords_sign[lon_dir], lon2 * coords_sign[lon_dir]]
    longitud.sort()
    return latitud + longitud
