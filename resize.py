import cv2

src = input('введите путь до изображения: ')
image = cv2.imread(src)
if (image == None):
    print('Ошбика в пути, принято стандартное изображение')
    image = cv2.imread('s1200.jpg')
try:
    k = float(input('Введите коэффициент маштабирования: '))
except:
    k = 1
    print('некорректное значение k принят как 1')
dim = (int(image.shape[1]*k), int(image.shape[0]*k))
print('До: \nВысота: %d, Ширина: %d, Глубина: %d ' % image.shape)

image = cv2.resize(image, dim , interpolation = cv2.INTER_AREA)

print('После: \nВысота: %d, Ширина: %d, Глубина: %d ' % image.shape)

cv2.imshow('my_bike', image)
cv2.imwrite("new_image.jpg", image)

print('Файл с новым изображение сохранен под именем new_image.jpg')

cv2.waitKey(0)
