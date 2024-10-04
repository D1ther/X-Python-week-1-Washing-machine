"""
Файл з оброкником сторінки головного меню
"""

from flask import (
    render_template,
)

from app import app

# Обробник головної сторінки
@app.route('/')
def main_menu():
    """Сторінка з кнопкою для запуску прання"""
    return render_template('start_washing_button.html')
