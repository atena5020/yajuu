from PIL import Image
import time
a = Image.open("/home/tatu/snap/yaju_senpai.png")
for i in range(30):
    time.sleep(7)
    a.show()