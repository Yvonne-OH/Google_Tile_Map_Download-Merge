import cv2
import os

import Tile_Map_Download
import Tile_Map_Merge
import Gis_Calculate
import Image_Processing
import Readme_Fun



if __name__ == '__main__':
    # Bounding box for area to be scanned. AreaID is added to file name.
    AreaID = "Roosevelt Blvd"
    northWestLat, northWestLng = 40.07, -75.0525
    #southEastLat, southEastLng = 40.055, -75.0325
    southEastLat, southEastLng = 40.065, -75.0475

    # Your API request
    api_key = "xxxxxxxx"

    # --- do not change variables below this point ---
    Readme_Fun.print_copyright_info()
    Tile_Map_Download.download_map_tiles(api_key, northWestLat, northWestLng, southEastLat, southEastLng)
    x_distance, y_distance, total_distance = Gis_Calculate.calculate_xy_distance(northWestLat, northWestLng, southEastLat,
                                                                   southEastLng)
    midpoint_lat, midpoint_lon = Gis_Calculate.calculate_midpoint(northWestLat, northWestLng, southEastLat, southEastLng)
    merged_image = Tile_Map_Merge.merge_images_in_folders(os.getcwd() + '\output')
    h, w, _ = merged_image.shape
    print("X_Resolution", x_distance / w, "Y_Resolution", y_distance / h)
    merged_image = Image_Processing.draw_center_marker(merged_image, marker_size=int(merged_image.shape[0] * 0.05),
                                      marker_thickness=int(merged_image.shape[0] * 0.005), marker_color=(0, 0, 255))
    merged_image = Image_Processing.add_white_border(merged_image, border_percentage=0.1)
    merged_image = Image_Processing.draw_filled_corner_rectangles(merged_image)
    merged_image = Image_Processing.overlay_single_image_top_center_x(merged_image, os.getcwd() + '\\Logo\\Xlab.png')
    merged_image = Image_Processing.overlay_single_image_top_center_upenn(merged_image, os.getcwd() + '\\Logo\\Upenn.jpg')
    merged_image = Image_Processing.draw_text_on_image(merged_image, AreaID, x_distance, y_distance, w, h, midpoint_lat, midpoint_lon)

    cv2.imwrite("merge.jpg", merged_image)
