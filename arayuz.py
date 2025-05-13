import tkinter as tk
from tkinter import messagebox
from chatgpt_helper import ask_chatgpt
from storage import Storage

# Görevleri yükle
gorevler = Storage.load_tasks()

def gorev_ekle():
    baslik = baslik_girdisi.get()
    tarih = tarih_girdisi.get()
    if not baslik or not tarih:
        messagebox.showwarning("Eksik Bilgi", "Lütfen başlık ve tarih gir.")
        return

    gorev = f"{baslik} ({tarih})"
    gorevler.append(gorev)
    gorev_listesi.insert(tk.END, gorev)
    Storage.save_tasks(gorevler)

    baslik_girdisi.delete(0, tk.END)
    tarih_girdisi.delete(0, tk.END)

def gorev_sil():
    secili_index = gorev_listesi.curselection()
    if not secili_index:
        messagebox.showwarning("Seçim Yok", "Silmek için bir görev seçmelisin.")
        return
    index = secili_index[0]
    gorev_listesi.delete(index)
    del gorevler[index]
    Storage.save_tasks(gorevler)

def gpt_ile_baslik_olustur():
    cumle = baslik_girdisi.get()
    if not cumle:
        messagebox.showwarning("Uyarı", "Lütfen doğal bir cümle gir.")
        return

    prompt = f"""
Aşağıdaki cümleyi analiz et ve sadece görev başlığını çıkar.
Cümle: "{cumle}"
Sadece şu formatta döndür: Başlık: ...
"""
    yanit = ask_chatgpt(prompt)
    satirlar = yanit.splitlines()
    for s in satirlar:
        if s.lower().startswith("başlık:"):
            baslik = s.split(":", 1)[1].strip()
            baslik_girdisi.delete(0, tk.END)
            baslik_girdisi.insert(0, baslik)
            messagebox.showinfo("GPT Başlık Önerisi", f"Önerilen başlık: {baslik}")
            return
    messagebox.showerror("Hata", "GPT başlık çıkaramadı.")

# Pencere oluştur
pencere = tk.Tk()
pencere.title("🧠 Görev Asistanı")
pencere.geometry("500x550")
pencere.configure(bg="#f5f5f5")

# Başlık
etiket = tk.Label(pencere, text="🧠 Görev Ekle", font=("Arial", 14, "bold"), bg="#f5f5f5")
etiket.pack(pady=10)

# Girdi: Başlık / Doğal Cümle
tk.Label(pencere, text="Başlık veya Doğal Cümle:", bg="#f5f5f5").pack()
baslik_girdisi = tk.Entry(pencere, width=40)
baslik_girdisi.pack(pady=5)

# GPT butonu
gpt_buton = tk.Button(pencere, text="🧠 GPT ile Başlık Öner", command=gpt_ile_baslik_olustur, bg="#2196F3", fg="white")
gpt_buton.pack(pady=5)

# Girdi: Tarih
tk.Label(pencere, text="Tarih (yyyy-aa-gg):", bg="#f5f5f5").pack()
tarih_girdisi = tk.Entry(pencere, width=40)
tarih_girdisi.pack(pady=5)

# Ekle butonu
ekle_buton = tk.Button(pencere, text="➕ Görevi Ekle", command=gorev_ekle, bg="#4CAF50", fg="white")
ekle_buton.pack(pady=10)

# Görev listesi başlık
liste_baslik = tk.Label(pencere, text="📋 Görev Listesi", font=("Arial", 12, "bold"), bg="#f5f5f5")
liste_baslik.pack()

# Listbox
gorev_listesi = tk.Listbox(pencere, width=50)
gorev_listesi.pack(pady=10)

# Önceki görevleri listeye ekle
for g in gorevler:
    gorev_listesi.insert(tk.END, g)

# Silme butonu
sil_buton = tk.Button(pencere, text="❌ Seçili Görevi Sil", command=gorev_sil, bg="#e53935", fg="white")
sil_buton.pack(pady=5)

# Başlat
pencere.mainloop()
