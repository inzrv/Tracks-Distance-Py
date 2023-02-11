import numpy as np
import checks
from draw import draw_seg

# this function can be further extended
def dst(p1, p2, metric='euclidean'):
    if metric == 'euclidean':
        return np.linalg.norm(p1 - p2)
    return np.linalg.norm(p1 - p2)


def my_naive_dst(track_1, track_2, metric='euclidean'):
    try:
        checks.check_shapes(track_1, track_2)
        checks.check_types(track_1, track_2)
        checks.check_metric(metric)
    except ValueError as val_e:
        print(str(val_e))
        return 0.0

    diff = abs(track_1.shape[0] - track_2.shape[0])
    track_1_aligned = track_1
    track_2_aligned = track_2

    if track_1.shape[0] > track_2.shape[0]:
        extra = np.full((diff, 2), track_2[-1])
        track_2_aligned = np.append(track_2, extra, axis=0)
    elif track_2.shape[0] > track_1.shape[0]:
        extra = np.full((diff, 2), track_1[-1])
        track_1_aligned = np.append(track_1, extra, axis=0)

    tracks_len = track_1_aligned.shape[0]
    dst_arr = np.zeros((tracks_len, ), dtype=np.float64) 
    for i in range(tracks_len):
        dst_arr[i] = dst(track_1_aligned[i], track_2_aligned[i], metric)
    return np.max(dst_arr)


def illustrate_naive(img, track_1, track_2):
    diff = abs(track_1.shape[0] - track_2.shape[0])
    track_1_aligned = track_1
    track_2_aligned = track_2

    if track_1.shape[0] > track_2.shape[0]:
        extra = np.full((diff, 2), track_2[-1])
        track_2_aligned = np.append(track_2, extra, axis=0)
    elif track_2.shape[0] > track_1.shape[0]:
        extra = np.full((diff, 2), track_1[-1])
        track_1_aligned = np.append(track_1, extra, axis=0)

    tracks_len = track_1_aligned.shape[0]
    for i in range(tracks_len):
        start = track_1_aligned[i]
        end = track_2_aligned[i]
        img = draw_seg(img, [start, end])
    return img