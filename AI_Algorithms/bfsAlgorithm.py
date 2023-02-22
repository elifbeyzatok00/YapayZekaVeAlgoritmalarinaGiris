#bfs - Breadth-first search (yayılım öncelikli arama)

grafik = {
  'A': ['B', 'C'],
  'B': ['D', 'E'],
  'C': ['F'],
  'D': [],
  'E': [],
  'F': []
}

ziyaret = []
yıgın = []


#ziyaret içe alınan veri, grafik verilerin alındığı yer, dügüm hangi aşamada gerçekleşecektir? bunlar dügüm olarak gerçekleşecektir
#ziyaret ettiklerimizi append ile dügüm yapısına ekledik
#eklediğimiz dügümleri yıgın yapısında oluşturuyoruz
def bfs(ziyaret, grafik, dügüm):
  ziyaret.append(dügüm)
  yıgın.append(dügüm)

  # bunları sayaça koyalım
  #while ile yıgındaki elemanları ziyaret edelim
  while yıgın:
    s = yıgın.pop(
      0
    )  #s başlangıç verisi, yıgın.pop yani en üsttekini alacak. (0) yani baslangıç elemanından itibaren sıralamaya başlayacak
    print(
      s, end=" "
    )  #s.end yani başlangıcından sonuna kadar aralarına " " boşluk koyarak yazdırır

    for komsu in grafik[s]:  #komsusundan başlayarak grafiği ziyaret edecek
      if komsu not in ziyaret:  #eğer komsu ziyaret edilenin içinde değilse
        yıgın.append(komsu)  #komsuyu yıgına ekler


#çalışmaya buradan başlasın dedik
bfs(ziyaret, grafik, 'A')
