def display_res(res_arr):
    #Print results:
    print('    a','\t   b','\t   r','\t  q','\t   S','\t   T')
    print('\t\t\t\t   1\t  0')
    print('\t\t\t\t   0\t  1')
    rl = [" "]*(len(res_arr)+1)
    for rl, row in zip(rl, res_arr):
        print ('%s [%s]' % (rl, ' '.join('%06s' % i for i in row)))



def euclid_algo(x, y):
       
    S_T_list=[1,0,0,1]
    res_arr=list()
    row_arr=[]
    while y != 0:
        
        temp=divmod(x,y)
        r=temp[1] ; q=temp[0]
        if r==0:
            x=y
            break
        S=S_T_list[0] - q*S_T_list[2]
        
        T=S_T_list[1] - q*S_T_list[3]
        
        S_T_list.pop(0);S_T_list.pop(0)
        S_T_list.append(S)
        S_T_list.append(T)
        row_arr=[x,y,r,q,S,T]
        res_arr.append(row_arr)
        (x, y) = (y, x % y)
       
    display_res(res_arr)
    print('(',x,S,T,')')


    
a=1398
b=324
euclid_algo(a,b)
