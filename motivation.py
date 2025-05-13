import random

motivasyonlar = [
    "Bugün küçük bir adım, yarın büyük bir zafer!",
    "Başlamak, başarmanın yarısıdır. Hadi başlayalım!",
    "Zor görevler en çok gelişmeni sağlar.",
    "Kendine güven, çünkü harika işler başarabilirsin!",
    "Günün kahramanı sen olabilirsin — şimdi başla!"
]

def rastgele_motivasyon():
    return random.choice(motivasyonlar)
