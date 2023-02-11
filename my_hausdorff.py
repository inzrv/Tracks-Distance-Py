from sklearn.neighbors import KDTree
import checks
from draw import draw_seg

def max_dst(points_1, points_2, metric):
    tree = KDTree(points_2, leaf_size=2, metric=metric)
    dist, ind = tree.query(points_1)
    return dist.max()

def my_hausdorff_dst(track_1, track_2, metric='euclidean'):
    try:
        checks.check_shapes(track_1, track_2)
        checks.check_types(track_1, track_2)
        checks.check_metric(metric)
    except ValueError as val_e:
        print(str(val_e))
        return 0.0 
    dst_1_to_2 = max_dst(track_1, track_2, metric)
    dst_2_to_1 = max_dst(track_2, track_1, metric)
    return max(dst_1_to_2, dst_2_to_1)

def illustrate_hausdorff(img, track_1, track_2, metric='euclidean'):
    tree = KDTree(track_2, leaf_size=2, metric=metric)
    dist, ind = tree.query(track_1)
    for i in range(len(track_1)):
        start = track_1[i]
        end = track_2[ind[i][0]]
        draw_seg(img, [start, end])
