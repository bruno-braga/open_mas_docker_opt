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
# from time import time, sleep
import time

from types import SimpleNamespace

from datetime import datetime

# export_file = "/teste/teste.txt"
# config_file = "/teste/teste_config.txt"

# export_file = os.environ['export_file']
# config_file = os.environ['config_file']

my_hostname = os.environ['my_hostname']
# talker = os.environ['talker']

model_file = os.environ['model_file']
experiment = os.environ['experiment']

auto_run = os.environ['auto_run']

# export_file = "teste.txt"
# config_file = "teste_config.txt"

def execute_model():
    #cmd = "netlogo-headless.bat --model teste6_fitness_desvio.nlogo --experiment experiment2"
    # cmd = "netlogo-headless.bat --model "+'"C:\\Program Files\\NetLogo 6.0.4\\teste6_fitness_desvio.nlogo"'+" --experiment experiment2"
    #cmd = "/opt/netlogo/netlogo-headless.sh --model /teste/novo_model.nlogo --experiment experiment3"
    
    #time.sleep(10)

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
        #s.bind(('modelo', 9999))
        s.listen(2)

        while True:
            conn, addr = s.accept()
            print("Conexao estabelecida com %s" % str(addr))
            received_message = bytes.decode(conn.recv(1024))
            print ("Mensagem recebida:")

            #received_message = [{"id": 1, "sugar": 6, "metabolism": 3, "vision": 5}, {"id": 2, "sugar": 5, "metabolism": 2, "vision": 2}]        
            print(received_message)
            #received_message = json.dumps(received_message)
            #x = json.loads(received_message, object_hook=lambda d: SimpleNamespace(**d))
            x = json.loads(received_message)
            print(x)
            print("typex")
            print(type(x))

            # for line in x:
            #         for key, value in line.items():
            #             print("The key and value are ({}) = ({})".format(key, value))

            conf_parameters = []

            print ("------------")
            #received_message = ["{\"id\": 1, \"position\": 9}", "{\"id\": 2, \"position\": 60}"]
            for msg in x:
                print("message:")
                print(msg)
                #print(type(msg))

                # temp_string = ""
                # temp_string += "agent"
                temp_list = []
                temp_list.append("agent")

                # for line in msg:
                for key, value in msg.items():
                    #print("The key and value are ({}) = ({})".format(key, value))
                    print("The key and value are ({})".format(value))
                    #temp_string += " "+param
                    temp_list.append(value)
                conf_parameters.append(temp_list)
                print ("conf_parameters")
                print(conf_parameters)

                #message = str(message).replace('"',"'")
                #x = json.loads(message, object_hook=lambda d: SimpleNamespace(**d))


                # print ("msg.id:")
                # print (msg.id)
                # print ("msg.position")
                # print (msg.position)
                # conf_parameters.append(["agent", int(msg.id), int(msg.position)])

                # temp_string = ""
                # temp_string += "agent"
                # for param in msg:
                #     print("param")
                #     print (param)
                #     temp_string += " "+param
                #     # print ("param:")
                #     # print (param)
                #     # print ("msg.sugar")
                #     # print (g.sugar)
                #     # print ("msg.metabolism")
                #     # print (msg.metabolism)
                #     # print ("msg.vision")
                #     # print (msg.vision)
                #     # conf_parameters.append(["agent", int(msg.id), int(msg.sugar), int(msg.metabolism), int(msg.vision)])
                # print ("temp_string:")
                # print (temp_string)
                # conf_parameters.append([temp_string])
                
            # conf_parameters.append(["config_file", config_file])
            # conf_parameters.append(["export_file", export_file])
            
            #conf_parameters.append(["num_agents", int(os.environ['num_agents'])])

            #open('config.txt', 'w').close()

            # with open("/teste/config.txt", "w") as output:
            with open(config_file, "w") as output:
                for x in conf_parameters:

                    x[0] = x[0].replace('"', '')
                    #if (type(x[1]) == str)

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


            # TALVEZ NÃO PRECISE MAIS
            # with open(export_file,"r") as f:
            #     first_line = f.readline()
            #     content_file = first_line[1:]

            # print (content_file)
            # content_file = content_file.replace('"', '')
            # chunks = content_file.split(' ')

            # queue = []
            # for elements in chunks:
            #     element = elements.split('/')
            #     agent_id = element[0]
            #     print ("agent id:"+agent_id)
            #     action = element[1]
            #     print ("action:"+action)

            #     m = {"id": agent_id, "action": action}
            #     queue.append(m)
                

            #JANEIRO, COMEÇANDO GIT, TALVEZ NÃO PRECISE MAIS
            # command = json.dumps(queue)
            # print ("Enviando para o servidor:"+command)

            # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # # print(socket.gethostname())
            # #sock.connect(('talker'+agent_id, 9999))
            # sock.connect((talker, 9999))
            # sock.sendall(command.encode())

            
            # TALVEZ NÃO PRECISE MAIS
            # print ("Excluindo export_file")
            # delete_file(export_file)
            # print ("Excluindo config_file")
            # delete_file(config_file)


            # ------------PARTE DO SOCKET------------------------
            # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # m = {"id": agent_id, "action": action} # a real dict.


            # # m = {"id": str(randrange(10)), "action": best.fitness} # a real dict.
            # command = json.dumps(m)

            # print ("Enviando para o servidor:"+command)
            # sock.connect(('talker', 9999))
            # sock.sendall(command.encode())