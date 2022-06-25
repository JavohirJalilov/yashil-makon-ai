import requests
import numpy as np
from PIL import Image
import io

def get_image(api_key,lon,lat,zoom=19):
    """
    Extract a marked location from a map using the Google Maps API.

    Args:
        api_key(str): access key
        lon(str or int): degrees of longitude
        lat(str or int): degrees of latitude
    Returns:
        numpyArray: image
    """
    url = f"https://maps.googleapis.com/maps/api/staticmap?center={lat},{lon}&zoom={zoom}&size=400x400&maptype=hybrid&key={api_key}"

    response = requests.get(url).content
    image = Image.open(io.BytesIO(response)).convert()
    image = np.array(image)

    return image
