import os
import sys
import time
from PIL import Image
import cv2
from blessed import Terminal
from colorama import init

term = Terminal()
init()

DEFAULT_CHARSET = "@#$%&*()0!=-.,"
DEFAULT_COLOR = False
IMG_SIZE = (0, 0)  # Will be set based on terminal size
imgs = []

def get_terminal_size():
    return os.get_terminal_size()

def pix_to_code(i, img):
    x = i % IMG_SIZE[0]
    y = i // IMG_SIZE[0]
    code = img.getpixel((x, y))
    return f"\033[38;2;{code[0]};{code[1]};{code[2]}m"

def print_img(image, is_colored):
    img = image.resize(IMG_SIZE, Image.Resampling.LANCZOS)
    gimg = img.convert('L')
    img = img.quantize(colors=32).convert('RGB')
    pixels = list(gimg.getdata())

    output_string = ""
    last_color = None

    for i, pixel in enumerate(pixels):
        if i % IMG_SIZE[0] == 0 and i != 0:
            output_string += "\n"
        
        ind = int(pixel / 255 * (len(DEFAULT_CHARSET) - 1))
        char = DEFAULT_CHARSET[ind]

        if is_colored:
            color = pix_to_code(i, img)
            if color != last_color:
                output_string += "\033[0;39m" + color + char
                last_color = color
            else:
                output_string += char
        else:
            output_string += char

    with term.hidden_cursor():
        sys.stdout.write(term.home + output_string)
        sys.stdout.flush()

def open_video(file):
    vid = cv2.VideoCapture(file)
    if not vid.isOpened():
        print(f"Error: Unable to open video file {file}.")
        return

    while True:
        ret, img = vid.read()
        if not ret:
            break
        conv = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        imgs.append(Image.fromarray(conv))

    vid.release()

def open_image(file):
    try:
        return Image.open(file)
    except Exception as e:
        print(f"Error: Unable to open image file {file}. {e}")
        return None

def main():
    global IMG_SIZE, DEFAULT_COLOR, DEFAULT_CHARSET

    IMG_SIZE = get_terminal_size()
    if len(sys.argv) < 2:
        print("No file provided. Please provide an image or video file as an argument.")
        return

    file_path = sys.argv[1]

    if file_path.split('.')[-1] in ["mp4", "avi", "mov", "gif"]:
        open_video(file_path)
    else:
        img = open_image(file_path)
        if img:
            imgs.append(img)

    for arg in sys.argv[2:]:
        match arg:
            case "-c":
                DEFAULT_COLOR = True
            case "-f":
                DEFAULT_CHARSET = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,^`'."
    
    for img in imgs:
        print_img(img, DEFAULT_COLOR)
        time.sleep(0.033)  # Approx. 30fps

    print("\033[0;39m")

if __name__ == "__main__":
    main()
