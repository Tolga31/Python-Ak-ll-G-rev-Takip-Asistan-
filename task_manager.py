
from storage import Storage

class TaskManager:
    def __init__(self):
        self.tasks = Storage.load_tasks()

    def add_task(self, title, date=None):
        task = {
            "id": len(self.tasks) + 1,
            "title": title.strip(),  # Başlıkta boşluk varsa temizle
            "date": date.strip() if date else "",  # Tarihi boşluklardan arındır
            "done": False
        }
        self.tasks.append(task)
        Storage.save_tasks(self.tasks)
        print(f"✅ Başarılı. Görev eklendi: {title}")

    def list_tasks(self):
        if not self.tasks:
            print("📝 Henüz hiç görev yok.")
        else:
            print("\n📋 Görev Listesi:")
            for task in self.tasks:
                status = "✔️" if task["done"] else "⏳"
                print(f"{task['id']}. {task['title']} | Tarih: {task['date']} | Durum: {status}")

    def delete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                # ID’leri yeniden sırala
                for i, t in enumerate(self.tasks, start=1):
                    t["id"] = i
                Storage.save_tasks(self.tasks)
                print(f"🗑️ Görev silindi: {task['title']}")
                return
        print("❌ Böyle bir görev ID'si bulunamadı.")


        #Görevleri bir liste olarak tuttuk.
        # Görevler.json dosyasına kaydedilecek ve bunu storage.py dosyasına yazacağım.
        # Görev silindiği zaman ID'ler sıfırlanıyor(liste bozulmaması için gerekli).
