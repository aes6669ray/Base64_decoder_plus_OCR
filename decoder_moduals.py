import base64
from PIL import Image
import pytesseract
import os



def write_pic(dcode,num_index):
    picname="准考證pic/"+str(num_index)+".jpg"
    try:
        with open(picname,"wb") as pic:
            pic.write(base64.b64decode(dcode))
            pic.close()
    except:
        print("write_pic_fail"+str(num_index))
    return picname


def img_to_str(img_file):
    img_file=(r"%s" % img_file)
    img=Image.open(img_file)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    try:
        text=pytesseract.image_to_string(img,lang="eng")
        os.remove(img_file)
    except:
        print("convert fail")
        

    return text



