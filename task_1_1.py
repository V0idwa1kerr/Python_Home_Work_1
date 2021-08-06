duration = int(input("Введите количество секунд: "))

year = (duration // 31536000)
month = (duration % 31536000) // 2628000
day = (duration % 2628000) // 86400
hour = (duration % 86400) // 3600
minute = (duration % 3600) // 60
second = duration % 60
result = ["{} г. {} мес. {} дн. {} ч. {} мин. {} сек.".format(year, month, day, hour, minute, second)]

print(result)
