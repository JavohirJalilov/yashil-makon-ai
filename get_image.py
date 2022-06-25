import requests
import numpy as np
from PIL import Image

def get_image(url,api_key,lon,lat,zoom):
    """
    Extract a marked location from a map using the Google Maps API.

    Args:
        url(str): Google Maps API
        api_key(str): access key
        lon(str or int): degrees of longitude
        lat(str or int): degrees of latitude
    Returns:
        numpyArray: image
    """