from flask import Flask, url_for
import os, ctypes

fnest = Flask(__name__)

# Function to easily find your assets
# In your template use <link rel=stylesheet href="{{ static('filename') }}">
fnest.jinja_env.globals['static'] = (
    lambda filename: url_for('static', filename = filename)
)

fnest.config['current_temp'] = 66
fnest.config['set_temp'] = 70

fnest.config['mmap_lib'] = ctypes.cdll.LoadLibrary('./mmap.so')

from fnest import views
from fnest import api