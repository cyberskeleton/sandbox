def segment(x, y):
    if x != y:
        bool = False
    else:
        bool = True
    return x, y, bool


def segmempty(segment, emptiness):
    if emptiness == False:
        emptiness = True
    return segment[0], segment[1], emptiness


def isempty(segment):
    return segment[2]



def intersept(segment1, segment2):
    min1 = min(segment1[0], segment1[1])
    max1 = max(segment1[0], segment1[1])
    min2 = min(segment2[0], segment2[1])
    max2 = max(segment2[0], segment2[1])
    if max1 < min2 or max2 < min1:
        return 0, 0, True
    if min1 > min2:
        minseg = min1
    else:
        minseg = min2
    if max1 < max2:
        maxseg = max1
    else:
        maxseg = max2
    return minseg, maxseg, False
