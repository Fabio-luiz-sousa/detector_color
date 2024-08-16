import os
import cv2
import numpy as np
from PIL import Image


# função que lê a imagem
def read_image(image):
    image_path = os.path.join('.','assets')
    img = cv2.imread(image_path+f'/{image}')
    return img

# função que exibe as imagens
def show_images(img,img_color_detect) -> None:
    cv2.imshow('img',img)
    cv2.imshow('img_color_detect',img_color_detect)
    cv2.waitKey(0)

# função que cria a mascara
def detect_color(src,number_color:str):
    src_hsv = cv2.cvtColor(src,cv2.COLOR_BGR2HSV)

    dict_colors = {
        'blue' : [255,0,0],
        'red' : [0,0,255],
        'green' : [0,255,0],
        'yellow' : [0,255,255]
    }
    # Função que cria os limites para a mascara
    def get_limits(color_choice: dict)-> tuple[np.uint8, np.uint8]:
        color = np.uint8([[color_choice]])
        color_hsv = cv2.cvtColor(color,cv2.COLOR_BGR2HSV)

    
        if color_hsv[0][0][0] > 0:
            lw_limmit = color_hsv[0][0][0] - 10,150,150
            up_limmit = color_hsv[0][0][0] + 10,255,255
        else:
            lw_limmit = color_hsv[0][0][0] + 0,150,150
            up_limmit = color_hsv[0][0][0] + 10,255,255

        lw_limmit = np.array(lw_limmit,dtype=np.uint8)
        up_limmit = np.array(up_limmit,dtype=np.uint8)

        return lw_limmit,up_limmit

    match number_color:
        case '1':
            lw_limmit,up_limmit = get_limits(dict_colors['blue'])
            mask = cv2.inRange(src_hsv,lw_limmit,up_limmit)
        case '2':
            lw_limmit,up_limmit = get_limits(dict_colors['red'])
            mask = cv2.inRange(src_hsv,lw_limmit,up_limmit)
        case '3':
            lw_limmit,up_limmit = get_limits(dict_colors['green'])
            mask = cv2.inRange(src_hsv,lw_limmit,up_limmit)
        case '4':
            lw_limmit,up_limmit = get_limits(dict_colors['yellow'])
            mask = cv2.inRange(src_hsv,lw_limmit,up_limmit)
    return mask

# função que aplica a mascara 
def apply_mask(src,type_src:str, mask):
    src_color_detect = src
    if type_src == '1':
        src_color_detect = cv2.bitwise_and(src,src,mask=mask)

    else:
        mask_ = Image.fromarray(mask)

        bbox = mask_.getbbox()

        if bbox is not None:
            x1, y1, x2, y2 = bbox
            src_color_detect = cv2.rectangle(src,(x1,y1),(x2,y2),(0,0,0),3)
    return src_color_detect
    
    
# função que aciona a webcam
def webcam(number_color:str)->None:

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        mask = detect_color(frame,number_color) 
        frame_detect_color = apply_mask(frame,'2',mask)
        cv2.imshow('webcam',frame_detect_color)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

