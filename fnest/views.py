from flask import render_template
from fnest import fnest

@fnest.route('/')
def index():
    return render_template('index.html', 
        cur_temp = fnest.config['current_temp'], 
        set_temp = fnest.config['set_temp'])
