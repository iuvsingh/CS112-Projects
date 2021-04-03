def mat_to_str(mat):
    result=''

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            result+=str(mat[i][j])  + ' '
        result+='\n'
    
    return result

def minesweeper(mat):
    copy=mat[:]

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            ct=0
            if mat[i][j]=='x':
                for k in range(len(mat)):
                    for l in range(len(mat[k])):
                        if (mat[k][l]=='m') and (l==j or l==j+1 or l==j-1) and (i==k or i==k+1 or i==k-1):
                            ct+=1
                mat[i][j]=ct
    copy=[]












    # mines, next_spot=0,[]

    # for i in range(len(mat)):
    #     for j in range(len(mat[i])):
    #         if mat[i][j]=='m':
    #             mines+=1
    # i,j=0,0
    # for i in range(len(mat)):
    #     for j in range(len(mat[i])):
    #         if mat[i][j]=='x':
    #             mat[i][j]=mines
        

                
    
# def transpose(mat):

# def mat_mul_ele(mat1, mat2):

# def mat_mul_row_col(mat1, mat2, i, j):

# def mat_mul_mat(mat1, mat2):
