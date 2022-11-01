import random
def create_grid(x,y):
    grid_list = list()
    for j in range(y):
        k=list()
        for i in range(x):
            k.append(0)
        grid_list.append(k)
    return grid_list

def place_mine(grid_list):
    global bomb_have
    bomb_have=int(input('Number of mine(s): '))
    bomb_plant = 0
    while bomb_plant != bomb_have:
        pos_x,pos_y = random.randint(0,len(grid_list[0])-1),random.randint(0,len(grid_list)-1)
        if grid_list[pos_y][pos_x] != 'X':
            grid_list[pos_y][pos_x] = 'X'
            bomb_plant+=1
            max_y,low_y =  pos_y+1,pos_y-1
            max_x,low_x = pos_x+1,pos_x-1      
            for j in range(len(grid_list)):
                for i in range(len(grid_list[0])):
                    if i in range(low_x,max_x+1) and j in range(low_y,max_y+1):
                        if grid_list[j][i]!='X':
                            grid_list[j][i] +=1
    return grid_list

def print_result():
    for i in range(len(grid_list[0])):
        print(f' X{i}',end='')
    print('')
    box_remain = 0
    for i in range(len(grid_list)):
        row = [str(j) for j in grid_list[i]]
        print('',end=' ')
        for box in range(len(row)):
            pos_x,pos_y = box,i
            if (pos_x,pos_y) in is_open:
                if box<=10:
                    print(' ' + row[box],end=' ')
                else:
                    print(' '*2 + row[box],end=' ')
            else:
                if box<=10:
                    print(' ' + '?',end=' ')
                    box_remain += 1
                else:
                    print(' '*2 + '?',end=' ')
                    box_remain += 1
            if box == len(row)-1:
                print(f'Y{i}',end='\n')
    print('box_remain :',box_remain)
    print('bomb_have :',bomb_have)
    if box_remain == bomb_have:
        return True
    else:
        return False

def select_box(pos_x,pos_y):
    box_select = grid_list[pos_y][pos_x]
    if box_select == 'X':
        return True
    else:
        if box_select == 0:
            open_close(pos_x,pos_y)
        else:
            is_open.append((pos_x,pos_y))
        return False

def open_close(pos_x,pos_y):
    try:
        grid_list[pos_y][pos_x]
        if grid_list[pos_y][pos_x] != 0 or grid_list[pos_y][pos_x] == 'X' or (pos_x,pos_y) in is_open:
            if not((pos_x,pos_y) in is_open) and grid_list[pos_y][pos_x] != 'X':
                is_open.append((pos_x,pos_y))
            return
        else:
            is_open.append((pos_x,pos_y))
            li1 = list(range(pos_x-1,pos_x+2))
            li2 = list(range(pos_y-1,pos_y+2))
            all_pos = [(x,y) for x in li1 for y in li2]
            for pos in all_pos:
                po_x,po_y = pos
                open_close(po_x,po_y)
    except:
        return

def main():
    global is_open,grid_list
    x,y = input('Grid Size: ').split(' ')
    x,y = int(x),int(y)
    grid_list = create_grid(x,y)
    grid_list = place_mine(grid_list)
    is_open = []
    while True:
        result_ = print_result()
        if result_:
            print('You Win!!')
            break
        else:
            se_x,se_y = input('Select Your Box: ').split(' ')
            se_x,se_y = int(se_x),int(se_y)
            if (se_x,se_y) == (-1,-1):
                break
            elif (se_x,se_y) in is_open:
                print('It already open please select again!!')
            else:
                isDead = select_box(se_x,se_y)
                if isDead:
                    print('You Dead!!')
                    break

def main_menu():
    print('Welcome to Minesweep!!!')
    print('To Start Type : 1')
    print('To Exit Type 2')
    op = input('Type : ')
    if op == '1':
        main()
    elif op == '2':
        pass

main_menu()
