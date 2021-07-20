"""
QR CODE
QR codes are used to encode and decode that data into a machine-readable form.
The use of camera of phones to read two-dimensional barcodes for various purposes is currently a popular topic
in both types of research and practical applications.
"""
import pyqrcode
from pyqrcode import QRCode, create
# string which represent the QR code
target = 'https://www.youtube.com/watch?v=2zecTyFZHUg'
# Generate QR code
url = pyqrcode.create(target)
url.svg('01_youtube_video.svg', scale=8)