my_file = open("text.txt", "r")
text = my_file.read().split("\n")

try: 
    input_value = 0
    input_value = int(input("Ваше значення: "))
    # Перевірка
    if input_value > 1000 or input_value <= 0: 
        exit("Неправильні дані.")

    # Знаходження потрібних значень
    for x in text:
        arr_parts = x.split(" ")
        if int(arr_parts[1]) > input_value:
            print(x)
except:
    print("Помилка, перевірте введені параметри")
