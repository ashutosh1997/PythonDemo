import random
import urllib.request


def download(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)

download("https://www.facebook.com/rsrc.php/v3/yx/r/pyNVUg5EM0j.png")
