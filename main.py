import Core
import os

def main():
    cmd = 'D:\\Program Files (x86)\\Tesseract-OCR\\tesseract'
    # Include the above line, if you don't have tesseract executable in your PATH
    data = '--tessdata-dir "D:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
    while True:
        file = input('Введите имя файла: ')
        parser = Core.Parser(cmd, data)
        image_file = os.path.join(os.path.dirname(__file__), 'img', 'image.jpg')


if __name__ == "__main__":
    main()