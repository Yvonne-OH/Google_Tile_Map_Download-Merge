import requests
import math
from tqdm import tqdm
import os


def requestImage(api_key,picHeight, picWidth, zoom, scale, maptype, lat, lng, row, col):
    center = str(lat) + "," + str(lng)
    url = "https://maps.googleapis.com/maps/api/staticmap?center=" + center + "&zoom=" + str(zoom) + "&size=" + str(
        picWidth) + "x" + str(picHeight) + "&key=" + api_key + "&maptype=" + maptype + "&scale=" + str(scale)

    # Create a new folder for each col if it doesn't exist
    output_folder = os.path.join("output", f"{col}")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # filename = os.path.join(output_folder,str(col) + "," + str(row) + ".png")
    filename = os.path.join(output_folder, str(row) + ".png")

    r = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(r.content)
    f.close()

    # print("writtern to file: " + filename)


def download_map_tiles(api_key, northWestLat, northWestLng, southEastLat, southEastLng, scale=2, maptype="satellite",
                       zoom=20, picHeight=640, picWidth=640):
    mapHeight = 256
    mapWidth = 256
    xScale = math.pow(2, zoom) / (picWidth / mapWidth)
    yScale = math.pow(2, zoom) / (picHeight / mapWidth)

    startLat = northWestLat
    startLng = northWestLng

    startCorners = getImageBounds(mapWidth, mapHeight, xScale, yScale, startLat, startLng)
    lngStep = startCorners[3] - startCorners[1]

    col = 0
    lat = startLat

    # Calculate the total number of tiles to download
    total_tiles = abs(int((northWestLat - southEastLat) / getLatStep(mapWidth, mapHeight, yScale, lat, startLng)) * \
                      int((southEastLng - northWestLng) / lngStep))

    with tqdm(total=total_tiles, desc="Downloading Map Tiles") as pbar:
        while lat >= southEastLat:
            lng = startLng
            row = 0

            while lng <= southEastLng:
                requestImage(api_key,picHeight, picWidth, zoom, scale, maptype, lat, lng, row, col)
                row += 1
                lng += lngStep
                pbar.update(1)

            col -= 1
            lat += getLatStep(mapWidth, mapHeight, yScale, lat, lng)


def getImageBounds(mapWidth, mapHeight, xScale, yScale, lat, lng):
    centreX, centreY = latLngToPoint(mapWidth, mapHeight, lat, lng)

    southWestX = centreX - (mapWidth / 2) / xScale
    southWestY = centreY + (mapHeight / 2) / yScale
    SWlat, SWlng = pointToLatLng(mapWidth, mapHeight, southWestX, southWestY)

    northEastX = centreX + (mapWidth / 2) / xScale
    northEastY = centreY - (mapHeight / 2) / yScale
    NElat, NElng = pointToLatLng(mapWidth, mapHeight, northEastX, northEastY)

    return [SWlat, SWlng, NElat, NElng]


def getLatStep(mapWidth, mapHeight, yScale, lat, lng):
    pointX, pointY = latLngToPoint(mapWidth, mapHeight, lat, lng)

    steppedPointY = pointY - ((mapHeight) / yScale)
    newLat, originalLng = pointToLatLng(mapWidth, mapHeight, pointX, steppedPointY)

    latStep = lat - newLat

    return (latStep)


def latLngToPoint(mapWidth, mapHeight, lat, lng):
    x = (lng + 180) * (mapWidth / 360)
    y = ((1 - math.log(math.tan(lat * math.pi / 180) + 1 / math.cos(lat * math.pi / 180)) / math.pi) / 2) * mapHeight

    return (x, y)


def pointToLatLng(mapWidth, mapHeight, x, y):
    lng = x / mapWidth * 360 - 180

    n = math.pi - 2 * math.pi * y / mapHeight
    lat = (180 / math.pi * math.atan(0.5 * (math.exp(n) - math.exp(-n))))

    return (lat, lng)

