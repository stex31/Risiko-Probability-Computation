'Created on Fri Jun 16 21:19:44 2023'
'@author: Stefano Romano'

def Risiko(A,D):
        
    if A==0:
        return 0
    
    if D==0:
        return 100
    
    if A == 1 and D == 1:
        return 500/12
    
    if A==2 and D==1:        
        return 100*(1-91/216*(1-Risiko(1,1)/100))
    
    if A>2 and D==1:
        # Here I compute the probability of winning Nv1, where N>2. 
        return 100*(1-441/1296**(A-2)*(1-Risiko(2,1)/100))
    
    if A==1 and D==2:
        #compute the probability of winning the first toss as 55/216        
        #multiply the probability obtained with the probability of winning 1v1
        return 55/216*Risiko(1,1)
    
    if A==1 and D>2:
        #compute the probability of winning the first D-2 tosses times the probability of winning 1v2
        return (225/1296)**(D-2)*Risiko(A,2)
    
    if A==2 and D==2:
        return 100*295/6**4+420/6**4*Risiko(1,1)
    
    if A > 2 and D==2:
        return 2890/6**5*100 + 2611/6**5*Risiko(A-1,1)+2275/6**5*Risiko(A-2,2)
    
       
    if A==2 and D > 2:
        return 979/6**5*Risiko(A,D-2) + 1981/6**5*Risiko(1,D-1)
    
    return 6420/6**6*Risiko(A,D-3)+10017/6**6*Risiko(A-1,D-2)+12348/6**6*Risiko(A-2,D-1)+17871/6**6*Risiko(A-3,D)