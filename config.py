from decouple import Config

# Путь к файлу settings.ini
config_path = r'settings.ini'

# Создаем экземпляр Config для работы с settings.ini
config = Config(config_path)

# Получаем значения из секции GameSettings с помощью get()
min_number_str = config.get('GameSettings', 'min_number')
max_number_str = config.get('GameSettings', 'max_number')
max_attempts_str = config.get('GameSettings', 'max_attempts')
initial_capital_str = config.get('GameSettings', 'initial_capital')

# Преобразуем строки в целые числа в блоке try-except для обработки возможных ошибок
try:
    min_number = int(min_number_str)
    max_number = int(max_number_str)
    max_attempts = int(max_attempts_str)
    initial_capital = int(initial_capital_str)

    # Выводим значения для проверки
    print(f"min_number: {min_number}, max_number: {max_number}, max_attempts: {max_attempts}, initial_capital: {initial_capital}")

except ValueError:
    print("Ошибка: одно из значений в файле settings.ini не является целым числом.")
