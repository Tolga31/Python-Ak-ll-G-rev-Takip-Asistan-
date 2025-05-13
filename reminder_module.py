from datetime import datetime, timedelta

class Reminder:
    def __init__(self, task_manager):
        self.task_manager = task_manager

    def check_due_tasks(self):
        today = datetime.today().date()
        upcoming = []

        for task in self.task_manager.tasks:
            if task.get("date") and task["date"] != "":
                try:
                    task_date = datetime.strptime(task["date"].strip(), "%Y-%m-%d").date()
                    delta = (task_date - today).days

                    if delta < 0:
                        print(f"⚠️ Gecikmiş görev: {task['title']} ({task['date']})")
                    elif delta == 0:
                        print(f"📌 Bugün yapılması gereken görev: {task['title']}")
                    elif 0 < delta <= 2:
                        upcoming.append(f"⏳ Yaklaşan görev: {task['title']} ({task['date']})")
                except ValueError:
                    print(f"⚠️ Tarih okunamadı: {task['title']}. Lütfen yyyy-aa-gg formatında girildiğinden emin olun.")


        if upcoming:
            print("\nYaklaşan görevler:")
            for task_info in upcoming:
                print(task_info)


# Görevlerin tarihini kontrol ediyoruz.
#Geçmiş,bugün,yakında olacak görevleri kullanıcıya bildiriyoruz.
