import numpy as np
import cv2

def add_white_border(image, border_percentage=0.1):
    """
    Add a white border to the top, bottom, left, and right of the image.

    Parameters:
        image (numpy.ndarray): Input image.
        border_percentage (float): Percentage of image size for border width.

    Returns:
        numpy.ndarray: Image with added border.
    """
    height, width, _ = image.shape

    # Calculate the pixel size of the white border
    border_width = int(width * border_percentage)
    border_height = int(height * border_percentage)

    # Create a white background
    border = 255 * np.ones((height + 2 * border_height, width + 2 * border_width, 3), dtype=np.uint8)

    # Place the input image in the center of the white background
    border[border_height:border_height + height, border_width:border_width + width, :] = image

    return border


def draw_center_marker(image, marker_size=20, marker_thickness=2, marker_color=(0, 255, 0)):
    """
    Draw a marker at the center of the image.

    Parameters:
        image (numpy.ndarray): Input image.
        marker_size (int): Size of the marker.
        marker_thickness (int): Line thickness of the marker.
        marker_color (tuple): Color of the marker (B, G, R).

    Returns:
        numpy.ndarray: Image with the center marker.
    """
    height, width, _ = image.shape

    # Calculate the coordinates of the image center
    center_x = width // 2
    center_y = height // 2

    # Draw a cross-shaped marker at the center of the image
    cv2.line(image, (center_x - marker_size // 2, center_y), (center_x + marker_size // 2, center_y), marker_color,
             marker_thickness)
    cv2.line(image, (center_x, center_y - marker_size // 2), (center_x, center_y + marker_size // 2), marker_color,
             marker_thickness)

    return image


def draw_filled_corner_rectangles(image, distance_percentage=0.025, rectangle_color=(0, 0, 0)):
    """
    Generate black-filled rectangles at the four corners of the image.

    Parameters:
        image (numpy.ndarray): Input image.
        distance_percentage (float): Percentage of the image size for the distance from rectangle edges to image edges.
        rectangle_color (tuple): Color of the rectangles (B, G, R).

    Returns:
        numpy.ndarray: Image with filled rectangles.
    """
    height, width, _ = image.shape

    # Calculate the distance from rectangle edges to image edges
    distance = int(min(height, width) * distance_percentage)

    # Calculate the size of the rectangles
    rectangle_size = int(min(height, width) * 0.025)

    # Generate black-filled rectangles at the four corners of the image
    image[distance:distance + rectangle_size, distance:distance + rectangle_size, :] = rectangle_color  # Top-left
    image[distance:distance + rectangle_size, width - distance - rectangle_size:width - distance,
    :] = rectangle_color  # Top-right
    image[height - distance - rectangle_size:height - distance, distance:distance + rectangle_size,
    :] = rectangle_color  # Bottom-left
    image[height - distance - rectangle_size:height - distance, width - distance - rectangle_size:width - distance,
    :] = rectangle_color  # Bottom-right

    return image


def overlay_single_image_top_center_x(background_image, overlay_path, scale_factor=0.5):
    """
    Overlay an image at the top center of the background image.

    Parameters:
        background_image (str): Path to the background image.
        overlay_path (str): Path to the image to overlay.
        scale_factor (float): Scaling factor, default is 0.5.

    Returns:
        None
    """

    # Read the image to be overlayed
    overlay_image = cv2.imread(overlay_path)

    if overlay_image is not None:
        # Scale the overlay image
        scaled_overlay = cv2.resize(overlay_image, (round(background_image.shape[0] * 0.05),
                                                    round(background_image.shape[1] * 0.05)))

        # Get the size of the overlay image
        h, w, _ = scaled_overlay.shape

        # Place the overlay image at the top center of the background image
        x = (background_image.shape[1] - w) // 2 - round(background_image.shape[1] * 0.15)
        y = round(background_image.shape[0] * 0.01)  # Place it at the top center

        # Overlay the image on the background image
        background_image[y:y + h, x:x + w] = scaled_overlay

        # Return the resulting image
        return background_image


def overlay_single_image_top_center_upenn(background_image, overlay_path, scale_factor=0.5):
    """
    Overlay an image at the top center of the background image.

    Parameters:
        background_image (str): Path to the background image.
        overlay_path (str): Path to the image to overlay.
        scale_factor (float): Scaling factor, default is 0.5.

    Returns:
        None
    """
    # Read the image to be overlayed
    overlay_image = cv2.imread(overlay_path)

    if overlay_image is not None:
        # Scale the overlay image
        scaled_overlay = cv2.resize(overlay_image, (round(background_image.shape[1] * 0.15),
                                                    round(overlay_image.shape[0] * (background_image.shape[1] * 0.15) /
                                                          overlay_image.shape[1])))

        # Get the size of the overlay image
        h, w, _ = scaled_overlay.shape

        # Place the overlay image at the top center of the background image
        x = (background_image.shape[1] - w) // 2 + round(background_image.shape[1] * 0.05)
        y = round(background_image.shape[0] * 0.015)  # Place it at the top center

        # Overlay the image on the background image
        background_image[y:y + h, x:x + w] = scaled_overlay

        # Return the resulting image
        return background_image

def draw_text_on_image(image, area_id, x_distance, y_distance, w, h, midpoint_lat, midpoint_lon):
    # Define font properties
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = image.shape[0] / 2000.0
    font_thickness = round(font_scale * 2)
    font_color = (0, 0, 0)

    # Prepare text lines
    text_lines = [
        area_id,
        f"X Distance: {x_distance:.2f} m, X Res:{x_distance / w:.4f}",
        f"Y Distance: {y_distance:.2f} m, Y Res:{y_distance / h:.4f}",
        f"Midpoint: ({midpoint_lat:.6f}, {midpoint_lon:.6f})"
    ]

    # Calculate text position
    text_position = (
        round(image.shape[1] * 0.5), round(image.shape[0] * 0.98))

    # Draw text on the image
    for i, line in enumerate(text_lines):
        y_offset = i * int(30 * font_scale)
        cv2.putText(image, line, (text_position[0], text_position[1] - y_offset), font, font_scale, font_color,
                    font_thickness)

    return image