#Alpha-Beta Pruning - ağaç budama

agac=[[[5, 1, 2], [8, -8, -9], [9, 4 ,5], [-3, 4, 3]]]
kok=0
budama=0

def cocuklar(dal, derinlik, alfa, beta):
    global agac
    global kok
    global budama
    i=0
    for cocuk in dal:
        if type(cocuk) is list: #type cocuk ise ve listedeyse
            (nalfa, nbeta)=cocuklar(cocuk, derinlik+1, alfa, beta) 
            if derinlik % 2 == 1: #derinlik tek sayı ise
                beta = nalfa  if nalfa < beta  else beta
            else:
                alfa = nbeta  if nbeta < alfa  else alfa
                dal[i]=alfa if derinlik % 2 == 0 else beta
                i+=1
        else: #eğer buradaki hiçbir şey olmazsa
            if derinlik % 2 == 0  and  alfa < cocuk:
                alfa = cocuk
            if derinlik % 2 == 1  and  beta > cocuk:
                beta = cocuk
            if alfa >= beta:
                budama+=1
                break
    if derinlik == kok:
        agac = alfa if kok == 0 else beta 
        return(alfa, beta)

def alfabeta(in__agac, baslangıc = kok, alt = -15, ust = 15):
    global agac
    global kok
    global budama
    (alfa, beta) = cocuklar(agac, baslangıc, alt, ust)
    if __name__ == "__main__":
        print("(alfa, beta): ", alfa, beta)
        print("Sonuc: ", agac)
        print("Budama Sayısı: ", budama)
    return(alfa, beta, agac, budama)
if __name__ == "__main__":
    alfabeta(None)