import sys


def tree_top_tree_house(values):
    row = len(values)
    col = len(values[0])
    
    # transverse the nodes to select visible trees within the trees
    def transverse(values, cr, cc, tc, tr):
        if cr < 0 or cr > tr or cc < 0 or cc > tc:
            return 0, 0

        # return 1 if it's an edge
        if cr == 0 or cr == tr or cc == 0 or cc == tc:
            t = transverse(values, cr , cc+1, tc, tr)
            return 1+t[0], t[1]

        r_idx = cc+1
        l_idx = cc-1
        t_idx = cr-1
        b_idx = cr+1

        current = values[cr][cc]

        right_count = 0 
        right_visible = True
        for x in range(r_idx, col):  # Checking to the right
            if current <= values[cr][x]:
                right_visible = False
                right_count += 1 
                break  
            else:
                right_count += 1 
       
        left_count = 0
        left_visible = True
        for x in range(l_idx, -1, -1):  # Checking to the left
            if current <= values[cr][x]:
                left_visible = False
                left_count += 1 
                break  
            else:
                left_count += 1 

        
        top_count = 0
        top_visible = True
        for y in range(t_idx, -1, -1):  # Checking to the top
            if current <= values[y][cc]:
                top_visible = False
                top_count += 1 
                break  
            else:
                top_count += 1 

       
        bottom_count = 0
        bottom_visible = True
        for y in range(b_idx, row):  # Checking to the bottom
            if current <= values[y][cc]:
                bottom_visible = False
                bottom_count += 1 
                break  
            else:
                bottom_count += 1
        
        scenic_score = left_count * right_count * top_count * bottom_count

        if right_visible or top_visible or left_visible or bottom_visible: 
            t = transverse(values, cr , cc+1, tc, tr)
            return 1+t[0], max(scenic_score, t[1])

        t = transverse(values, cr , cc+1, tc, tr)
        return t[0], max(scenic_score, t[1])

    tc = col-1
    tr = row-1
    cc = 0
    count = 0
    scenic_score = 0
    for cr in range(0, row):
        t = transverse(values, cr ,cc, tc, tr)
        count += t[0]
        scenic_score = max(t[1], scenic_score)

    return count, scenic_score

if __name__ == "__main__":
    for path in sys.argv[1:]:
        with open(path) as file:
            v = file.read().splitlines()
            print(tree_top_tree_house(v))

