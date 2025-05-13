from chatgpt_helper import ask_chatgpt

def dogal_gorev_coz(ifadeler):
    prompt = f"""
Aşağıdaki cümleyi analiz et. Sadece görev başlığını çıkar. Tarih belirtme, sadece başlığı ver.

Cevap formatı sadece şu şekilde olsun:
Başlık: <görev başlığı>

Cümle: "{ifadeler}"
"""
    try:
        yanit = ask_chatgpt(prompt)
        satirlar = yanit.splitlines()
        baslik = ""
        for s in satirlar:
            if s.lower().startswith("başlık:"):
                baslik = s.split(":", 1)[1].strip()
                break
        return baslik  # ❗ tuple değil, sadece string
    except Exception as e:
        return ""
