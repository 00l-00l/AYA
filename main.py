import os

if os.path.exists("memory.txt"):
# Фаил существует -читает имя 
 with open("memory.txt", "r") as file:
           name  = file.read()
           print(f"C возврашением {name}")
else:
#файл отсутсвует создаем новый
  name = input("Как вас зовут ? ")
  with open("memory.txt", "w") as file:
      file.write(name)
      print(f"Приятно познакомиться, {name}! Я запомнил ваше имя.")

print(f"Я — АЯ. Готова к работе.")

answer  = input ("Какое время суток  сейчас у вас ? ").lower()
if answer == "утро":
    print(f"Доброе утро, {name}! Пора кодить.")
elif answer == "день":
    print(f"Добрый день, {name}! Как успехи?")
else:
    print(f"Добрый вечер, {name}! Подводим итоги дня.")

while True:
      list = input("Что хотите сделать ? ").lower()
      if list == "добавить":
       with open("tasks.txt", "a", encoding="utf-8") as file:
         task = input("Введите задачу ")
         file.write(task + "\n")
         print(f"Записала {task}")
                    
      elif list == "список":
           with open("tasks.txt", "r", encoding="utf-8") as file1:
               for line in file1:
                print(line.strip())
      elif list == "выход":
         print("до свидания")
         break
        
       
