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
##########################
def mat_mul_ele(mat1, mat2):
    result=[]
    copy=[]
    for i in range(len(mat1)):
            for j in range(len(mat1[i])):
                copy.append(mat1[i][j]*mat2[i][j])
            result.append(copy)
            copy=[]

    return result

###################
def mat_mul_row_col(mat1, mat2, i, j):
    result=[]
    copy=[]

    if len(mat2)==len(mat1[i]):
        for a in range(len(mat2)):
            for b in range(len(mat2[a])):
                if (b==j):
                    copy.append(mat2[a][b])
        
        a=0
        for a in range(len(mat1[i])):
            result.append(copy[a]*mat1[i][a])

        return result  

################
def mat_mul_mat(mat1, mat2):
    result=[]
    copy,copy2=[],[]
    if len(mat2)==len(mat1[0]):
        for a in range(len(mat2)):
            for b in range(len(mat2[a])): 
                copy.append(mat_mul_row_col(mat1,mat2,a,b))
            
            copy2=[]
            for c in range(len(copy)):
                sum=0
                for d in range(len(copy[c])):
                    sum+=copy[c][d]
                copy2.append(sum)
            result.append(copy2)
            copy=[]
    return result  
            