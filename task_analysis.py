from chatgpt_helper import ask_chatgpt
from datetime import datetime

def analiz_yap(gorevler):
    if not gorevler:
        return "📭 Şu anda analiz edilecek görev yok."

    bugun = datetime.today().date()
    metin = "Görev listem:\n"

    for task in gorevler:
        tarih = task.get("date") or "belirsiz"
        baslik = task.get("title")
        metin += f"- {baslik} | Tarih: {tarih}\n"

    prompt = f"""
Aşağıda bir görev listesi verilmiştir. Tarih ve içerik bilgisine göre hangilerine öncelik verilmesi gerektiğini sıralı şekilde belirt:
{metin}
    """

    return ask_chatgpt(prompt)
