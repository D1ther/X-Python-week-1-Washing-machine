"""
Обробник сторінки прання
"""

from flask import (
    render_template,
    request,
)

from app import app

# Обробник сторінки прання
@app.route('/washing', methods=['POST', 'GET'])
def washing():
    """Обробник сторінки з початком прання"""
    if request.method == 'POST':
        return render_template('washing.html')
