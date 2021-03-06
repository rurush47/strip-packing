import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

from utils import removeNotNeededHoles
from store import Box, Store

boxes_test = [Box((0,0,1,1)),Box((2,2,1,1))]

# rysuje obok siebie magazyny z listy
def showResults(store_list=[Store(width=10, height=10, boxes=boxes_test)]):
    fig, ax = plt.subplots()
    Path = mpath.Path

    # store_bottom_left_corner
    c = 0

    for store in store_list:
        # draw store
        store_path = path_data = [
            (Path.MOVETO, (0 + c, store.height)),
            (Path.LINETO, (0 + c, 0)),
            (Path.LINETO, (store.width + c, 0)),
            (Path.CLOSEPOLY, (store.width + c, store.height)),
        ]
        codes, verts = zip(*path_data)
        path = mpath.Path(verts, codes)
        x, y = zip(*path.vertices)
        line, = ax.plot(x, y, 'go-')

        # draw boxes
        for box in store.placed_boxes:
            path_data = [
                (Path.MOVETO, (box.x + c, box.y)),
                (Path.LINETO, (box.x + c, box.y + box.h)),
                (Path.LINETO, (box.x + box.w + c, box.y + box.h)),
                (Path.LINETO, (box.x + box.w + c, box.y)),
                (Path.CLOSEPOLY, (box.x + c, box.y)),
            ]
            codes, verts = zip(*path_data)
            path = mpath.Path(verts, codes)
            x, y = zip(*path.vertices)
            line, = ax.plot(x, y, 'go-')

        # draw holes for debug
        #for hole in removeNotNeededHoles(store.boxes, store.holes):
        #    ax.plot(hole[0] + c, hole[1], 'o')

        c += store.width + 10

    ax.grid()
    ax.axis('equal')
    plt.show()
