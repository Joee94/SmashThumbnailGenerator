from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from Tkinter import Tk
from tkFileDialog import askopenfilename

def resizeImage(image, percent):
    width, height = image.size
    print (width)
    print (height)
    print percent
    newWidth = width * (percent / 100)
    newHeight = height * (percent / 100)
    print(newWidth)
    print(newHeight)
    return image.resize((int(newWidth), int(newHeight)), Image.LANCZOS)

def addCharactersToForeground(background, image1, image2):
    background.paste(image1, (-100, 0), image1)
    background.paste(image2, (750, 0), image2)

    return background

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
backgroundLocation = askopenfilename() # show an "Open" dialog box and return the path to the selected file
overlay = askopenfilename() # show an "Open" dialog box and return the path to the selected file

background = Image.open(backgroundLocation)
background = background.convert("RGBA")
overlay = Image.open(overlay)


with open("data.txt") as f:
    for line in f:
        line = [x.strip() for x in line.split(',')]
        background = Image.open(backgroundLocation)
        foreground = Image.open(line[1].lower() + ".png")
        foreground2 = Image.open(line[3].lower() + ".png")
        foreground = resizeImage(foreground, 50.0)
        foreground2 = resizeImage(foreground2, 50.0)
        background = addCharactersToForeground(background, foreground, foreground2)
        background.paste(overlay, (0, 0), overlay)

        draw = ImageDraw.Draw(background)
        # font = ImageFont.truetype(<font-file>, <font-size>)
        fontsize = 1  # starting font size
        font = ImageFont.truetype("Arial.ttf", fontsize)
        while font.getsize(line[0])[0] < 300:
            # iterate until the text size is just larger than the criteria
            fontsize += 1
            font = ImageFont.truetype("arial.ttf", fontsize)
        # draw.text((x, y),"Sample Text",(r,g,b))
        draw.text((100, 450 + (200-font.getsize(line[0])[1])),line[0],(0,0,0),font=font)

        fontsize = 1  # starting font size
        while font.getsize(line[2])[0] < 300:
            # iterate until the text size is just larger than the criteria
            fontsize += 1
            font = ImageFont.truetype("arial.ttf", fontsize)

        draw.text((850, 450 + (200-font.getsize(line[2])[1])),line[2],(0,0,0),font=font, align="right")
        background.save('thumbnails/' + line[0] + '.png')

        print font.getsize(line[0])

    #Image.alpha_composite(background, foreground).save("test3.png")