from functions import *

print(80*'#')
print('\t\t\t\tDETECTOR COLOR')
print(80*'#')
print('\n\n')

type_src = input('Escolha o tipo de fonte para fazer a detecção:\n\n 1 - Imagem\n 2 - Webcam\n\n Digite 1 ou 2: ')
number_color = input('Escolha a cor para detectar:\n\n 1 - Azul\n 2 - Vermelho\n 3 - Verde\n 4 - Amarelo'
                     '\n\nDigite sua escolha: ')

if type_src == '1':
    img_input = input('Digite o nome da imagem e sua extensão: ')
    img = read_image(img_input)
    mask = detect_color(img,number_color)
    src_color_detect = apply_mask(img,type_src,mask)
    print('Digite "q" para sair do script')
    show_images(img,src_color_detect)

else:
    webcam(number_color)

    
    


