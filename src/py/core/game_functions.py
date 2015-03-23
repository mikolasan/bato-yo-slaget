import random
import copy

from ship_classes import *



def fence_in(x_l, y_l, mat):
    for i in x_l:
        for c in y_l:
            if (c+1) in range(len(mat)) and (i+1) in range(len(mat[0])):
                mat[i+1][c+1] = '5'
                
            if c-1 in range(len(mat)) and i-1 in range(len(mat[0])):
                mat[i-1][c-1] = '5'
                
            if c-1 in range(len(mat)) and i+1 in range(len(mat[0])):
                mat[i+1][c-1] = '5'
                
            if c+1 in range(len(mat)) and i-1 in range(len(mat[0])):
                mat[i-1][c+1] = '5'
                
            if c+1 in range(len(mat)) and i in range(len(mat[0])):
                mat[i][c+1] = '5'

            if c-1 in range(len(mat)) and i in range(len(mat[0])):
                mat[i][c-1] = '5'
                
            if c in range(len(mat)) and i-1 in range(len(mat[0])):
                mat[i-1][c] = '5'
                    
            if c in range(len(mat)) and i+1 in range(len(mat[0])):
                mat[i+1][c] = '5'
            
    for u in range(len(x_l)):        
        mat[x_l[u]][y_l[u]] = '1'


def ship4(mat):
    x1 = random.randrange(10)
    y1 = random.randrange(10)

    rand = random.randrange(4)
    if rand == 0:
        y2 = y1
        y3 = y1
        y4 = y1

        
        if x1 <= 6:
            x2 = x1 + 1
            x3 = x1 + 2
            x4 = x1 + 3
            
        elif x1 == 7:
            x2 = x1 + 1
            x3 = x1 + 2
            x4 = x1 -1
            
        elif x1 == 8:
            x2 = x1 + 1
            x3 = x1 - 1
            x4 = x1 - 2
            
        elif x1 == 9:
            x2 = x1 - 1
            x3 = x1 - 2
            x4 = x1 - 3


    elif rand == 1:
        y2 = y1
        y3 = y1
        y4 = y1

        if x1 >= 3:
            x2 = x1 - 1
            x3 = x1 - 2
            x4 = x1 - 3
            
        elif x1 == 2:
            x2 = x1 - 1
            x3 = x1 - 2
            x4 = x1 + 1

        elif x1 == 1:
            x2 = x1 - 1
            x3 = x1 + 1
            x4 = x1 + 2

        elif x1 == 0:
            x2 = x1 + 1
            x3 = x1 + 2
            x4 = x1 + 3
            
            
        

        
    elif rand == 2:
        x2 = x1
        x3 = x1
        x4 = x1

        if y1 <=6:
            y2 = y1 + 1
            y3 = y1 + 2
            y4 = y1 + 3
            
        elif y1 == 7:
            y2 = y1 + 1
            y3 = y1 + 2
            y4 = y1 -1
            
        elif y1 == 8:
            y2 = y1 + 1
            y3 = y1 - 1
            y4 = y1 - 2
            
        elif y1 == 9:
            y2 = y1 - 1
            y3 = y1 - 2
            y4 = y1 - 3
        
    else:
        x2 = x1
        x3 = x1
        x4 = x1

        if y1 >= 3:
            y2 = y1 - 1
            y3 = y1 - 2
            y4 = y1 - 3
            
        elif y1 == 2:
            y2 = y1 - 1
            y3 = y1 - 2
            y4 = y1 + 1

        elif y1 == 1:
            y2 = y1 - 1
            y3 = y1 + 1
            y4 = y1 + 2

        elif y1 == 0:
            y2 = y1 + 1
            y3 = y1 + 2
            y4 = y1 + 3


    fence_in([x1,x2,x3,x4],[y1,y2,y3,y4], mat)




