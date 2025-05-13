from task_manager import TaskManager
from reminder_module import Reminder
from storage import Storage
from chatgpt_helper import ask_chatgpt
from motivation import rastgele_motivasyon
from task_analysis import analiz_yap
from etiketleme import etiket_olustur
from akilli_ekleyici import dogal_gorev_coz

class ChatBot:
    def __init__(self):
        self.task_manager = TaskManager()
        self.reminder = Reminder(self.task_manager)

    def start(self):
        print("🎯 Python Akıllı Görev Takip Asistanın'a Hoş Geldiniz!")
        print(f"💡 Motivasyon: {rastgele_motivasyon()}\n")
        while True:
            self.reminder.check_due_tasks()
            command = input("\nKomut girin (ekle/sohbetleekle/listele/sil/sıfırla/analiz/yardım/çık): ").strip().lower()

            if command == "ekle":
                title = input("Görev başlığı: ")
                date = input("Tarih (opsiyonel - yyyy-aa-gg): ")
                print("🏷️ Görev etiketleniyor...")
                etiket = etiket_olustur(title)
                print(f"🤖 Etiket önerisi: {etiket}")
                self.task_manager.add_task(title, date)

            elif command == "sohbetleekle":
                cumle = input("Görevini doğal dilde yaz: ")
                baslik = dogal_gorev_coz(cumle)
                if baslik:
                    print(f"📌 Başlık: {baslik}")
                    tarih = input("📅 Tarihi manuel gir (yyyy-aa-gg): ")
                    self.task_manager.add_task(baslik, tarih)
                else:
                    print("❌ GPT cümleyi anlayamadı.")

            elif command == "listele":
                self.task_manager.list_tasks()

            elif command == "sil":
                try:
                    task_id = int(input("Silmek istediğiniz görev ID'si: "))
                    self.task_manager.delete_task(task_id)
                except ValueError:
                    print("❌ Lütfen geçerli bir sayı girin.")

            elif command == "analiz":
                print("🧠 Yapay Zekâ görevlerini inceliyor...\n")
                yanit = analiz_yap(self.task_manager.tasks)
                print(f"\n🤖 Tavsiye:\n{yanit}")

            elif command == "sıfırla":
                confirm = input("Tüm görevleri silmek istediğinize emin misiniz? (evet/hayır): ").strip().lower()
                if confirm == "evet":
                    self.task_manager.tasks = []
                    Storage.save_tasks([])
                    print("📭 Tüm görevler silindi.")
                else:
                    print("❌ İşlem iptal edildi.")

            elif command == "yardım":
                user_input = input("Ne hakkında yardım istiyorsunuz? ")
                yanit = ask_chatgpt(user_input)
                print(f"\n🤖 Yapay Zekâ Asistan:\n{yanit}")

            elif command == "çık":
                print("👋 Görüşmek üzere!")
                break

            else:
                print("❗ Tanımsız komut girdiniz.")
