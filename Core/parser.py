try:
    import Image
    import pytesseract
except ImportError:
    from PIL import Image
from pytesseract import image_to_string


class Parser(object):
    def __init__(self, tesseract_cmd, tessdata_dir_config):
        pytesseract.pytesseract.tesseract_cmd = tesseract_cmd
        self.__tessdata = tessdata_dir_config
    def Parse(self, filepath, lang):
        return image_to_string(Image.open(filepath), lang=lang, config=self.__tessdata)



