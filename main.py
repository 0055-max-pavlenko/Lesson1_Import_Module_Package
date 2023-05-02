from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')


if __name__ == '__main__':
    print(f"Сегодня: {datetime.now().strftime('%d %B %Y')}")