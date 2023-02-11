import cv2
import numpy as np
from matplotlib import pyplot as plt

nice_white= (245, 245, 245)
nice_red = (60, 20, 220)
nice_blue = (225, 105, 65)
nice_green = (50, 205, 154)
nice_pink = (147, 20, 255)

colors_for_tracks = [nice_white, nice_blue, nice_red, nice_green]

def get_rand_color():
    return (np.random.choice(range(255),size=3))

def draw_track(img, track, color=nice_white):
    track_int = np.array(track, dtype=np.int64)
    img = cv2.polylines(img, [track_int], False, color, 2)
    for point in track_int:
        img = cv2.circle(img, point,  5, color, -1)
    return img

def draw_tracks(img, tracks):
    for i in range(len(tracks)):
        color = (0, 0, 0)
        if i < 4:
            color = colors_for_tracks[i]
        else:
            color = get_rand_color()
        img = draw_track(img, tracks[i], color)
    return img

def draw_seg(img, seg, color=nice_red):
    start = np.array(seg[0], dtype=np.int64)
    end = np.array(seg[1], dtype=np.int64)
    img = cv2.line(img, start, end, color, 1)
    return img    
    
def show_img(img, size=(18, 12)):
    fig, ax = plt.subplots()
    w, h = size
    fig.set_size_inches(w, h)
    ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()