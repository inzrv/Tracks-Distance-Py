import numpy as np

def get_next_point(seg, delta):
    start = seg[0]
    end = seg[1]
    seg_len = np.linalg.norm(start - end)
    if seg_len <= delta:
        return end
    t = delta / seg_len
    x_new = (1 - t) * start[0] + t * end[0]
    y_new = (1 - t) * start[1] + t * end[1]
    return np.array([x_new, y_new], dtype=np.float64)

def split_segment(seg, delta):
    start = seg[0]
    end = seg[1]
    new_points = []
    new_points.append(start)
    cur_point = get_next_point(seg, delta)
    while not np.array_equal(cur_point, end):
        new_points.append(cur_point)
        cur_point = get_next_point([cur_point, end], delta)
    return new_points

def split_track(track, delta):
    splitted_segments = np.empty((0,2))
    for i in range(len(track) - 1):
        seg = [track[i], track[i+1]]
        splitted_segments = np.append(splitted_segments, np.array(split_segment(seg, delta)), axis=0)
    splitted_segments = np.append(splitted_segments, np.array([track[-1]]), axis=0)
    return splitted_segments