def ship3(mat):
    x1 = random.randrange(10)
    y1 = random.randrange(10)
    x2 = 0
    x3=0
    y2=0
    y3=0


    while mat[x1][y1] == '5' or mat[x1][y1] == '1' :
        x1 = random.randrange(10)
        y1 = random.randrange(10)
        

    rand = random.randrange(2)


    if rand == 0:
        y2 = y1
        y3 = y1
    
        if x1+2 in range(9) and y1 in range(9):
            if (mat[x1+1][y1] != '5' and mat[x1+1][y1] != '1') and (mat[x1+2][y1] != '5' and mat[x1+2][y1] != '1'):
                x2 = x1+1
                x3 = x1+2
                fence_in([x1,x2,x3],[y1,y2,y3],mat)
            else:
                rand += 1

                
        elif x1-2 in range(9) and y1 in range(9):
            if (mat[x1-1][y1] != '5' and mat[x1-1][y1] != '1') and (mat[x1-2][y1] != '5' and mat[x1-2][y1] != '1'):
                x2 = x1-1
                x3 = x1-2
                fence_in([x1,x2,x3],[y1,y2,y3],mat)
            else:
                rand += 1
        else:
            rand += 1
        
    if rand == 1:
        x2 = x1
        x3 = x1

        if y1+2 in range(9) and x1 in range(9):
            if (mat[x1][y1+1] != '5' and mat[x1][y1+1] != '1') and (mat[x1][y1+2] != '5' and mat[x1][y1+2] != '1'):
                y2 = y1+1
                y3 = y1+2
                fence_in([x1,x2,x3],[y1,y2,y3],mat)
            else:
                ship3(mat)
                
        elif y1-2 in range(9) and x1 in range(9):
            if (mat[x1][y1-1] != '5' and mat[x1][y1-1] != '1') and (mat[x1][y1-2] != '5' and mat[x1][y1-2] != '1'):
                y2 = y1-1
                y3 = y1-2
                fence_in([x1,x2,x3],[y1,y2,y3],mat)
            else:
                ship3(mat)
            
        else:
            ship3(mat)

    

def ship2(mat):
    x1 = random.randrange(10)
    y1 = random.randrange(10)
    x2 = 0
    y2=0


    while mat[x1][y1] == '5' or mat[x1][y1] == '1' :
        x1 = random.randrange(10)
        y1 = random.randrange(10)
        

    rand = random.randrange(2)


    if rand == 0:
        y2 = y1
    
        if x1+1 in range(9) and y1 in range(9):
            if mat[x1+1][y1] != '5' and mat[x1+1][y1] != '1':
                x2 = x1+1
                fence_in([x1,x2],[y1,y2],mat)
            else:
                rand += 1

                
        elif x1-1 in range(9) and y1 in range(9):
            if mat[x1-1][y1] != '5' and mat[x1-1][y1] != '1':
                x2 = x1-1
                fence_in([x1,x2],[y1,y2],mat)
            else:
                rand += 1
        else:
            rand += 1
        
    if rand == 1:
        x2 = x1

        if y1+1 in range(9) and x1 in range(9):
            if mat[x1][y1+1] != '5' and mat[x1][y1+1] != '1':
                y2 = y1+1
                fence_in([x1,x2],[y1,y2],mat)
            else:
                ship2(mat)
                
        elif y1-1 in range(9) and x1 in range(9):
            if mat[x1][y1-1] != '5' and mat[x1][y1-1] != '1':
                y2 = y1-1
                fence_in([x1,x2],[y1,y2],mat)
            else:
                ship2(mat)
            
        else:
            ship2(mat)

    
        

def ship1(mat):
    x1 = random.randrange(10)
    y1 = random.randrange(10)



    while mat[x1][y1] == '5' or mat[x1][y1] == '1' :
        x1 = random.randrange(10)
        y1 = random.randrange(10)
        
    fence_in([x1],[y1],mat)

      
        
        
def print_board(board):
    for row in board:
        print " ".join(row)

def set_ships(mat):
    ship4(mat)
    for i in range(2):
        ship3(mat)

    for i in range(3):
        ship2(mat)
    for i in range(4):
        ship1(mat)

######################################################################################       

def put_boards(b1, b2, coord_p, coord_cpu, p_cells, cpu_cells):


    x1=y1=21
    for row in b2:
        for col in row:
            if col == '0' or col == '5':
                cell = Cell('c')
                
            elif col == '2':
                cell = Cell('p')
                
            elif col == '1':
                cell = Cell('c')

            cell.rect.x = x1
            cell.rect.y = y1
            cpu_cells.add(cell)
            coord_cpu.append([x1, y1])
                
            x1+=35
                    
        x1 = 21
        y1+=35
        
    y2=291
    x2 = 391
    for row in b1:
        for col in row:
            if col == '0':

                cell = Cell('p')
                cell.rect.x = x2
                cell.rect.y = y2
                p_cells.add(cell)
                coord_p.append([x2, y2])
                
            elif col == '2':
                cell = Cell('c')
                cell.rect.x = x2
                cell.rect.y = y2
                p_cells.add(cell)
                coord_p.append([x2, y2])

    
            y2+=35
        y2 = 291
        x2+=35


