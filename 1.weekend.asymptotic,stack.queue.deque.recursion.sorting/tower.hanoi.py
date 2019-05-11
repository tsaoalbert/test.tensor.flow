
def TowerOfHanoi(n , from_rod, to_rod, aux_rod): 
    if n == 0: 
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod) 
    print ("Move disk",n,"from",from_rod,"to",to_rod )
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)

TowerOfHanoi(6, "A","B","C")
