def unlu_say(text, cikti=0):
    unlu_kelimeler='aeuıoüiöAEUIOÜİÖ'
    for char in text:
        if char in unlu_kelimeler:
            cikti =cikti+1
    return cikti
text=input("Lütfen yazı giriniz : ")
print("Yazınızdaki Ünlü Kelime sayısı {}" .format(unlu_say(text)))