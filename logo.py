import numpy as np
import cv2
import random

def generate_logo(brand_name, font_size=100, bg_color=(255, 255, 255), output_path='logo.png'):
    # Create a blank white image
    image_size = (200, 200)
    img = np.ones((image_size[1], image_size[0], 3), dtype=np.uint8)
    img[:] = bg_color

    # Get the first letter of the brand name
    first_letter = brand_name[0]

    # Select a font
    font = cv2.FONT_HERSHEY_SIMPLEX

    # Calculate text size and position
    (text_width, text_height), baseline = cv2.getTextSize(first_letter, font, font_size, 2)
    text_x = (image_size[0] - text_width) // 2
    text_y = (image_size[1] + text_height) // 2  # Adjust for baseline

    # Draw the text on the image
    cv2.putText(img, first_letter, (text_x, text_y), font, font_size, (0, 0, 0), 2)

    # Save the image
    cv2.imwrite(output_path, img)

# Example usage:
brand_name = 'MyBrand'
generate_logo(brand_name)
