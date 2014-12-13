from flask import render_template, jsonify, request
from fnest import fnest
import time
import serial


@fnest.route('/setTemp', methods=['GET'])
def set():
    temp = int(request.args['setpoint'])
    print temp
    fnest.config['set_temp'] = temp
    fnest.config['mmap_lib'].change_set_temp(temp)
    cur_temp = fnest.config['mmap_lib'].get_cur_temp() 
    return jsonify(set_temp=temp, cur_temp = cur_temp)


@fnest.route('/getTemp', methods=['GET'])
def get():
    fnest.config['current_temp'] = fnest.config['mmap_lib'].get_cur_temp();
    return jsonify(
        cur_temp = fnest.config['current_temp'], 
        set_temp = fnest.config['set_temp'])

