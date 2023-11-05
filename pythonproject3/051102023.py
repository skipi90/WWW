from PIL import Image
import numpy as np
from PIL import ImageChops
from PIL import Imagestat as stat
import matplotlib.pyplot as plt
from random import randint

im = Image.open('jesien.jpg')
print("tryb", im.mode)
print("format", im.format)
print("rozmiar", im.size)
h, w = im.size
im


im.save('jesien1.jpg')

im1 = Image.open('jesien1.jpg')
im1.save('jesien2.jpg')

im2 = Image.open('jesien2.jpg')

plt.figure(figsize=(32, 16))
plt.subplot(1,3,1)
plt.imshow(im)
plt.axis('off')
plt.subplot(1,3,2)
plt.imshow(im1)
plt.axis('off')
plt.subplot(1,3,3)
plt.imshow(im2)
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.show()

dif1 = ImageChops.difference(im, im1)
dif2 = ImageChops.difference(im, im2)
dif3 = ImageChops.difference(im1, im2)
#%%
plt.figure(figsize=(32, 16))
plt.subplot(1, 3, 1)
plt.imshow(dif1)
plt.axis('off')
plt.subplot(1, 3, 2)
plt.imshow(dif2)
plt.axis('off')
plt.subplot(1, 3, 3)
plt.imshow(dif3)
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.show()


def statystyki(im):
    s = stat.Stat(im)
    print("extrema ", s.extrema)  # max i min
    print("count ", s.count)  # zlicza
    print("mean ", s.mean)  # srednia
    print("median ", s.median)  # mediana
    print("stddev ", s.stddev)  # odchylenie standardowe


# %%
statystyki(dif1)

# %%
hist = dif1.histogram()
p = 0
print(hist[p])
print(hist[256 + p])
print(hist[2 * 256 + p])


# %%
def rysuj_histogram_RGB(obraz):
    hist = obraz.histogram()
    plt.title("histogram  ")
    plt.bar(range(256), hist[:256], color='r', alpha=0.5)
    plt.bar(range(256), hist[256:2 * 256], color='g', alpha=0.4)
    plt.bar(range(256), hist[2 * 256:], color='b', alpha=0.3)
    plt.show()


# %%
rysuj_histogram_RGB(dif1)
# %%
statystyki(dif2)
# %%
hist = dif2.histogram()
p = 0
print(hist[p])
print(hist[256 + p])
print(hist[2 * 256 + p])
# %%
statystyki(dif3)
# %%
hist = dif3.histogram()
p = 0
print(hist[p])
print(hist[256 + p])
print(hist[2 * 256 + p])
# %% md
Propozycje
funkcji
oceny
różnic


# %%
def zlicz_roznice_srednia_RGB(obraz, wsp):  # wsp - współczynnik określający dokładność oceny
    t_obraz = np.asarray(obraz)
    h, w, d = t_obraz.shape
    zlicz = 0
    for i in range(h):
        for j in range(w):
            if np.mean(t_obraz[i, j, :]) > wsp:
                zlicz = zlicz + 1
    procent = zlicz / (h * w)
    return zlicz, procent


def zlicz_roznice_suma_RGB(obraz, wsp):  # wsp - współczynnik określający dokładność oceny
    t_obraz = np.asarray(obraz)
    h, w, d = t_obraz.shape
    zlicz = 0
    for i in range(h):
        for j in range(w):
            if sum(t_obraz[i, j, :]) > wsp:  # poniżej równoważne sformułowania tego warunku
                # if (t_obraz[i, j, 0] + t_obraz[i, j, 1] + t_obraz[i, j, 2]) > wsp:
                # if t_obraz[i, j, 0] > wsp or  t_obraz[i, j, 1] > wsp or t_obraz[i, j, 2] > wsp:
                zlicz = zlicz + 1
    procent = zlicz / (h * w)
    return zlicz, procent


# %%
wsp = 10
zlicz, procent = zlicz_roznice_srednia_RGB(dif3, wsp)
print('liczba niepasujących pikseli = ', zlicz)
print('procent niepasujących pikseli = ', procent)
zlicz1, procent1 = zlicz_roznice_suma_RGB(dif3, wsp)
print('liczba niepasujących pikseli = ', zlicz1)
print('procent niepasujących pikseli = ', procent1)
# %% md
Ukrywanie
informacji
w
obrazie
# %%
im_kod = Image.open('kod.bmp')


# %%
def ukryj_kod(obraz, im_kod):
    t_obraz = np.asarray(obraz)
    t_kodowany = t_obraz.copy()
    h, w, d = t_obraz.shape
    t_kod = np.asarray(im_kod)
    for i in range(h):
        for j in range(w):
            if t_kod[i, j] > 0:
                k = randint(0, 2)
                t_kodowany[i, j, k] = t_obraz[i, j, k] + 1
    return Image.fromarray(t_kodowany)


# %%
im_kodowany = ukryj_kod(im, im_kod)
im_kodowany
# %% md
Próba
odkrycia
kodu
z
użyciem
ImageChops.difference(nieskuteczna)
# %%
odkodowany = ImageChops.difference(im, im_kodowany)
odkodowany