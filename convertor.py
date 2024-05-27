import os
import cv2
import numpy as np

# Указать здесь путь до test набора
path_to_dir = r"test_rucode"

# Получение списка всех файлов в директории
files = os.listdir(path_to_dir)

print(files)
print(len(files))
prefix = 'public_test'
filenames = [f'{prefix}_{i}.png' for i in range(1, 785)]
#
# В test наборах должно быть 707 изображений, проверим это
assert len(files) == 784, f'Length of test set is {len(files)} not equal 707! Please check test images'
#
# # Функция для чтения изображения и преобразования его в тензор
def read_image_as_tensor(file_path):
    # Чтение изображения с помощью OpenCV
    print(file_path)
    image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    # Преобразование в тензор numpy

    tensor = np.array(image, dtype=np.bool_)

    return tensor
#
# # Список для хранения тензоров
tensor_list = []
#
# # Чтение и преобразование каждого изображения в тензор и добавление его в список
for filename in filenames:
  file_path = os.path.join(path_to_dir, filename)
  tensor = read_image_as_tensor(file_path)
  tensor_list.append(tensor)

#
# Преобразование списка тензоров в тензор numpy
tensor_array = np.array(tensor_list)
#
# # Печать размерности полученного тензора. Проверьте, что количество количество снимков совпадает с количеством полученных тензоров маски
print("Размерность тензора:", tensor_array.shape)
#
# # Размер тензора должен быть равен (707, 256, 256)
assert tensor_array.shape == (784, 256, 256), "Please check path to images"
#
output_file = "solution.npy"
#
# # Сохранение тензорного массива в файл .npy
np.save(output_file, tensor_array)