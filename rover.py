matrix=[[0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,'N',0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]]

curr_D = 'N'

def print_matrix():
    for i in matrix:
        print(*i)
        
def north():
    for i in matrix:
        if curr_D in i:
            cur_list = matrix.index(i)
            if not cur_list <= 0:
                cur_pos = i.index(curr_D)
                matrix[cur_list][cur_pos] = 0
                matrix[cur_list-1][cur_pos] = curr_D
                print_matrix()
                break
            else:
                print("wall ahead")
                break

def south():
    for i in matrix:
        if curr_D in i:
            cur_list = matrix.index(i)
            if not cur_list >= len(matrix)-1:
                cur_pos = i.index(curr_D)
                matrix[cur_list][cur_pos] = 0
                matrix[cur_list+1][cur_pos] = curr_D
                print_matrix()
                break
            else:
                print("wall ahead")
                break

def east():
    for i in matrix:
        if curr_D in i:
            cur_list = matrix.index(i)
            cur_pos = i.index(curr_D)
            if not cur_pos >= len(i)-1:
                matrix[cur_list][cur_pos] = 0
                matrix[cur_list][cur_pos+1] = curr_D
                print_matrix()
                break
            else:
                print("wall ahead")
                break

def west():
    for i in matrix:
        if curr_D in i:
            cur_list = matrix.index(i)
            cur_pos = i.index(curr_D)
            if not cur_pos <= 0:
                matrix[cur_list][cur_pos] = 0
                matrix[cur_list][cur_pos-1] = curr_D
                print_matrix()
                break
            else:
                print("wall ahead")
                break

def rotate(LR):
    directions = ('N','E','S','W')
    if LR == 'R':
        curr_pos = directions.index(curr_D)
        if not curr_pos >= len(directions)-1:
            return directions[curr_pos+1]
        else:
            return directions[0]
    if LR == 'L':
        curr_pos = directions.index(curr_D)
        if not curr_pos <= 0:
            return directions[curr_pos-1]
        else:
            return directions[len(directions)-1]

def change_direction(curr_d,D):
    for i in matrix:
        if curr_d in i:
            cur_list = matrix.index(i)
            cur_pos = i.index(curr_d)
            matrix[cur_list][cur_pos] = D
            print_matrix()
            return D
    

print_matrix()
print('')
#change_direction('W')
while True:
    print("current direction:"+curr_D)
    command = input("Enter command:")
    if command == 'M':
        if curr_D == 'N':
            north()
        if curr_D == 'E':
            east()
        if curr_D == 'S':
            south()
        if curr_D == 'W':
            west()
    elif command == 'L':
        curr_D = change_direction(curr_D,rotate('L'))
    elif command == 'R':
        curr_D = change_direction(curr_D,rotate('R'))
    else:
        "Enter right command"
    print("")
