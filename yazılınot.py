yazili1 = int(input("1.yazılı notunu girin:"))
yazili2 = int(input("2.yazılı notunu girin:"))
sözlü = int(input("sözlü notunu girin:"))

ortalama = float((yazili1 + yazili2 + sözlü)/3)

if  ortalama > 0  and ort<24:
    print(f"ortalamanız: {ortalama} ve değerlendirme notu: 0")
elif ortalama > 25  and ort<44:
    print(f"ortalamanız: {ortalama} ve değerlendirme notu: 1")
elif ortalama > 45  and ort<54:
    print(f"ortalamanız: {ortalama} ve değerlendirme notu: 2")
elif ortalama > 55  and ort<69:
    print(f"ortalamanız: {ortalama} ve değerlendirme notu: 3")
elif ortalama > 70  and ort<84:
    print(f"ortalamanız: {ortalama} ve değerlendirme notu: 4")
elif ortalama > 85  and ort<100:
    print(f"ortalamanız: {ortalama} ve değerlendirme notu: 5")
else :
    print("yanlış not bilgisi")    
