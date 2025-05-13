# storage.py

import json
import os

FILE_NAME = "tasks.json"

class Storage:
    @staticmethod
    def load_tasks():
        if not os.path.exists(FILE_NAME): #load_tasks(): Eğer tasks.json dosyası yoksa boş liste döner.
            return []

        with open(FILE_NAME, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []

    @staticmethod
    def save_tasks(tasks):
        #save_tasks(): Görevleri JSON formatında dosyaya yazar.
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            json.dump(tasks, f, indent=4, ensure_ascii=False)
# ensure_ascii=False: Türkçe karakterler bozulmadan yazılır.
