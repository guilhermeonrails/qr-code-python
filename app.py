import pyqrcode

url = pyqrcode.create('https://guilhermeonrails.github.io/guilima_burger/')
url.svg('guilima-burger.svg', scale=6)
url.png('guilima-burger.png', scale=5)