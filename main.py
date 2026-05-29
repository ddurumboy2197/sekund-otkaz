def sekundni_soat_minut_sekundga(qaytarish):
    soat = qaytarish // 3600
    qolgan_sekundlar = qaytarish % 3600
    minut = qolgan_sekundlar // 60
    sekund = qolgan_sekundlar % 60
    return soat, minut, sekund

sekund = int(input("Sekundni kiriting: "))
soat, minut, sekund = sekundni_soat_minut_sekundga(sekund)
print(f"{sekund} sekund {soat} soat {minut} minut")
```

```python
def sekundni_soat_minut_sekundga(qaytarish):
    soat = qaytarish // 3600
    qolgan_sekundlar = qaytarish % 3600
    minut = qolgan_sekundlar // 60
    sekund = qolgan_sekundlar % 60
    return f"{soat} soat {minut} minut {sekund} sekund"

sekund = int(input("Sekundni kiriting: "))
print(sekundni_soat_minut_sekundga(sekund))