def update_boards(screen, b1 ,b2, coord_p, coord_cpu, p_cells, cpu_cells, dam_cells):
    x1=y1=21
    for row in b2:
        for col in row:
            if col == '2':
                for c in cpu_cells:
                    if c.rect.x == x1 and c.rect.y == y1:
                        c.typ = 'p'
                        c.update()
                        

                        
            elif col == '4':
                for c in cpu_cells:
                    if c.rect.x == x1 and c.rect.y == y1:
                        c.typ = 'o'
                        c.update()

            elif col == '9':
                for c in cpu_cells:
                    if c.rect.x == x1 and c.rect.y == y1:
                        c.typ = 'dead'
                        c.update()
                        
            
                    
            x1+=35
        x1 = 21
        y1+=35


        

    y2=291
    x2 = 391
    for row in b1:
        for col in row:
            if col == '9':
                for c in p_cells:
                    if c.rect.x == x2 and c.rect.y == y2:
                        c.typ = 'dead'
                        c.update()
                        dam_cells.add(c)
                        

                
            if col == '2':
                for c in p_cells:
                    if c.rect.x == x2 and c.rect.y == y2:
                        c.typ = 'o'
                        c.update()
                        dam_cells.add(c)


                
            elif col == '8':
                for c in p_cells:
                    if c.rect.x == x2 and c.rect.y == y2:
                        c.typ = 'damaged'
                        c.update()
                        dam_cells.add(c)
                        


            

    
            x2+=35
        x2 = 391
        y2+=35

