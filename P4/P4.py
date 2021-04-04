def mat_to_str(mat):
    result=''

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            result+=str(mat[i][j])  + ' '
        result+='\n'
    
    return result
######################
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
######################
def transpose(mat):
    result=[]
    copy=[]
    if (len(mat))==len(mat[0]):
        for i in range(len(mat)):
            for k in range(len(mat)):
                copy.append(mat[k][i])
            result.append(copy)
            copy=[]
    else:
        for i in range(len(mat[0])):
            for k in range(len(mat)):
                copy.append(mat[k][i])
            result.append(copy)
            copy=[]
    copy=[]
    return result

def mat_mul_ele(mat1, mat2):

# def mat_mul_row_col(mat1, mat2, i, j):

# def mat_mul_mat(mat1, mat2):
