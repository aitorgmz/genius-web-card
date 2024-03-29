import base64

import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

white = (255, 255, 255)
black = (0, 0, 0)
line_count = 0

def createImage(base_64, song_text, song_autor, song_name, is_local_file):
    global line_count
    encoded_data = str(base_64)
    if is_local_file == True:
        encoded_data = base_64.split(',')[1]
    nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    cv2_img_array = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    width, height, channels = img.shape

    pillow_font_programme = ImageFont.truetype("C:\\Users\\Aitor\\Desktop\\Programme.ttf", int(0.043*width))
    pillow_font_georgia = ImageFont.truetype("C:\\Users\\Aitor\\Desktop\\Georgia.ttf", int(0.1*width))

    #default values for both left and top margin
    margin_x = 0.048*width
    line_height = width*0.063

    song_text_lines_array = song_text.splitlines()
    song_text_array = []
    line_length = 0
    line_text = ""
    for line in song_text_lines_array:
        if len(line) > 40:
            line_words = line.split(" ")
            for word in line_words:
                if line_length + len(word) < 36:
                    if line_text != "" :
                        line_text = line_text + " " + word
                    else:
                        line_text = word
                    line_length += len(word)
                else:
                    line_text = line_text + " "
                    song_text_array.append(line_text)
                    line_text = word
                    line_length = len(word)
            line_text = line_text + " "
            song_text_array.append(line_text)
            line_text = ""
            line_length = 0
        else:
            song_text_array.append(line)

    if len(song_text_array) <= 2:
        pos_y = (height - (height * 0.26))
    elif len(song_text_array) <= 4:
        pos_y = (height-(height*0.36))
    elif len(song_text_array) <= 6:
        pos_y = (height-(height*0.42))
    elif len(song_text_array) <= 8:
        pos_y = (height-(height*0.60))
    elif len(song_text_array) <= 10:
        pos_y = (height-(height*0.70))
    else:
        pos_y = (height-(height*0.85))

    for i,line in enumerate(song_text_array):
        cv2_img_array = write_text_with_background(cv2_img_array, line, "#000", "#FFF", pillow_font_programme,
                                                 2*margin_x, pos_y + (line_height*line_count))
    cv2_img_array = write_text_no_background(cv2_img_array,  song_autor.lstrip() + " \"" + song_name + "\"", pillow_font_programme,
                                             2*margin_x, pos_y+(line_height*line_count))
    cv2_img_array = write_text_no_background(cv2_img_array, "“", pillow_font_georgia,
                                             margin_x, pos_y - (width*0.03))

    if line_count % 2 == 0:
        cv2_img_array = cv2.cvtColor(cv2_img_array, cv2.COLOR_RGB2BGR)
    _, buffer = cv2.imencode('.jpg', cv2_img_array)
    line_count = 0
    return base64.b64encode(buffer).decode('ascii')


def write_text_with_background(cv2_image_array,text, text_color, bg_color, font, pos_x, pos_y):
    global line_count
    pillow_image = Image.fromarray(cv2_image_array)
    pillow_draw_type = ImageDraw.Draw(pillow_image)
    text_pos_x, text_pos_y = get_text_dimensions(text, font)
    pillow_draw_type.rectangle([(pos_x - 5, pos_y),(pos_x + text_pos_x + 8, pos_y + text_pos_y)],
                               fill=bg_color)
    pillow_draw_type.text((pos_x, pos_y), text, font=font, fill=text_color)
    cv2_image_array = cv2.cvtColor(np.array(pillow_image), cv2.COLOR_RGB2BGR)
    line_count+=1
    return cv2_image_array

def write_text_no_background(cv2_image_array, text, font, pos_x, pos_y):
    global line_count
    pillow_image = Image.fromarray(cv2_image_array)
    pillow_draw_type = ImageDraw.Draw(pillow_image)
    pillow_draw_type.text((pos_x, pos_y), text, font=font, fill="#FFF")
    cv2_image_array = cv2.cvtColor(np.array(pillow_image), cv2.COLOR_RGB2BGR)
    line_count+=1
    return cv2_image_array

def get_text_dimensions(text_string, font):
    ascent, descent = font.getmetrics()

    text_width = font.getmask(text_string).getbbox()[2]
    text_height = font.getmask(text_string).getbbox()[3] + descent

    return (text_width, text_height)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    createImage("C:\\Users\\Aitor\\Desktop\\surimi.jpg","Yo te cojo y te mato y te mando al carajo",
                "Space Surimi", "Romantic Bogavantic")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/