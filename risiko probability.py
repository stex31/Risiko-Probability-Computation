'Created on Fri Jun 16 21:19:44 2023'
'@author: Stefano Romano'

# The probability of winning 1v1 can be easily computed calling the results D1 of 
# the die tosses D1 and D2, and noting that by simmetry, P(D1>D2)=P(D2>D1), and 
# P(D1=D2)=1/6. Then we have: P(D1>D2)+P(D2>D1)+P(D2=D1)=1 => 2P(D1>D2)=5/6
# => P(D1>D2)=5/12
# We can also compute the probability directly:
R_1v1_10=0
for x in range(6):
    R_1v1_10 = R_1v1_10 + x/36


# Here I compute the probability of losing a die toss when 2v1 
R_2v1_01 = 0
for x in range(7):
    R_2v1_01 = R_2v1_01 + x**2/216
    
# Here I compute the probability of losing a die toss when 3v1 
R_3v1_01 = 0
for x in range(7):
    R_3v1_01 = R_3v1_01 + x**3/1296

# Here I compute the probability of losing a die toss when 1v2    
R_1v2_10 = 0
for x in range(6):
    R_1v2_10 = R_1v2_10 + x**2/216

# Here I compute the probability of losing a die toss when 1v3    
R_1v3_10 = 0
for x in range(6):
    R_1v3_10 = R_1v3_10 + x**3/1296
    
# Here I compute the probabilities of the various outcomes when 2v2
R_2v2_20 = 0
R_2v2_11 = 0
R_2v2_02 = 0
    
for x in range(1, 7):
    for y in range(1, 7):
        for a in range(1, 7):
            for b in range(1, 7):
                    
                if max(x,y) > max(a,b) and min(x,y) > min(a,b):
                    R_2v2_20=R_2v2_20 + 1
                        
                if max(x,y) <= max(a,b) and min(x,y) <= min(a,b):
                    R_2v2_02 = R_2v2_02 + 1
                        
R_2v2_11 = 6**4-R_2v2_20-R_2v2_02






# computing the probabilities of the various outcomes when 3v2


R_3v2_20 = 0
R_3v2_02 = 0                
R_3v2_11 = 0
    
for x in range(1, 7):
    for y in range(1, 7):
        for z in range(1, 7):
            for a in range(1, 7):
                for b in range(1,7):
                    S = sorted([x,y,z])
                    T = sorted([a,b])
                        
                    if S[2]>T[1] and S[1]>T[0]:
                        R_3v2_20 = R_3v2_20 + 1
                            
                    if S[2]<=T[1] and S[1]<=T[0]:
                        R_3v2_02 = R_3v2_02 + 1
    
R_3v2_20 = R_3v2_20
R_3v2_02 = R_3v2_02               
R_3v2_11 = 6**5 - R_3v2_20 - R_3v2_02



# computing the probabilities of the various outcomes when 2v3



R_2v3_20 = 0
R_2v3_11 = 0
R_2v3_02 = 0
    
for x in range(1, 7):
    for y in range(1, 7):
        for a in range(1, 7):
            for b in range(1, 7):
                for c in range(1,7):
                    S = sorted([x,y])
                    T = sorted([a,b,c])
                        
                    if S[1]>T[2] and S[0]>T[1]:
                        R_2v3_20 = R_2v3_20 + 1
                            
                    if S[1]<=T[2] and S[0]<=T[1]:
                        R_2v3_02 = R_2v3_02 + 1
    
R_2v3_11 = 6**5 - R_2v3_20 - R_2v3_02




# computing the probabilities of the various outcomes when 2v3


R_3v3_30 = 0
R_3v3_21 = 0
R_3v3_12 = 0
R_3v3_03 = 0
R=[0,0,0,0]
for x in range(1,7):
    for y in range(1,7):
        for z in range(1,7):
            for a in range(1,7):
                for b in range(1,7):
                    for c in range(1,7):
                        i = 0
                        S = sorted([x,y,z])
                        T = sorted([a,b,c])
                            
                        for f in range(3):
                            if S[f]>T[f]:
                                i = i + 1
                        R[i] = R[i] + 1
R_3v3_30 = R[3]
R_3v3_21 = R[2]
R_3v3_12 = R[1]
R_3v3_03 = R[0]