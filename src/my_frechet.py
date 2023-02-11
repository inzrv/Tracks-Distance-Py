import numpy as np
import checks
from draw import draw_seg

# this function can be further extended
def dst(p1, p2, metric='euclidean'):
    if metric == 'euclidean':
        return np.linalg.norm(p1 - p2)
    return np.linalg.norm(p1 - p2)

def fill_table(table, track_1, track_2, metric):
    table[0][0] = dst(track_1[0], track_2[0], metric)

    for i in range(1, table.shape[0]):
        table[i][0] = max(table[i-1][0], dst(track_1[i], track_2[0], metric))

    for j in range(1, table.shape[1]):
        table[0][j] = max(table[0][j-1], dst(track_1[0], track_2[j], metric))
    
    for i in range(1, table.shape[0]):
        for j in range(1, table.shape[1]):
            table[i][j] = max(min(table[i-1][j], table[i-1][j-1], table[i][j-1]), dst(track_1[i], track_2[j], metric))


def my_frechet_dst(track_1, track_2, metric='euclidean'):
    try:
        checks.check_shapes(track_1, track_2)
        checks.check_types(track_1, track_2)
        checks.check_metric(metric)
    except ValueError as val_e:
        print(str(val_e))
        return 0.0
    table = np.full((track_1.shape[0], track_2.shape[0]), -1.0)
    fill_table(table, track_1, track_2, metric)
    return table[-1][-1]

def illustrate_frechet(img, track_1, track_2, metric='euclidean'):
    table = np.full((track_1.shape[0], track_2.shape[0]), -1.0)
    fill_table(table, track_1, track_2, metric)

    i = track_1.shape[0] - 1
    j = track_2.shape[0] - 1

    while i > -1 and j > -1:
        seg = [track_1[i], track_2[j]]
        if i == 0 and j == 0:
            draw_seg(img, seg)
            break
        elif i == 0 and j > 0:
            if dst(track_1[i], track_2[j]) > table[i][j-1]:
                draw_seg(img, seg)
            j -= 1
        elif i > 0 and j == 0:
            if dst(track_1[i], track_2[j]) > table[i-1][j]:
                draw_seg(img, seg)
            i -= 1
        else:
            min_prev = min(table[i-1][j], table[i-1][j-1], table[i][j-1])
            if dst(track_1[i], track_2[j]) > min_prev:
                draw_seg(img, seg)
            if min_prev == table[i-1][j]:
                i-=1
            elif min_prev == table[i][j-1]:
                j-=1
            else:
                i-=1
                j-=1
