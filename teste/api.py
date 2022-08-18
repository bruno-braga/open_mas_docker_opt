import flask
from flask import request, jsonify
import sqlite3

import mysql.connector
from mysql.connector import errorcode

import random

import os
import re
import json

import time

#https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True



@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

@app.route('/api/v1/resources/output_php', methods=['GET'])
def output_php():

  print("ooo")

  query_parameters = request.args
  modelo = query_parameters.get('model')

  return_list = []
  to_update = []

  connected = False
  while (connected == False):
    try:
      cnx = mysql.connector.connect(user='root', password='root',
                                     host='db',
                                     database='MYSQL_DATABASE')
      cursor = cnx.cursor()
      connected = cnx.is_connected()
    except:
      print("Error connecting to the DB")
      time.sleep(3)

  query = "SELECT MAX(id) AS id, agent_id, MAX(data) AS data, MAX(path) AS path, MAX(proccessed) AS proccessed FROM "+modelo+" GROUP BY agent_id ORDER BY agent_id ASC";
  cursor.execute(query)

  for (id, agent_id, data, path, proccessed) in cursor:
    print("iii")
    return_list.append([agent_id, data, path, proccessed])
    to_update.append(id)

  cursor.close()

  cnx.close()
  print("enviando: "+str(return_list))
  return jsonify(return_list)

@app.route('/api/v1/resources/check_new_agents_1', methods=['GET'])
def check_new_agentss_1():

  query_parameters = request.args
  modelo = query_parameters.get('model')

  return_list = []
  to_update = []

  connected = False
  while (connected == False):
    try:
      cnx = mysql.connector.connect(user='root', password='root',
                                     host='db',
                                     database='MYSQL_DATABASE')
      cursor = cnx.cursor()
      connected = cnx.is_connected()
    except:
      print("Error connecting to the DB")
      time.sleep(3)
  query = ("SELECT id, agent_id, data, path, proccessed FROM "+modelo+" "
            "WHERE proccessed = %s AND %s ORDER BY created_at ASC LIMIT 1")

  cursor.execute(query, (0, "1=1"))

  for (id, agent_id, data, path, proccessed) in cursor:
    return_list.append([agent_id, data, path])
    to_update.append(id)

  cursor.close()

  for tupla in to_update:
    try:
      cursor = cnx.cursor()
      temporary_query = "UPDATE "+modelo+" SET proccessed = 1 WHERE id = "+str(tupla)+"; "
      query = (temporary_query)
      cursor.execute(temporary_query)
      cnx.commit()
    except mysql.connector.Error as err:
      print("Failed inserting on database: {}".format(err))
      teste_exception(err)
    finally:
      cursor.close()

  cnx.close()
  print("enviando: "+str(return_list))
  return jsonify(return_list)

@app.route('/api/v1/resources/check_new_agents', methods=['GET'])
def check_new_agentss():

  query_parameters = request.args
  modelo = query_parameters.get('model')

  return_list = []
  to_update = []

  connected = False
  while (connected == False):
    try:
      cnx = mysql.connector.connect(user='root', password='root',
                                     host='db',
                                     database='MYSQL_DATABASE')
      cursor = cnx.cursor()
      connected = cnx.is_connected()
    except:
      print("Error connecting to the DB")
      time.sleep(3)
  query = ("SELECT id, agent_id, data, path, proccessed FROM "+modelo+" "
            "WHERE proccessed = %s AND %s")

  cursor.execute(query, (0, "1=1"))

  for (id, agent_id, data, path, proccessed) in cursor:
    return_list.append([agent_id, data, path])
    to_update.append(id)

  cursor.close()

  for tupla in to_update:
    try:
      cursor = cnx.cursor()
      temporary_query = "UPDATE "+modelo+" SET proccessed = 1 WHERE id = "+str(tupla)+"; "
      query = (temporary_query)
      cursor.execute(temporary_query)
      cnx.commit()
    except mysql.connector.Error as err:
      print("Failed inserting on database: {}".format(err))
      teste_exception(err)
    finally:
      cursor.close()

  cnx.close()
  print("enviando: "+str(return_list))
  return jsonify(return_list)

