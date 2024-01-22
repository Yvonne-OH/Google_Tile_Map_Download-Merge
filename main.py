import cv2
import os

import Tile_Map_Download
import Tile_Map_Merge
import Gis_Calculate
import Image_Processing
import Readme_Fun
import shutil

if __name__ == '__main__':
    # Bounding box for area to be scanned. AreaID is added to file name.
    AreaID = "Wissahickon Transportation Center to Hunting Park Station"

    northWestLat, northWestLng = 40.025, -75.216
    southEastLat, southEastLng = 40.005, -75.141
    #southEastLat, southEastLng = 40.07, -75.07 40.015 -75.216

    # Your API request
    api_key = "AIzaSyCW7tBPP3eWvJMFG3Y7QI_LCY6hZj31MtU"

    folder_path = os.path.join(os.getcwd(), 'output')
    if os.path.exists(folder_path):

        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
    else:
        print(f'Folder {folder_path} does not exist.')

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
    #merged_image = Image_Processing.overlay_single_image_top_center_x(merged_image, os.getcwd() + '\\Logo\\Xlab.png')
    #merged_image = Image_Processing.overlay_single_image_top_center_upenn(merged_image, os.getcwd() + '\\Logo\\Upenn.jpg')
    merged_image = Image_Processing.draw_text_on_image(merged_image, AreaID, x_distance, y_distance, w, h, midpoint_lat, midpoint_lon)

    print(cv2.imwrite("merge.jpg", merged_image))
