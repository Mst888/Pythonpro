meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL" : "bir şakaya karşılık cevap",
            "SHEESH" :"onaylamamak",
            "CREEPY ":"korkunç",
            "AGGRO": "agresifleşmek/sinirlenmek"
            }
n= int(input("Kaç kelimeye bakacaksınız?(Sayı giriniz.)"))
for i in range(n):
    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!)(Bitirmek isterseniz boşluğa basın.): ")
    if word == " ":
        print("Sözlük kapatılıyor.")
        break 
    elif word in meme_dict.keys():
        print(meme_dict[word]) 
