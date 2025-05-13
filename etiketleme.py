from chatgpt_helper import ask_chatgpt

def etiket_olustur(gorev_basligi):
    prompt = f"""
Aşağıdaki görev başlığına uygun olacak şekilde 1 ila 3 arasında görev etiketi öner.
Etiketler yalnızca şunlardan seçilmeli: [Acil, Kişisel, İş, Rutin, Sağlık, Eğitim, Finans, Aile, Hobi]

Görev: "{gorev_basligi}"

Cevabı yalnızca şu formatta döndür:
Etiketler: [etiket1, etiket2]
"""
    try:
        yanit = ask_chatgpt(prompt)
        return yanit
    except Exception as e:
        return f"Etiketleme başarısız: {e}"


