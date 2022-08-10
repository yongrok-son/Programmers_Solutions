#https://school.programmers.co.kr/learn/courses/30/lessons/60059
#Lv3 자물쇠와 열쇠 1
def solution(key, lock):
    
    def is_true(key, lock, x , y):

        for i in range(M):
            for j in range(M):
                if x <= M+i< x+N and y <= M+j < y+N:
                    temp  = key[M+i-x][M+j-y] + lock[i][j]
                    if temp == 0 or temp > 1:
                        return False
                else:                    
                    if lock[i][j] == 0:
                        return False
        return True
    
    def turn_clockwise(key):      
        temp_i = []
        for i in range(len(key)):
            temp_j=[]
            for j in range(len(key)): 
                temp_j.append(key[len(key)-j-1][i])  

            temp_i.append(temp_j)
        return temp_i
    


    M = len(lock) # lock = M*M
    N = len(key)  # key = N*N
    
    answer_key = key

    for turn in range(4):
        
        for i in range(M*2):
            for j in range(M*2):
                if is_true(answer_key, lock, i, j): 
                    return True                 

        answer_key =turn_clockwise(answer_key) 
                                              
    return False

key	=[[1, 1, 1], [1, 1, 1], [1, 1, 0]]
lock =[[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]
print( solution(key,lock))
