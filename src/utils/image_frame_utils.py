import math
import pdb
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

class ImageProcessor:
    def resize_image(self,pixel_values, original_width=200, new_width=150):
        images = []
        for pixels in pixel_values:
            image = np.array(pixels).reshape(-1, original_width)
            image_np = np.array(image, dtype=np.uint8)
            image_pil = Image.fromarray(image_np)
            aspect_ratio = image_pil.width / float(image_pil.height)
            new_height = math.ceil(new_width / aspect_ratio)
            image_resized = image_pil.resize((new_width, new_height), Image.LANCZOS)
            images.append(np.array(image_resized).flatten())
        return np.array(images)

    def apply_custom_colormap(self,pixels, width=150):
        image = np.array(pixels).reshape(-1, width)
        colormap = plt.cm.viridis
        colored_image = colormap(image)
        color_applied_rgb = (colored_image[:, :, :3] * 255).astype(np.uint8)
        return color_applied_rgb.tolist()