def ship_coord_check(coord, ships,mat, turn):
    for cell in coord:
        c = coord.index(cell)
        for ship in ships:
            if ship.rect.x + 16 in range(cell[0], cell[0]+32) and ship.rect.y + 16 in range(cell[1], cell[1]+32):
                if turn == 9:
                    if ship.w > ship.h:
                        for i in range(4):
                            mat[c%10][(c//10)+i] = '1'
                    elif ship.w < ship.h:
                        for i in range(4):
                            mat[(c%10)+i][c//10] = '1'
                    
                elif turn == 8 or turn == 7 :
                    if ship.w > ship.h:
                        for i in range(3):
                            mat[c%10][(c//10)+i] = '1'
                    elif ship.w < ship.h:
                        for i in range(3):
                            mat[(c%10)+i][c//10] = '1'

                if turn == 6 or turn == 5 or turn == 4:
                    if ship.w > ship.h:
                        for i in range(2):
                            mat[c%10][(c//10)+i] = '1'
                    elif ship.w < ship.h:
                        for i in range(2):
                            mat[(c%10)+i][c//10] = '1'

                if turn == 3 or turn == 2 or turn == 1 or turn == 0:
                        mat[c%10][c//10] = '1'




def hit_coord_check(coord, aim, mat):
    for cell in coord:
        c = coord.index(cell)
        if aim.rect.x  == cell[0] and aim.rect.y == cell[1]:
            if mat[c//10][c%10] == '1':
                mat[c//10][c%10] = '2'
            
            elif mat[c//10][c%10] == '0' or mat[c//10][c%10] == '5':
                mat[c//10][c%10] = '4'
    kill(mat, '2', '1', '9')
    fence_cpu(mat, '9', '4')

                


def res_check(coord, aim, mat):
    print_board(mat)
    for cell in coord:
        c = coord.index(cell)
        if aim.rect.x  == cell[0] and aim.rect.y == cell[1]:
            if mat[c//10][c%10] == '1':
                return 'hit'
            
            elif mat[c//10][c%10] == '0' or mat[c//10][c%10] == '5':
                return 'miss'
            
            else:
                return 'wrong'
        
    


def finish_him(mat):
    cells = []
    axis = ''
    step = ()
    
    print_board(mat)
    
    for row in mat:
        for col in row:
            cells.append(col)
    if '8' in cells:
        for row in mat:
            for col in row:
                if col == '8':
                    x_in = row.index(col)
                    y_in = mat.index(row)


        around = [(y_in, x_in + 1), (y_in, x_in - 1), (y_in + 1, x_in),(y_in - 1, x_in)]

        for a in around:
            if a[0] in range(10) and a[1] in range(10):
                if mat[a[0]][a[1]] == '8':
                    step = a
                    
        
                    
        if step == ():

            
            rand  = random.randrange(4)
            while (around[rand][0] not in range(10) or around[rand][1] not in range(10)) or mat[around[rand][0]][around[rand][1]] == '2':
                rand  = random.randrange(4)
                                                
            return (around[rand][0], around[rand][1])

        
        elif step == around[0] or step == around[1]:
            axis = 'x'
            
        elif step == around[2] or step == around[3]:
            axis = 'y'
            
        print axis

        if axis == 'x':
            range_x = [x_in - 1, x_in + 1, x_in - 2, x_in + 2, x_in - 3, x_in + 3]

            for v in range_x:
                if (v in range(10)) and (mat[y_in][v] =='0' or mat[y_in][v] =='1'):
                    return (y_in, v)


            range_x_1 = [x_in - 1, x_in + 1]


            for v in range_x_1:
                if (v in range(10)) and (mat[y_in][v] =='0' or mat[y_in][v] =='1'):
                    return (y_in, v)

            range_x_2 = [x_in - 2, x_in + 2]

            for a in range(2):
                if (range_x_2[a] in range(10)) and (mat[y_in][range_x_2[a]] =='0' or (mat[y_in][range_x_2[a]] =='1' and mat[y_in][range_x_1[a]] =='8')):
                    return (y_in,range_x_2[a])


            range_x_3 = [x_in - 3, x_in + 3]

            for b in range(2):
                if (range_x_3[b] in range(10)) and (mat[y_in][range_x_3[b]] =='0' or (mat[y_in][range_x_3[b]] =='1' and mat[y_in][range_x_2[b]] =='8')):
                    return (y_in,range_x_3[b])
                


        elif axis == 'y':
            range_y_1 = [y_in - 1, y_in + 1]


            for v in range_y_1:
                if (v in range(10)) and (mat[v][x_in] =='0' or mat[v][x_in] =='1'):
                    return (v, x_in)

            range_y_2 = [y_in - 2, y_in + 2]

            for a in range(2):
                if (range_y_2[a] in range(10)) and ((mat[range_y_2[a]][x_in] =='0' or mat[range_y_2[a]][x_in] =='1') and mat[range_y_1[a]][x_in] =='8'):
                    return (range_y_2[a], x_in)


            range_y_3 = [y_in - 3, y_in + 3]

            for b in range(2):
                if (range_y_3[b] in range(10)) and ((mat[range_y_3[b]][x_in] =='0' or mat[range_y_3[b]][x_in] =='1') and mat[range_y_2[b]][x_in] =='8'):
                    return (range_y_3[b], x_in)
                
            
    else:
        return ('+','+')

def fence_cpu(mat, killed, mark):
    xx =[]
    yy = []
    
    for a in range(10):
        for b in range(10):
            if mat[a][b] == killed:
                xx.append(b)
                yy.append(a)
    print xx
    print
    print yy

                
    for i in range(len(xx)):

        if xx[i]+1 in range(10) and yy[i]+1 in range(10):
            mat[yy[i]+1][xx[i]+1] = mark
            
        if xx[i]-1 in range(10) and yy[i]-1 in range(10):
            mat[yy[i]-1][xx[i]-1] = mark
            
        if xx[i]-1 in range(10) and yy[i]+1 in range(10):
            mat[yy[i]+1][xx[i]-1] = mark
            
        if xx[i]+1 in range(10) and yy[i]-1 in range(10):
            mat[yy[i]-1][xx[i]+1] = mark
            
        if xx[i]+1 in range(10) and yy[i] in range(10):
            mat[yy[i]][xx[i]+1] = mark

        if xx[i]-1 in range(10) and yy[i] in range(10):
            mat[yy[i]][xx[i]-1] = mark
            
        if xx[i] in range(10) and yy[i]-1 in range(10):
            mat[yy[i]-1][xx[i]] = mark
                
        if xx[i] in range(10) and yy[i]+1 in range(10):
            mat[yy[i]+1][xx[i]] = mark

    for u in range(len(xx)):
        mat[yy[u]][xx[u]] = killed



                

def kill(mat, dam, busy, killed):
    counter = 0
    for row in range(10):
        for col in range(10):
            if mat[row][col] == dam:
                x0 = col
                y0 = row
                    
                around = [(x0 + 1, y0), (x0 - 1, y0), (x0, y0 + 1),(x0, y0 - 1)]

                for c in around:
                    if c[0] in range(10) and c[1] in range(10):
                        if mat[c[1]][c[0]] == busy:
                            counter += 1

        
    print counter
    if counter == 0 :
        for row in mat:
            for col in row:
                if col == dam:
                    b = row.index(col)
                    a = mat.index(row)
                    mat[a][b] = killed
    

                    


                
                    
                    
def process_cpu_shot(mat):
    (x0, y0) =  finish_him(mat)

    
    
    if (x0,y0) != ('+','+'):
        x = x0
        y = y0


    else:
        x = random.randrange(10)
        y = random.randrange(10)
        while mat[x][y] == '2' or mat[x][y] == '9':
            x = random.randrange(10)
            y = random.randrange(10)

    
    if mat[x][y] == '1':
        mat[x][y] = '8'
        kill(mat, '8', '1', '9')
        fence_cpu(mat, '9', '2')
        
        
        return'hit'

        

    elif mat[x][y] == '0':
        mat[x][y] = '2'
        return 'miss'

def win_lose(pla, cpu):
    counter1 = 0
    counter2 = 0
    for row in pla:
        for col in row:
            if col == '9':
                counter1 += 1

    for row in cpu:
        for col in row:
            if col == '9':
                counter2 += 1
                
    if counter1 == 20:
        return 'cpu'
    
    if counter2 == 20:
        return 'player'
    

    



    


