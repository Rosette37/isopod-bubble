from PIL import ImageGrab, Image
from io import BytesIO
import pyperclip, os, win32clipboard

dir_name = os.path.dirname(__file__)

#function to save completed picture to clipboard
def send_to_clipboard(image):
    #convert image to data
    output = BytesIO()
    image.convert('RGB').save(output, 'BMP')
    data = output.getvalue()[14:]
    output.close()

    #save data to clipboard
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()

print("screenshot an image\nthe completed image will be saved to your clipboard automatically,\nand then this window will close")
#detect when image is copied
while True:
    pyperclip.copy(".")
    pyperclip.waitForNewPaste()
    if pyperclip.paste() == "":
        break

#get image from clipboard
img = ImageGrab.grabclipboard()
#resize image
img = img.resize((116, 74))

#get isopod image
isopod = Image.open(dir_name + r"/base.png")
#paste copied image onto isopod image at the coordinates of the box tuple
box = (57, 2, 173, 76)
isopod.paste(img, box)
#save the new image to the clipboard
send_to_clipboard(isopod)