@app.route('/api/v1/resources/sanity_test', methods=['GET'])
def sanity_test():

  query_parameters = request.args
  modelo = query_parameters.get('model')

  return_list = []
  to_update = []

  m1_alive = []
  m2_alive = []
  m3_alive = []

  m1_on_db = []
  m2_on_db = []
  m3_on_db = []

  on_router = []

  connected = False
  while (connected == False):
    try:
      cnx = mysql.connector.connect(user='root', password='root',
                                     host='db',
                                     database='MYSQL_DATABASE')
      cursor = cnx.cursor()
      connected = cnx.is_connected()
    except:
      print("Error connecting to the DB")
      time.sleep(3)

  cursor = cnx.cursor()
  query = ("SELECT agent_id FROM m1 WHERE proccessed = 0 ORDER BY agent_id")
  cursor.execute(query)
  for agent_id in cursor:
    string1 = str(agent_id)
    agent_id_part = int(re.search(r'\d+', string1).group())
    m1_on_db.append(agent_id_part)
  cursor.close()

  print("m1_on_db:")
  print(m1_on_db)

  cursor = cnx.cursor()
  query = ("SELECT agent_id FROM m2 WHERE proccessed = 0 ORDER BY agent_id")
  cursor.execute(query)
  for agent_id in cursor:
    string1 = str(agent_id)
    agent_id_part = int(re.search(r'\d+', string1).group())
    m2_on_db.append(agent_id_part)
  cursor.close()

  print("m2_on_db:")
  print(m2_on_db)

  cursor = cnx.cursor()
  query = ("SELECT agent_id FROM m3 WHERE proccessed = 0 ORDER BY agent_id")
  cursor.execute(query)
  for agent_id in cursor:
    string1 = str(agent_id)
    agent_id_part = int(re.search(r'\d+', string1).group())
    m3_on_db.append(agent_id_part)
  cursor.close()

  print("m3_on_db:")
  print(m3_on_db)

  fname = "/teste/important/m1_alive.txt"
  if(os.path.isfile(fname)):
    f = open(fname, "r")
    text = f.read()
    text = text[1:]
    print(text)
  m1_alive = [int(x) for x in text.split()]

  print("m1_alive:")
  print(m1_alive)

  fname = "/teste/important/m2_alive.txt"
  if(os.path.isfile(fname)):
    f = open(fname, "r")
    text = f.read()
    text = text[1:]
    print(text)
  m2_alive = [int(x) for x in text.split()]

  print("m2_alive:")
  print(m2_alive)

  cursor = cnx.cursor()
  query = ("SELECT agent_id FROM m3 WHERE proccessed = 1 ORDER BY id DESC LIMIT 1")
  cursor.execute(query)
  for agent_id in cursor:
    string1 = str(agent_id)
    agent_id_part = int(re.search(r'\d+', string1).group())
    m3_alive.append(agent_id_part)
  cursor.close()

  print("m3_alive:")
  print(m3_alive)

  cursor = cnx.cursor()
  query = ("SELECT agent_id FROM router WHERE proccessed = 0 ORDER BY agent_id")
  cursor.execute(query)
  for agent_id in cursor:
    string1 = str(agent_id)
    agent_id_part = int(re.search(r'\d+', string1).group())
    on_router.append(agent_id_part)
  cursor.close()

  print("on_router:")
  print(on_router)

  return_list = []

  # m3_on_db.remove(8)
  # m3_on_db.remove(19)

  print("-----------------------TEST-----------------------")
  # Test if all agent_id from 1 to 799 is in any of the normal conditions
  for x in range(1, 800):
    if x not in m1_alive and x not in m2_alive and x not in m3_alive and x not in m1_on_db and x not in m2_on_db and x not in m3_on_db and x not in on_router:
      print(str(x)+" not found")
      return_list.append({'id': x, 'error': "not found"})

  # https://stackoverflow.com/questions/4446380/python-check-the-occurrences-in-a-list-against-a-value
  # Test for duplicated values
  lst = m1_alive + m2_alive + m3_alive + m1_on_db + m2_on_db + m3_on_db + on_router

  # lst.append(11)
  # lst.append(700)


  count={}
  for item in lst:
    if(lst.count(item) != 1):
      print("Error on item: "+str(item))
      new_value = {'id': str(item), 'error': "duplicated"}
      if(new_value not in return_list):
        return_list.append(new_value)


  # Test if m3 tuples has files:

  m3_proccessed_agents = []
  cursor = cnx.cursor()
  query = ("SELECT agent_id FROM m3 WHERE proccessed = 1 ORDER BY agent_id")
  cursor.execute(query)
  for agent_id in cursor:
    string1 = str(agent_id)
    agent_id_part = int(re.search(r'\d+', string1).group())
    m3_proccessed_agents.append(agent_id_part)
  cursor.close()

  #Alive agent
  m3_alive_agent = m3_alive[0]

  for agent_id in m3_proccessed_agents:
    fname = "/teste/jacamo/integra_gold_miners/src/agt/list/"+str(agent_id)+".asl"
    if(not os.path.isfile(fname)):
      if(agent_id != m3_alive_agent):
        print(str(agent_id)+ " asl file does not exists")
        new_value = {'id': str(agent_id), 'error': "asl file does not exists"}
        return_list.append(new_value)

  cnx.close()
  
  if(len(return_list) == 0):
    new_value = {'id': str(0), 'error': "none"}
    return_list.append(new_value)

  return jsonify(return_list)


