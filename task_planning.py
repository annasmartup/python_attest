from datetime import datetime, timedelta

def get_future_date(days_from_now):
    current_date = datetime.now()

    future_date = current_date + timedelta(days=days_from_now)

    formatted_date = future_date.strftime('%Y-%m-%d')

    return formatted_date


days = 10
future_date = get_future_date(days)
print(f"Дата через {days} дней: {future_date}")