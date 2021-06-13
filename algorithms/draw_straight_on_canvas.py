def draw(size, coords):
    draw_vertical = [-1] * len(coords)
    draw_horizontal = [-1] * len(coords)
    for i, coord in enumerate(coords):
        if coord[0][1] == coord[1][1]:
            draw_vertical[i] = coord[1][1]
        if coord[0][0] == coord[1][0]:
            draw_horizontal[i] = coord[0][0]
    canvas = [ ["O" for j in range(size) ] for i in range(size) ]
    for coor_index, coor_axe in filter(lambda x: x[1] > -1, enumerate(draw_vertical)):
        for point in range(coords[coor_index][0][0], coords[coor_index][1][0] + 1):
            canvas[point][coor_axe] = "X"
    for coor_index, coor_axe in filter(lambda x: x[1] > -1, enumerate(draw_horizontal)):
        for point in range(coords[coor_index][0][1], coords[coor_index][1][1] + 1):
            canvas[coor_axe][point] = "X"

    for i in range(size):
        for j in range(size):
            print(canvas[i][j], end = '')
        print("\n", end='')


draw(10, [ [[0,0],[3,0]] , [[2,5],[2,9]], ])