@app.route('/api/v1/resources/solicita_cartorio', methods=['POST'])
def solicita_cartorio():
  json_data = request.get_json()
  print(json_data)
  model = json_data['model']
  model_number = model[1:]
  min = json_data['min']
  max = json_data['max']

  connected = False
  while (connected == False):
    try:
      cnx = mysql.connector.connect(user='root', password='root',
                                     host='db',
                                     database='MYSQL_DATABASE')
      cursor = cnx.cursor()
      connected = cnx.is_connected()
    except:
      print("Error connecting to the DB")
      time.sleep(3)
  retorno = False
  for agent_id in range(min, max):
    cursor = cnx.cursor()

    data = "[" + str(random.randint(5, 25)) + " " + str(random.randint(1, 4)) + " " + str(random.randint(1, 6)) + "]"
    sql1 = "INSERT INTO "+model+ " (agent_id, data, path) "+"VALUES ('"+str(agent_id)+"', '"+data+"', "+"''"+");"
    try:
        cursor.execute(sql1)
        # Make sure data is committed to the database
        cnx.commit()
        retorno = True
    except mysql.connector.Error as err:
        print("Failed inserting on database: {}".format(err))
        teste_exception(err)
        retorno = False
    finally:
        cursor.close()

    if (retorno == False):
        break

  cnx.close()
  if(retorno):
    return 'true'
  else:
    return 'false'


@app.route('/api/v1/resources/model_to_router', methods=['POST'])
def teste_envio():
  json_data = request.get_json()
  print(json_data)
  agent_id = json_data['agent_id']
  data = json_data['data']
  path = json_data['path']

  connected = False
  while (connected == False):
    try:
      cnx = mysql.connector.connect(user='root', password='root',
                                     host='db',
                                     database='MYSQL_DATABASE')
      cursor = cnx.cursor()
      connected = cnx.is_connected()
    except:
      print("Error connecting to the DB")
      time.sleep(3)

  add_agent = ("INSERT INTO router "
                 "(agent_id, data, path) "
                 "VALUES (%s, %s, %s)")

  data_agent = (agent_id, data, path)
  try:
    cursor.execute(add_agent, data_agent)
    # Make sure data is committed to the database
    cnx.commit()
    retorno = True
  except mysql.connector.Error as err:
    print("Failed inserting on database: {}".format(err))
    teste_exception(err)
    retorno = False

  cursor.close()
  cnx.close()
  if(retorno):
    return 'true'
  else:
    return 'false'

app.run(host="0.0.0.0", port=5000)