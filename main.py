monday = int(input("Введите расход за понедельник: "))
tuesday=int(input('Введите расход за вторник: '))
wednesday = int(input('Введите расход за среду: '))
thursday = int(input('Введите расход за четверг: '))
friday = int(input('Введите расход за пятницу: '))
saturday = int(input('Введите расход за субботу: '))
sunday = int(input('Введите расход за воскресенье: '))
total_sum=monday+tuesday+wednesday+thursday+friday+saturday+sunday
print(f"Общий расход за всю неделю: {total_sum}")
average_num=total_sum/7
rounded_num=round(average_num,1)
print(f"Средний расход за день: {rounded_num}")
