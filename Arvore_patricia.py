import random

def gene_elem(nb_bit):
    L=[]
    for i in range(nb_bit):
        L.append(random.randint(0,1))
    return L
def gene_alea_list(nb_list,nb_bit): 
    L=[]
    i=0
    while(i < nb_list):
        l=[]
        for j in range(nb_bit):
            l.append(random.randint(0,1))
        if(l not in L):
            L.append(l)
            i=i+1
    return L

def arbr_from_list(L):  
    AP=init_arbre(L[0])
    for i in range(1,len(L)):
        add(AP,L[i])
        

    return AP

def affiche(AP):
    for cle,val in AP.items():
        print(str(cle)+" : "+str(val))
    print("\n")

def init_arbre(L):  
    D={}
    D[0]=[0,0,L,0,0,0,"N","N",0,[0]] 
    return D

def set_indice(AP): 
    L=AP[0][9]  
    if len(AP[0][9])>1:
        return AP[0][9].pop(-1)
    else:
        #print(AP[0][9][0])
        AP[0][9][0]=AP[0][9][0] + 1
        #print(AP[0][9][0])
        return AP[0][9][0]

def compar_list(L1,L2,ini): 
    N=len(L1)
    i=ini
    #print(L1)
    #print(L2)
    while(i < N and L1[i]==L2[i]  ):
        #print("i="+str(i))
        #print(L1[i])
        #print(L2[i])
        i=i+1
    #print(i)