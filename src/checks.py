import numpy as np

def check_shapes(track_1, track_2):
    shape_1 = track_1.shape
    shape_2 = track_2.shape
    if shape_1[0] < 1 or shape_2[0] < 1:
        raise ValueError('tracks must be non-empty arrays')
    if len(shape_1) != 2 or len(shape_2) != 2:
        raise ValueError('tracks must be 2-dimensional')
    if shape_1[1] != 2 or shape_2[1] != 2:
        raise ValueError('points must have two coordinates')
    
def check_types(track_1, track_2):
    if not isinstance(track_1, np.ndarray) or not isinstance(track_2, np.ndarray):
        raise ValueError('arrays must be of type numpy.ndarray')
    if not np.issubdtype(track_1.dtype, np.number) or not np.issubdtype(track_2.dtype, np.number):
        raise ValueError('the arrays data type must be numeric')

def check_metric(metric):
    if metric != 'euclidean':
        raise ValueError('wrong metric')