from datetime import datetime

now = datetime.now()

formatted_datetime = now.strftime('%Y-%m-%d %H:%M:%S')

day_of_week = now.strftime('%A')
week_number = now.isocalendar()[1]

print(f"Текущие дата и время: {formatted_datetime}")
print(f"День недели: {day_of_week}")
print(f"Номер недели в году: {week_number}")
