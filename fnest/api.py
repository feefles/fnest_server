from flask import render_template, jsonify, request
from fnest import fnest
import time
import serial


@fnest.route('/setTemp', methods=['GET'])
def set():
    temp = request.args["temp"]
    print temp
    fnest.config['set_temp'] = temp
    fnest.config['mmap_lib'].change_cur_temp(t)
    return jsonify(temp=temp)


@fnest.route('/getTemp', methods=['GET'])
def get():
    return jsonify(cur_temp = fnest.config['current_temp'], set_temp = fnest.config['set_temp'])

@fnest.route('/poll', methods=['GET'])
def poll():
    cur = time.localtime().tm_min
    if cur == 13:
        return jsonify(change=True, type=True) #change state
    else:
        return jsonify(change=False, type=False) #don't change state