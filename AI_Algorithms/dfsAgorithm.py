#dfs - Depth First Search (Derin öncelikli arama)

grafik={
    'A':["B", "C"],
    'B':["D", "E"],
    'C':["F"],
    'D':[],
    'E':[],
    'F':[]
}

ziyaret=set()  #kümemizi oluşturuyoracağız

def dfs(ziyaret, grafik, dügüm):
    if dügüm not in ziyaret:
        print(dügüm)
        ziyaret.add(dügüm)
        for komsu in grafik[dügüm]:
            dfs(ziyaret, grafik, komsu)

dfs(ziyaret, grafik, 'A')