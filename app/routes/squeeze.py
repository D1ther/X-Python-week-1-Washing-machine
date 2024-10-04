"""
Обробник сторінки відтиску
"""

from flask import (
    render_template
)

from app import app

# обробник сторінки прання
@app.route('/squeeze')
def squeeze():
    """Сторінка прання"""
    return render_template('squeeze.html')
