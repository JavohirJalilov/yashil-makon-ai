# import requests
# from PIL import Image
# import io
# # imprt numpy
# import cv2
# import numpy as np 
# api_key = 'AIzaSyAGbq62NbISl1Z5of3rchhA_dG_HYmGfQs'
# lat = 39.6436225
# lon = 66.99086
# zoom = 19
# url = f"https://maps.googleapis.com/maps/api/staticmap?center={lat},{lon}&zoom={zoom}&size=400x400&maptype=satellite&key={api_key}"

# response = requests.get(url).content
# image = Image.open(io.BytesIO(response)).convert()
# image = np.array(image)
# image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
# cv2.imwrite('map.png', image)
import telegram 
from settings import TOKEN
bot = telegram.Bot(token=TOKEN)
info = bot.get_webhook_info()
print(info)
