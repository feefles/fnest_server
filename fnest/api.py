from flask import render_template, jsonify, request
from fnest import fnest
import time
import serial


@fnest.route('/setTemp', methods=['GET'])
def set():
    temp = request.args["setpoint"]
    print temp
    fnest.config['set_temp'] = temp
    fnest.config['mmap_lib'].change_cur_temp(t)
    cur_temp = mmap.config['mmap_lib'].get_cur_temp(t)
    return jsonify(set_temp=temp, cur_temp = cur_temp)


@fnest.route('/getTemp', methods=['GET'])
def get():
    fnest.config['current_temp'] = fnest.config['mmap_lib'].get_cur_temp();
    return jsonify(
        cur_temp = fnest.config['current_temp'], 
        set_temp = fnest.config['set_temp'])

@fnest.route('/poll', methods=['GET'])
def poll():
    cur = time.localtime().tm_min
    if cur == 13:
        return jsonify(change=True, type=True) #change state
    else:
        return jsonify(change=False, type=False) #don't change state