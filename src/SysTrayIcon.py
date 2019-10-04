from pystray import Icon as Icon, Menu as Menu, MenuItem as Item
from PIL import Image, ImageDraw

autoskip = False

autoskip = 0


def set_state(v):
    def inner(icon, item):
        global autoskip
        state = v

    return inner


def get_state(v):
    def inner(item):
        return autoskip == v

    return inner


def create_image(bgcolor):
    width = 64
    height = 64
    color1 = bgcolor
    color2 = "BLACK"
    # Generate an image and draw a pattern
    image = Image.new('RGB', (width, height), color1)
    dc = ImageDraw.Draw(image)
    dc.rectangle(
        (width // 2 - width // 16, height - (height // 8) * 2, width // 2, height // 8),
        fill=color2)
    dc.ellipse(
        (width // 8, height*3//5, width // 2, height - height//8),
        fill=color2)
    dc.chord(
        (width // 2 - width // 3, height // 8, width * 3 // 4, height*4//5),
        280,
        20,
        fill=color2)

    return image