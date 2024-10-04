"""
Обробник сторінки завершення прання
"""

from flask import (
    render_template,
)

from app import app

#  Обробник кінцевої сторінки
@app.route('/completed')
def completed():
    """Завершаюча сторінка"""
    return render_template('completed.html')
