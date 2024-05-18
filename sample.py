import boto3
import os
import sys
import uuid
from urllib.parse import unquote_plus
from PIL import Image



with Image.open("week-6/images/lambda-execution-enviorment.PNG") as image:
    image.thumbnail(tuple(x / 2 for x in image.size))
    image.save("sample1.png")

