# -*- coding: utf-8 -*-
#from fuzzywuzzy import fuzz
import random
import string

import subprocess, sys
import json

import os
import signal

import copy

import socket
import sys
import json
import time

from types import SimpleNamespace

from datetime import datetime

my_hostname = os.environ['my_hostname']

model_file = os.environ['model_file']
experiment = os.environ['experiment']

auto_run = os.environ['auto_run']

# config_file = "testing_config.txt"

def execute_model():
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print("Starting model on: ", current_time)

    cmd = "/opt/netlogo/netlogo-headless.sh --model "+model_file+" --experiment "+experiment
    print (cmd)
    print ("Starting model...")
    os.system(cmd)

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print("Model finished on: ", current_time)

def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)

if __name__ == '__main__':

    if auto_run == "True":
        execute_model()
    else:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((my_hostname, 9999))
        s.listen(2)

        while True:
            conn, addr = s.accept()
            print("Conexao estabelecida com %s" % str(addr))
            received_message = bytes.decode(conn.recv(1024))
            print ("Mensagem recebida:")
            print(received_message)
            x = json.loads(received_message)
            print(x)
            print("typex")
            print(type(x))

            conf_parameters = []

            print ("------------")
            for msg in x:
                print("message:")
                print(msg)
                temp_list = []
                temp_list.append("agent")

                for key, value in msg.items():
                    print("The key and value are ({})".format(value))
                    temp_list.append(value)
                conf_parameters.append(temp_list)
                print ("conf_parameters")
                print(conf_parameters)

            # with open("/shared_volume/config.txt", "w") as output:
            with open(config_file, "w") as output:
                for x in conf_parameters:

                    x[0] = x[0].replace('"', '')

                    x[0] = '"' + x[0] + '"'

                    if(type(x[1]) is str):
                        x[1] = str(x[1]).replace('"', '')
                        x[1] = '"' + x[1] + '"'

                    aaa = json.dumps(x)

                    g = ' '.join(map(str,x))

                    g = '[' + g + ']'

                    #print (g)
                    output.write("%s\n" % (g))

            execute_model()