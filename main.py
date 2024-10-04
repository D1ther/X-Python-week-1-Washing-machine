"""
Файл запуску
"""

from app import app

# Головна функція
def main():
    """Функція запуску"""
    app.run(port=1000, debug=True)

# запуск
if __name__ == '__main__':
    main()
