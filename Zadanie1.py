#Модифицируйте программу из практики 7.3 (7 лабораторная работа ) или создайте заново: обработать любой операцией все картинки в заданной папке,
# используя для обхода файлов в папке модуль os (или Pathlib). При этом каталог для итоговых (обработанных) изображений должен тоже создаваться с
# помощью модуля os или Pathlib.
from PIL import Image, ImageFilter
import os

input_folder = 'C:/Users/AlexSash/Downloads/privet'
output_folder = 'images_laba'
os.makedirs(output_folder, exist_ok=True)
filter = ImageFilter.CONTOUR
for filename in os.listdir(input_folder):
    if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith(
            '.png'):
        input_file = os.path.join(input_folder, filename)
        output_file = os.path.join(output_folder, f'countoured_{filename}')

        with Image.open(input_file) as img:
            processed_img = img.filter(filter)
            processed_img.save(output_file)

print("Изображения сохранены в папке images_laba.")
