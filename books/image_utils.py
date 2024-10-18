# image_utils.py

from PIL import Image
import io
from django.core.files.uploadedfile import InMemoryUploadedFile

def optimize_image(image, quality=85):
    """
    Optimize an image file by reducing its size.
    
    :param image: The uploaded image file.
    :param quality: Quality level for the optimized image (1-100).
    :return: An optimized InMemoryUploadedFile.
    """
    # Open the uploaded image file
    img = Image.open(image)

    # Use BytesIO to save the optimized image to memory
    img_io = io.BytesIO()
    img.save(img_io, format='JPEG', quality=quality)  # Save as JPEG with specified quality

    # Create a new InMemoryUploadedFile instance
    optimized_image = InMemoryUploadedFile(
        img_io, None, image.name, 'image/jpeg', img_io.getbuffer().nbytes, None
    )
    
    return optimized_image
