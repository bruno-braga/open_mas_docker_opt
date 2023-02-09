#!/usr/bin/python
#-*- coding: latin-1 -*-

#https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html

import mysql.connector
from mysql.connector import errorcode

import random

import time

import requests

import os

host = os.environ['host']
#host = "api"
#host = "144.22.197.41"
port = "5000"


def testing_exception(error):
  raise Exception(error)

def solicita_register(model, min, max):
  start = time.time()
  print("Start time solicita_register: "+str(start))
  print("Host: "+host)
  # start = time.time()
  # print("hello")
  # end = time.time()
  # print(end - start)
  retorno = False
  while retorno == False:
    try:
      # response = requests.post('http://localhost:5000/api/v1/resources/solicita_register', json = {"model":model, "min":min, "max":max}, timeout=5)
      # response = requests.post('http://api:5000/api/v1/resources/solicita_register', json = {"model":model, "min":min, "max":max}, timeout=120)
      

      # response = requests.post('http://api:5000/api/v1/resources/solicita_register', json = {"model":model, "min":min, "max":max})
      
      #response = requests.post('http://api:5000/api/v1/resources/register_agents_on_platform', json = {"model":model, "min":min, "max":max})
      response = requests.post('http://'+host+':'+port+'/api/v1/resources/register_agents_on_platform', json = {"model":model, "min":min, "max":max}, timeout=120)
      print("Response from API: "+response.text)
      response.raise_for_status()

      #print(response)
      print("Function worked well")
      retorno = True
    except requests.exceptions.HTTPError as errh:
        print(errh)
        print("Error type 1, sleeping and retrying")
        time.sleep(1)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
        print("Error type 2, sleeping and retrying")
        time.sleep(1)
    except requests.exceptions.Timeout as errt:
        print(errt)
        print("Error type 3, sleeping and retrying")
        time.sleep(1)
    except requests.exceptions.RequestException as err:
        print(err)
        print("Error type 4, sleeping and retrying")
        time.sleep(1)

  print("Left loop")
  end = time.time()
  print("End time solicita_register: "+str(end - start))
  return retorno

def send_agent_to_alive(agent_id, model):
  start = time.time()
  print("Start time send_agent_to_alive: "+str(start))
  retorno = False
  while retorno == False:
    try:
      # response = requests.post('http://localhost:5000/api/v1/resources/model_to_router', json = {"agent_id":agent_id, "data":data, "path":path}, timeout=5)
      #response = requests.post('http://api:5000/api/v1/resources/model_to_router', json = {"agent_id":agent_id, "data":data, "path":path}, timeout=5)
      
      #response = requests.post('http://api:5000/api/v1/resources/model_to_alive', json = {"agent_id":agent_id, "model":model})
      response = requests.post('http://'+host+':'+port+'/api/v1/resources/model_to_alive', json = {"agent_id":agent_id, "model":model}, timeout=120)
      response.raise_for_status()

      #print(response)
      print("Function worked well")
      retorno = True
    except requests.exceptions.HTTPError as errh:
        print(errh)
        print("Error type 1, sleeping and retrying")
        time.sleep(1)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
        print("Error type 2, sleeping and retrying")
        time.sleep(1)
    except requests.exceptions.Timeout as errt:
        print(errt)
        print("Error type 3, sleeping and retrying")
        time.sleep(1)
    except requests.exceptions.RequestException as err:
        print(err)
        print("Error type 4, sleeping and retrying")
        time.sleep(1)

  print("Left loop")
  end = time.time()
  print("End time send_agent_to_alive: "+str(end - start))
  return retorno

def send_agent_to_router(agent_id, data, path):
  start = time.time()
  print("Start time send_agent_to_router: "+str(start))
  retorno = False
  while retorno == False:
    try:
      # response = requests.post('http://localhost:5000/api/v1/resources/model_to_router', json = {"agent_id":agent_id, "data":data, "path":path}, timeout=5)
      #response = requests.post('http://api:5000/api/v1/resources/model_to_router', json = {"agent_id":agent_id, "data":data, "path":path}, timeout=5)
      
      #response = requests.post('http://api:5000/api/v1/resources/model_to_router', json = {"agent_id":agent_id, "data":data, "path":path})
      response = requests.post('http://'+host+':'+port+'/api/v1/resources/model_to_router', json = {"agent_id":agent_id, "data":data, "path":path}, timeout=120)
      response.raise_for_status()

      #print(response)
      print("Function worked well")
      retorno = True
    except requests.exceptions.HTTPError as errh:
        print(errh)
        print("Error type 1, sleeping and retrying")
        time.sleep(1)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
        print("Error type 2, sleeping and retrying")
        time.sleep(1)
    except requests.exceptions.Timeout as errt:
        print(errt)
        print("Error type 3, sleeping and retrying")
        time.sleep(1)
    except requests.exceptions.RequestException as err:
        print(err)
        print("Error type 4, sleeping and retrying")
        time.sleep(1)

  print("Left loop")
  end = time.time()
  print("End time send_agent_to_router: "+str(end - start))
  return retorno

def receiving_agents(modelo):
  start = time.time()
  print("Start time receiving_agents: "+str(start))
  str1 = ''
  return_list = []
  retorno = False
  while retorno == False:
    try:
      # response = requests.get('http://localhost:5000/api/v1/resources/check_new_agents', params={"model":modelo}, timeout=5)
      # response = requests.get('http://api:5000/api/v1/resources/check_new_agents', params={"model":modelo}, timeout=5)
      
      #response = requests.get('http://api:5000/api/v1/resources/check_new_agents', params={"model":modelo})
      response = requests.get('http://'+host+':'+port+'/api/v1/resources/check_new_agents', params={"model":modelo}, timeout=120)
      response.raise_for_status()
      return_list = response.json()

      print("Function worked well")
      retorno = True    
      #str1 = ''.join(str(e) for e in response.json())
    except requests.exceptions.HTTPError as errh:
        print(errh)
        print("Error type 1, sleeping and retrying")
        time.sleep(1)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
        print("Error type 2, sleeping and retrying")
        time.sleep(1)
    except requests.exceptions.Timeout as errt:
        print(errt)
        print("Error type 3, sleeping and retrying")
        time.sleep(1)
    except requests.exceptions.RequestException as err:
        print(err)
        print("Error type 4, sleeping and retrying")
        time.sleep(1)
  # return str1
  print("Left loop")
  end = time.time()
  print("End time receiving_agents: "+str(end - start))
  return return_list

# def send_function(string_to_send):
#     return "3"

def process_agents_on_router():
  #router_type = "random"
  router_type = "sequential"
  print("Router type:"+router_type)
  connected = False
  while (connected == False):
    try:
      cnx = mysql.connector.connect(user='root', password='root',
                               host='db',
                               database='MYSQL_DATABASE')
      connected = cnx.is_connected()
    except:
      print("Error connecting to the database")
      time.sleep(3)
  cursor = cnx.cursor()

  # print("Connected to the DB successfully")

  if(router_type == "random"):
    order = "RAND()"
  elif(router_type == "sequential"):
    order = "created_at ASC"

  query = ("SELECT id, agent_id, data, path, processed FROM router "
            "WHERE processed = 0 ORDER BY "+order)
  modelos_list = ["m1", "m2", "m3"]
  #model_to_send = random.choice(modelos_list)
  cursor.execute(query)


  return_list = []
  delete_list = []

  for (id, agent_id, data, path, processed) in cursor:
    return_list.append([agent_id, data, path, id])

  cursor.close()
  # modelos_list = ["m1", "m2", "m3"]

  cnx.close()

  for tupla in return_list:
    cnx = mysql.connector.connect(user='root', password='root',
                               host='db',
                               database='MYSQL_DATABASE')
    cursor = cnx.cursor()
    cnx.start_transaction()

    model_to_send = random.choice(modelos_list)

    agent_id = str(tupla[0])
    data = tupla[1]
    path = tupla[2]
    tupla_id = str(tupla[3])
    processed = str(0)

    sql1 = "INSERT INTO "+model_to_send+ " (agent_id, data, path, processed) "+"VALUES ('"+agent_id+"', '"+data+"', '"+path+"', '"+processed+"');"
    sql2 = "UPDATE router SET processed = 1 WHERE id = "+tupla_id+"; "
    try:
      cursor.execute(sql1)
      cursor.execute(sql2)
      # Make sure data is committed to the database
      cnx.commit()
      print("Agent_id: "+agent_id+" sended to model "+model_to_send)
    # except mysql.connector.ProgrammingError as err:
    except mysql.connector.Error as err:
      print("Failed inserting on database: {}".format(err))
      print("Rolling back ...")
      print(e)
      db.rollback()  # rollback changes
      testing_exception(err)
    # except errors.Error as e:
    #   print("Rolling back ...")
    #   print(e)
    #   db.rollback()  # rollback changes
    finally:
      cursor.close()
      cnx.close()

def backup_funcional_process_agents_on_router():
  while True:
    cnx = mysql.connector.connect(user='root', password='root',
                                 host='db',
                                 database='MYSQL_DATABASE')
    cursor = cnx.cursor()
    query = ("SELECT id, agent_id, data, path, processed FROM router "
              "WHERE processed = 0")
    cursor.execute(query)


    return_list = []
    delete_list = []

    for (id, agent_id, data, path, processed) in cursor:
      return_list.append([agent_id, data, path, id])

    cursor.close()
    modelos_list = ["m1", "m2", "m3"]

    cnx.close()

    for tupla in return_list:
      cnx = mysql.connector.connect(user='root', password='root',
                                 host='db',
                                 database='MYSQL_DATABASE')
      cursor = cnx.cursor()
      cnx.start_transaction()

      model_to_send = random.choice(modelos_list)

      agent_id = str(tupla[0])
      data = tupla[1]
      path = tupla[2]
      tupla_id = str(tupla[3])
      processed = str(0)

      sql1 = "INSERT INTO "+model_to_send+ " (agent_id, data, path, processed) "+"VALUES ('"+agent_id+"', '"+data+"', '"+path+"', '"+processed+"');"
      sql2 = "UPDATE router SET processed = 1 WHERE id = "+tupla_id+"; "
      try:
        cursor.execute(sql1)
        cursor.execute(sql2)
        # Make sure data is committed to the database
        cnx.commit()
        print("Agent_id: "+agent_id+" sended to model "+model_to_send)
      # except mysql.connector.ProgrammingError as err:
      except mysql.connector.Error as err:
        print("Failed inserting on database: {}".format(err))
        print("Rolling back ...")
        print(e)
        db.rollback()  # rollback changes
        testing_exception(err)
      # except errors.Error as e:
      #   print("Rolling back ...")
      #   print(e)
      #   db.rollback()  # rollback changes
      finally:
        cursor.close()
        cnx.close()


  # while True:
  #   cnx = mysql.connector.connect(user='root', password='root',
  #                                host='db',
  #                                database='MYSQL_DATABASE')
  #   cursor = cnx.cursor()
  #   query = ("SELECT id, agent_id, data, path, processed FROM router "
  #             "WHERE processed = 0")
  #   cursor.execute(query)


  #   return_list = []
  #   delete_list = []

  #   for (id, agent_id, data, path, processed) in cursor:
  #     return_list.append([agent_id, data, path, id])

  #   cursor.close()
  #   modelos_list = ["m1"]

  #   for tupla in return_list:
  #     cnx = mysql.connector.connect(user='root', password='root',
  #                                host='db',
  #                                database='MYSQL_DATABASE')
  #     cursor = cnx.cursor()
  #     cnx.start_transaction()

  #     model_to_send = random.choice(modelos_list)

  #     agent_id = str(tupla[0])
  #     data = tupla[1]
  #     path = tupla[2]
  #     tupla_id = str(tupla[3])
  #     processed = str(0)

  #     sql1 = "INSERT INTO "+model_to_send+ " (agent_id, data, path, processed) "+"VALUES ('"+agent_id+"', '"+data+"', '"+path+"', '"+processed+"');"
  #     sql2 = "UPDATE router SET processed = 1 WHERE id = "+tupla_id+"; "
  #     try:
  #       cursor.execute(sql1)
  #       cursor.execute(sql2)
  #       # Make sure data is committed to the database
  #       cnx.commit()
  #     except errors.Error as e:
  #       db.rollback()  # rollback changes
  #       print("Rolling back ...")
  #       print(e)
  #     finally:
  #       cursor.close()
  #       cnx.close()


def print_solicita_register(model, qtd):

  cnx = mysql.connector.connect(user='root', password='root',
                                 host='db',
                                 database='MYSQL_DATABASE')
  retorno = False
  for agent_id in range(1, qtd):
    cursor = cnx.cursor()
    # add_agent = ("INSERT INTO router "
    #              "(agent_id, data) "
    #              "VALUES (%s, %s)")
    # data = [random.randint(5, 25) random.randint(1, 4) random.randint(1, 6)]
    # data = []
    # data.append(random.randint(5, 25))
    # data.append(random.randint(1, 4))
    # data.append(random.randint(1, 6))

    data = "[" + str(random.randint(5, 25)) + " " + str(random.randint(1, 4)) + " " + str(random.randint(1, 6)) + "]"

    print(data)

    # data_agent = (agent_id, data)
    sql1 = "INSERT INTO "+model+ " (agent_id, data) "+"VALUES ('"+str(agent_id)+"', '"+data+"');"

    # # Insert new employee
    # cursor.execute(add_employee, data_employee)
    try:
        # cursor.execute(add_agent, data_agent)
        cursor.execute(sql1)
        # Make sure data is committed to the database
        cnx.commit()
        retorno = True
    except mysql.connector.Error as err:
        print("Failed inserting on database: {}".format(err))
        retorno = False
    finally:
        cursor.close()

    if (retorno == False):
        break

  cnx.close()
  return retorno

def print_send_agent_to_router(agent_id, data, path):

  cnx = mysql.connector.connect(user='root', password='root',
                                 host='db',
                                 database='MYSQL_DATABASE')
  cursor = cnx.cursor()

  # tomorrow = datetime.now().date() + timedelta(days=1)

  print(agent_id)
  print(data)
  print(path)

  # print(string_recebida)
  # string_filtrada = string_recebida.split()
  # for agent_id, data, path in string_filtrada:
  #   print(agent_id)
  #   print(data)
  #   print(path)

  add_agent = ("INSERT INTO router "
                 "(agent_id, data, path) "
                 "VALUES (%s, %s, %s)")

  data_agent = (agent_id, data, path)

  # # Insert new employee
  # cursor.execute(add_employee, data_employee)
  try:
    cursor.execute(add_agent, data_agent)
    # Make sure data is committed to the database
    cnx.commit()
    retorno = True
  except mysql.connector.Error as err:
    print("Failed inserting on database: {}".format(err))
    retorno = False

  # if (cursor.execute(add_employee, data_employee)):
  #   print("dale")
  # else:
  #   print("dele")

  # # Make sure data is committed to the database
  # cnx.commit()

  cursor.close()
  cnx.close()
  return retorno

def print_receiving_agents(modelo):

  return_list = []
  to_update = []

  cnx = mysql.connector.connect(user='root', password='root',
                                 host='db',
                                 database='MYSQL_DATABASE')
  cursor = cnx.cursor()
  query = ("SELECT id, agent_id, data, path, processed FROM "+modelo+" "
            "WHERE processed = %s AND %s")

  # print("modelo:"+modelo)
  cursor.execute(query, (0, "1=1"))

  for (id, agent_id, data, path, processed) in cursor:
    print("id: {}, agent_id: {}, data: {}, path: {}, processed: {}".format(
      id, agent_id, data, path, processed))
    return_list.append([agent_id, data, path])
    to_update.append(id)

  cursor.close()

  print(to_update)

  for tupla in to_update:
    cursor = cnx.cursor()
    temporary_query = "UPDATE "+modelo+" SET processed = 1 WHERE id = "+str(tupla)+"; "
    print("temporary query:"+temporary_query)
    query = (temporary_query)
    cursor.execute(temporary_query)
    cnx.commit()
    cursor.close()

  # print("modelo:"+modelo)

  cnx.close()

  # for tupla in return_list:
  #   print("tupla: "+tupla)
  return return_list

def print_send_function(string_to_send):
    return "3"

def print_process_agents_on_router():
  #while True:
  cnx = mysql.connector.connect(user='root', password='root',
                               host='db',
                               database='MYSQL_DATABASE')
  cursor = cnx.cursor()
  query = ("SELECT id, agent_id, data, path, processed FROM router "
            "WHERE processed = 0")

  # print("modelo:"+modelo)
  cursor.execute(query)


  return_list = []
  delete_list = []

  print("lendo router: ")

  for (id, agent_id, data, path, processed) in cursor:
    print("id: {}, agent_id: {}, data: {}, path: {}, processed: {}".format(
      id, agent_id, data, path, processed))
    return_list.append([agent_id, data, path, id])


  print(return_list)

  cursor.close()

  # cursor.close()
  # cnx.close()

  # modelos_list = ["m1","m2","m3"]
  modelos_list = ["m1"]

  for tupla in return_list:
    cnx = mysql.connector.connect(user='root', password='root',
                               host='db',
                               database='MYSQL_DATABASE')
    cursor = cnx.cursor()
    cnx.start_transaction()

    model_to_send = random.choice(modelos_list)

    print("tupla: "+str(tupla[0])+" indo para modelo : "+model_to_send)

    agent_id = str(tupla[0])
    data = tupla[1]
    path = tupla[2]
    tupla_id = str(tupla[3])
    processed = str(0)

    sql1 = "INSERT INTO "+model_to_send+ " (agent_id, data, path, processed) "+"VALUES ('"+agent_id+"', '"+data+"', '"+path+"', '"+processed+"');"
    sql2 = "UPDATE router SET processed = 1 WHERE id = "+tupla_id+"; "


    # full_query = "START TRANSACTION; "
    # full_query += "INSERT INTO "+model_to_send+ " (data, processed) "+"VALUES ('"+tupla[0]+"' ,0); "
    # # full_query += "DELETE FROM router WHERE id = "+str(tupla[1])+"; "
    # full_query += "UPDATE router SET processed = 1 WHERE id = "+str(tupla[1])+"; "
    # full_query += "COMMIT;"

    # full_query = "START TRANSACTION; "
    # full_query += "INSERT INTO "+model_to_send+ " (data, processed) "+"VALUES ('"+tupla[0]+"' ,0); "
    # # full_query += "DELETE FROM router WHERE id = "+str(tupla[1])+"; "
    # full_query += "UPDATE router SET processed = 1 WHERE id = "+str(tupla[1])+"; "
    # full_query += "COMMIT;"

    # full_query = "START TRANSACTION; "
    # full_query += "INSERT INTO "+model_to_send+ " (data, processed) "+"VALUES (%s, %s); "
    # full_query += "DELETE FROM router WHERE id = %s "
    # full_query += "COMMIT;"

    # print("full query: "+full_query)
    # add_employee = ("INSERT INTO "+model_to_send+ " "
    #                "(data, processed) "
    #                "VALUES (%s, %s)")

    # data_employee = (tupla[0], 0, str(tupla[1]))

    # # Insert new employee
    # cursor.execute(add_employee, data_employee)
    try:
      # cursor.execute(full_query, data_employee)
      cursor.execute(sql1)
      cursor.execute(sql2)
      # Make sure data is committed to the database
      cnx.commit()
    except errors.Error as e:
      db.rollback()  # rollback changes
      print("Rolling back ...")
      print(e)
    finally:
      cursor.close()
      cnx.close()
    
  # cnx.close()

  # cursor.close()
  # cnx.close()

  # for tupla in return_list:
  #   print("tupla: "+tupla)
  return return_list


## BACKUP, FUNCIONA, ANTES DE ACESSAR API
# def testing_exception(error):
#   raise Exception(error)

# def solicita_register(model, min, max):

#   cnx = mysql.connector.connect(user='root', password='root',
#                                  host='db',
#                                  database='MYSQL_DATABASE')
#   retorno = False
#   for agent_id in range(min, max):
#     cursor = cnx.cursor()
#     # add_agent = ("INSERT INTO router "
#     #              "(agent_id, data) "
#     #              "VALUES (%s, %s)")
#     # data = [random.randint(5, 25) random.randint(1, 4) random.randint(1, 6)]
#     # data = []
#     # data.append(random.randint(5, 25))
#     # data.append(random.randint(1, 4))
#     # data.append(random.randint(1, 6))

#     data = "[" + str(random.randint(5, 25)) + " " + str(random.randint(1, 4)) + " " + str(random.randint(1, 6)) + "]"

#     # print(data)

#     # data_agent = (agent_id, data)
#     sql1 = "INSERT INTO "+model+ " (agent_id, data, path) "+"VALUES ('"+str(agent_id)+"', '"+data+"', "+"''"+");"
#     # print("sql1: "+sql1)

#     # # Insert new employee
#     # cursor.execute(add_employee, data_employee)
#     try:
#         # cursor.execute(add_agent, data_agent)
#         cursor.execute(sql1)
#         # Make sure data is committed to the database
#         cnx.commit()
#         retorno = True
#     # except mysql.connector.ProgrammingError as err:
#     except mysql.connector.Error as err:
#         print("Failed inserting on database: {}".format(err))
#         testing_exception(err)
#         retorno = False
#     finally:
#         cursor.close()

#     if (retorno == False):
#         break

#   cnx.close()
#   return retorno

# def testing_sending(agent_id, data, path):

#   cnx = mysql.connector.connect(user='root', password='root',
#                                  host='db',
#                                  database='MYSQL_DATABASE')
#   cursor = cnx.cursor()

#   # tomorrow = datetime.now().date() + timedelta(days=1)

#   # print(agent_id)
#   # print(data)
#   # print(path)

#   # print(string_recebida)
#   # string_filtrada = string_recebida.split()
#   # for agent_id, data, path in string_filtrada:
#   #   print(agent_id)
#   #   print(data)
#   #   print(path)

#   add_agent = ("INSERT INTO router "
#                  "(agent_id, data, path) "
#                  "VALUES (%s, %s, %s)")

#   data_agent = (agent_id, data, path)

#   # # Insert new employee
#   # cursor.execute(add_employee, data_employee)
#   try:
#     cursor.execute(add_agent, data_agent)
#     # Make sure data is committed to the database
#     cnx.commit()
#     retorno = True
#   # except mysql.connector.ProgrammingError as err:
#   except mysql.connector.Error as err:
#     print("Failed inserting on database: {}".format(err))
#     testing_exception(err)
#     retorno = False

#   # if (cursor.execute(add_employee, data_employee)):
#   #   print("dale")
#   # else:
#   #   print("dele")

#   # # Make sure data is committed to the database
#   # cnx.commit()

#   cursor.close()
#   cnx.close()
#   return retorno

# def receiving_agents(modelo):

#   return_list = []
#   to_update = []

#   cnx = mysql.connector.connect(user='root', password='root',
#                                  host='db',
#                                  database='MYSQL_DATABASE')
#   cursor = cnx.cursor()
#   query = ("SELECT id, agent_id, data, path, processed FROM "+modelo+" "
#             "WHERE processed = %s AND %s")

#   # print("modelo:"+modelo)
#   cursor.execute(query, (0, "1=1"))

#   for (id, agent_id, data, path, processed) in cursor:
#     # print("id: {}, agent_id: {}, data: {}, path: {}, processed: {}".format(
#     #   id, agent_id, data, path, processed))
#     return_list.append([agent_id, data, path])
#     to_update.append(id)

#   cursor.close()

#   # print(to_update)

#   for tupla in to_update:
#     try:
#       # cursor.execute(add_agent, data_agent)
#       # # Make sure data is committed to the database
#       # cnx.commit()

#       cursor = cnx.cursor()
#       temporary_query = "UPDATE "+modelo+" SET processed = 1 WHERE id = "+str(tupla)+"; "
#       # print("temporary query:"+temporary_query)
#       query = (temporary_query)
#       cursor.execute(temporary_query)
#       cnx.commit()
#     # except mysql.connector.ProgrammingError as err:
#     except mysql.connector.Error as err:
#       print("Failed inserting on database: {}".format(err))
#       testing_exception(err)
#     finally:
#       cursor.close()

#   # print("modelo:"+modelo)

#   cnx.close()

#   # for tupla in return_list:
#   #   print("tupla: "+tupla)
#   return return_list

# def send_function(string_to_send):
#     return "3"

# def process_agents_on_router():
#   while True:
#     cnx = mysql.connector.connect(user='root', password='root',
#                                  host='db',
#                                  database='MYSQL_DATABASE')
#     cursor = cnx.cursor()
#     query = ("SELECT id, agent_id, data, path, processed FROM router "
#               "WHERE processed = 0")
#     cursor.execute(query)


#     return_list = []
#     delete_list = []

#     for (id, agent_id, data, path, processed) in cursor:
#       return_list.append([agent_id, data, path, id])

#     cursor.close()
#     modelos_list = ["m1", "m2", "m3"]

#     cnx.close()

#     for tupla in return_list:
#       cnx = mysql.connector.connect(user='root', password='root',
#                                  host='db',
#                                  database='MYSQL_DATABASE')
#       cursor = cnx.cursor()
#       cnx.start_transaction()

#       model_to_send = random.choice(modelos_list)

#       agent_id = str(tupla[0])
#       data = tupla[1]
#       path = tupla[2]
#       tupla_id = str(tupla[3])
#       processed = str(0)

#       sql1 = "INSERT INTO "+model_to_send+ " (agent_id, data, path, processed) "+"VALUES ('"+agent_id+"', '"+data+"', '"+path+"', '"+processed+"');"
#       sql2 = "UPDATE router SET processed = 1 WHERE id = "+tupla_id+"; "
#       try:
#         cursor.execute(sql1)
#         cursor.execute(sql2)
#         # Make sure data is committed to the database
#         cnx.commit()
#         print("Agent_id: "+agent_id+" sended to model "+model_to_send)
#       # except mysql.connector.ProgrammingError as err:
#       except mysql.connector.Error as err:
#         print("Failed inserting on database: {}".format(err))
#         print("Rolling back ...")
#         print(e)
#         db.rollback()  # rollback changes
#         testing_exception(err)
#       # except errors.Error as e:
#       #   print("Rolling back ...")
#       #   print(e)
#       #   db.rollback()  # rollback changes
#       finally:
#         cursor.close()
#         cnx.close()


#   # while True:
#   #   cnx = mysql.connector.connect(user='root', password='root',
#   #                                host='db',
#   #                                database='MYSQL_DATABASE')
#   #   cursor = cnx.cursor()
#   #   query = ("SELECT id, agent_id, data, path, processed FROM router "
#   #             "WHERE processed = 0")
#   #   cursor.execute(query)


#   #   return_list = []
#   #   delete_list = []

#   #   for (id, agent_id, data, path, processed) in cursor:
#   #     return_list.append([agent_id, data, path, id])

#   #   cursor.close()
#   #   modelos_list = ["m1"]

#   #   for tupla in return_list:
#   #     cnx = mysql.connector.connect(user='root', password='root',
#   #                                host='db',
#   #                                database='MYSQL_DATABASE')
#   #     cursor = cnx.cursor()
#   #     cnx.start_transaction()

#   #     model_to_send = random.choice(modelos_list)

#   #     agent_id = str(tupla[0])
#   #     data = tupla[1]
#   #     path = tupla[2]
#   #     tupla_id = str(tupla[3])
#   #     processed = str(0)

#   #     sql1 = "INSERT INTO "+model_to_send+ " (agent_id, data, path, processed) "+"VALUES ('"+agent_id+"', '"+data+"', '"+path+"', '"+processed+"');"
#   #     sql2 = "UPDATE router SET processed = 1 WHERE id = "+tupla_id+"; "
#   #     try:
#   #       cursor.execute(sql1)
#   #       cursor.execute(sql2)
#   #       # Make sure data is committed to the database
#   #       cnx.commit()
#   #     except errors.Error as e:
#   #       db.rollback()  # rollback changes
#   #       print("Rolling back ...")
#   #       print(e)
#   #     finally:
#   #       cursor.close()
#   #       cnx.close()


# def print_solicita_register(model, qtd):

#   cnx = mysql.connector.connect(user='root', password='root',
#                                  host='db',
#                                  database='MYSQL_DATABASE')
#   retorno = False
#   for agent_id in range(1, qtd):
#     cursor = cnx.cursor()
#     # add_agent = ("INSERT INTO router "
#     #              "(agent_id, data) "
#     #              "VALUES (%s, %s)")
#     # data = [random.randint(5, 25) random.randint(1, 4) random.randint(1, 6)]
#     # data = []
#     # data.append(random.randint(5, 25))
#     # data.append(random.randint(1, 4))
#     # data.append(random.randint(1, 6))

#     data = "[" + str(random.randint(5, 25)) + " " + str(random.randint(1, 4)) + " " + str(random.randint(1, 6)) + "]"

#     print(data)

#     # data_agent = (agent_id, data)
#     sql1 = "INSERT INTO "+model+ " (agent_id, data) "+"VALUES ('"+str(agent_id)+"', '"+data+"');"

#     # # Insert new employee
#     # cursor.execute(add_employee, data_employee)
#     try:
#         # cursor.execute(add_agent, data_agent)
#         cursor.execute(sql1)
#         # Make sure data is committed to the database
#         cnx.commit()
#         retorno = True
#     except mysql.connector.Error as err:
#         print("Failed inserting on database: {}".format(err))
#         retorno = False
#     finally:
#         cursor.close()

#     if (retorno == False):
#         break

#   cnx.close()
#   return retorno

# def print_testing_sending(agent_id, data, path):

#   cnx = mysql.connector.connect(user='root', password='root',
#                                  host='db',
#                                  database='MYSQL_DATABASE')
#   cursor = cnx.cursor()

#   # tomorrow = datetime.now().date() + timedelta(days=1)

#   print(agent_id)
#   print(data)
#   print(path)

#   # print(string_recebida)
#   # string_filtrada = string_recebida.split()
#   # for agent_id, data, path in string_filtrada:
#   #   print(agent_id)
#   #   print(data)
#   #   print(path)

#   add_agent = ("INSERT INTO router "
#                  "(agent_id, data, path) "
#                  "VALUES (%s, %s, %s)")

#   data_agent = (agent_id, data, path)

#   # # Insert new employee
#   # cursor.execute(add_employee, data_employee)
#   try:
#     cursor.execute(add_agent, data_agent)
#     # Make sure data is committed to the database
#     cnx.commit()
#     retorno = True
#   except mysql.connector.Error as err:
#     print("Failed inserting on database: {}".format(err))
#     retorno = False

#   # if (cursor.execute(add_employee, data_employee)):
#   #   print("dale")
#   # else:
#   #   print("dele")

#   # # Make sure data is committed to the database
#   # cnx.commit()

#   cursor.close()
#   cnx.close()
#   return retorno

# def print_receiving_agents(modelo):

#   return_list = []
#   to_update = []

#   cnx = mysql.connector.connect(user='root', password='root',
#                                  host='db',
#                                  database='MYSQL_DATABASE')
#   cursor = cnx.cursor()
#   query = ("SELECT id, agent_id, data, path, processed FROM "+modelo+" "
#             "WHERE processed = %s AND %s")

#   # print("modelo:"+modelo)
#   cursor.execute(query, (0, "1=1"))

#   for (id, agent_id, data, path, processed) in cursor:
#     print("id: {}, agent_id: {}, data: {}, path: {}, processed: {}".format(
#       id, agent_id, data, path, processed))
#     return_list.append([agent_id, data, path])
#     to_update.append(id)

#   cursor.close()

#   print(to_update)

#   for tupla in to_update:
#     cursor = cnx.cursor()
#     temporary_query = "UPDATE "+modelo+" SET processed = 1 WHERE id = "+str(tupla)+"; "
#     print("temporary query:"+temporary_query)
#     query = (temporary_query)
#     cursor.execute(temporary_query)
#     cnx.commit()
#     cursor.close()

#   # print("modelo:"+modelo)

#   cnx.close()

#   # for tupla in return_list:
#   #   print("tupla: "+tupla)
#   return return_list

# def print_send_function(string_to_send):
#     return "3"

# def print_process_agents_on_router():
#   #while True:
#   cnx = mysql.connector.connect(user='root', password='root',
#                                host='db',
#                                database='MYSQL_DATABASE')
#   cursor = cnx.cursor()
#   query = ("SELECT id, agent_id, data, path, processed FROM router "
#             "WHERE processed = 0")

#   # print("modelo:"+modelo)
#   cursor.execute(query)


#   return_list = []
#   delete_list = []

#   print("lendo router: ")

#   for (id, agent_id, data, path, processed) in cursor:
#     print("id: {}, agent_id: {}, data: {}, path: {}, processed: {}".format(
#       id, agent_id, data, path, processed))
#     return_list.append([agent_id, data, path, id])


#   print(return_list)

#   cursor.close()

#   # cursor.close()
#   # cnx.close()

#   # modelos_list = ["m1","m2","m3"]
#   modelos_list = ["m1"]

#   for tupla in return_list:
#     cnx = mysql.connector.connect(user='root', password='root',
#                                host='db',
#                                database='MYSQL_DATABASE')
#     cursor = cnx.cursor()
#     cnx.start_transaction()

#     model_to_send = random.choice(modelos_list)

#     print("tupla: "+str(tupla[0])+" indo para modelo : "+model_to_send)

#     agent_id = str(tupla[0])
#     data = tupla[1]
#     path = tupla[2]
#     tupla_id = str(tupla[3])
#     processed = str(0)

#     sql1 = "INSERT INTO "+model_to_send+ " (agent_id, data, path, processed) "+"VALUES ('"+agent_id+"', '"+data+"', '"+path+"', '"+processed+"');"
#     sql2 = "UPDATE router SET processed = 1 WHERE id = "+tupla_id+"; "


#     # full_query = "START TRANSACTION; "
#     # full_query += "INSERT INTO "+model_to_send+ " (data, processed) "+"VALUES ('"+tupla[0]+"' ,0); "
#     # # full_query += "DELETE FROM router WHERE id = "+str(tupla[1])+"; "
#     # full_query += "UPDATE router SET processed = 1 WHERE id = "+str(tupla[1])+"; "
#     # full_query += "COMMIT;"

#     # full_query = "START TRANSACTION; "
#     # full_query += "INSERT INTO "+model_to_send+ " (data, processed) "+"VALUES ('"+tupla[0]+"' ,0); "
#     # # full_query += "DELETE FROM router WHERE id = "+str(tupla[1])+"; "
#     # full_query += "UPDATE router SET processed = 1 WHERE id = "+str(tupla[1])+"; "
#     # full_query += "COMMIT;"

#     # full_query = "START TRANSACTION; "
#     # full_query += "INSERT INTO "+model_to_send+ " (data, processed) "+"VALUES (%s, %s); "
#     # full_query += "DELETE FROM router WHERE id = %s "
#     # full_query += "COMMIT;"

#     # print("full query: "+full_query)
#     # add_employee = ("INSERT INTO "+model_to_send+ " "
#     #                "(data, processed) "
#     #                "VALUES (%s, %s)")

#     # data_employee = (tupla[0], 0, str(tupla[1]))

#     # # Insert new employee
#     # cursor.execute(add_employee, data_employee)
#     try:
#       # cursor.execute(full_query, data_employee)
#       cursor.execute(sql1)
#       cursor.execute(sql2)
#       # Make sure data is committed to the database
#       cnx.commit()
#     except errors.Error as e:
#       db.rollback()  # rollback changes
#       print("Rolling back ...")
#       print(e)
#     finally:
#       cursor.close()
#       cnx.close()
    
#   # cnx.close()

#   # cursor.close()
#   # cnx.close()

#   # for tupla in return_list:
#   #   print("tupla: "+tupla)
#   return return_list

































































## SUPER BACKUP DEPOIS DAS TRANSACTIONS, TRANSACTION FUNCIONA
# #!/usr/bin/python
# #-*- coding: latin-1 -*-

# #https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html

# import mysql.connector
# from mysql.connector import errorcode

# import random

# import time

# # from __future__ import print_function

# # print("1")
# # # cnx = mysql.connector.connect(user='root', password='root',
# # #                               host='db',
# # #                               database='MYSQL_DATABASE')
# # try:
# #   cnx = mysql.connector.connect(user='root', password='root',
# #                                host='db',
# #                                database='MYSQL_DATABASE')
# # except mysql.connector.Error as err:
# #   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
# #     print("Something is wrong with your user name or password")
# #   elif err.errno == errorcode.ER_BAD_DB_ERROR:
# #     print("Database does not exist")
# #   else:
# #     print(err)
# # else:
# #   cnx.close()
# # print("2")
# #host="db", user="root", passwd="root", db="MYSQL_DATABASE"

# def testing_sending(string_recebida):

#   cnx = mysql.connector.connect(user='root', password='root',
#                                  host='db',
#                                  database='MYSQL_DATABASE')
#   cursor = cnx.cursor()

#   # tomorrow = datetime.now().date() + timedelta(days=1)

#   add_employee = ("INSERT INTO router "
#                  "(data, processed) "
#                  "VALUES (%s, %s)")

#   data_employee = (string_recebida, 0)

#   # # Insert new employee
#   # cursor.execute(add_employee, data_employee)
#   try:
#     cursor.execute(add_employee, data_employee)
#     # Make sure data is committed to the database
#     cnx.commit()
#     retorno = True
#   except mysql.connector.Error as err:
#     print("Failed inserting on database: {}".format(err))
#     retorno = False

#   # if (cursor.execute(add_employee, data_employee)):
#   #   print("dale")
#   # else:
#   #   print("dele")

#   # # Make sure data is committed to the database
#   # cnx.commit()

#   cursor.close()
#   cnx.close()
#   print("string recebida: "+string_recebida)
#   return retorno

# def receiving_agents(modelo):

#   return_list = []

#   cnx = mysql.connector.connect(user='root', password='root',
#                                  host='db',
#                                  database='MYSQL_DATABASE')
#   cursor = cnx.cursor()
#   query = ("SELECT id, data, processed FROM "+modelo+" "
#             "WHERE processed = %s AND %s")

#   # print("modelo:"+modelo)
#   cursor.execute(query, (0, "1=1"))

#   for (id, data, processed) in cursor:
#     print("{}, {}, {}".format(
#       id, data, processed))
#     return_list.append(data)

#   cursor.close()
#   cnx.close()

#   # for tupla in return_list:
#   #   print("tupla: "+tupla)
#   return return_list

# def send_function(string_to_send):
#     return "3"

# def process_agents_on_router():
#   #while True:
#   cnx = mysql.connector.connect(user='root', password='root',
#                                host='db',
#                                database='MYSQL_DATABASE')
#   cursor = cnx.cursor()
#   query = ("SELECT id, data, processed FROM router "
#             "WHERE processed = 0")

#   # print("modelo:"+modelo)
#   cursor.execute(query)


#   return_list = []
#   delete_list = []

#   print("lendo router: ")

#   for (id, data, processed) in cursor:
#     print("{}, {}, {}".format(
#       id, data, processed))
#     return_list.append([data, id])


#   print(return_list)

#   cursor.close()

#   # cursor.close()
#   # cnx.close()

#   # modelos_list = ["m1","m2","m3"]
#   modelos_list = ["m1"]

#   for tupla in return_list:
#     cnx = mysql.connector.connect(user='root', password='root',
#                                host='db',
#                                database='MYSQL_DATABASE')
#     cursor = cnx.cursor()
#     cnx.start_transaction()

#     model_to_send = random.choice(modelos_list)

#     print("tupla: "+tupla[0]+" indo para modelo : "+model_to_send)

#     sql1 = "INSERT INTO "+model_to_send+ " (data, processed) "+"VALUES ('"+tupla[0]+"' ,0); "
#     sql2 = "UPDATE router SET processed = 1 WHERE id = "+str(tupla[1])+"; "


#     # full_query = "START TRANSACTION; "
#     # full_query += "INSERT INTO "+model_to_send+ " (data, processed) "+"VALUES ('"+tupla[0]+"' ,0); "
#     # # full_query += "DELETE FROM router WHERE id = "+str(tupla[1])+"; "
#     # full_query += "UPDATE router SET processed = 1 WHERE id = "+str(tupla[1])+"; "
#     # full_query += "COMMIT;"

#     # full_query = "START TRANSACTION; "
#     # full_query += "INSERT INTO "+model_to_send+ " (data, processed) "+"VALUES ('"+tupla[0]+"' ,0); "
#     # # full_query += "DELETE FROM router WHERE id = "+str(tupla[1])+"; "
#     # full_query += "UPDATE router SET processed = 1 WHERE id = "+str(tupla[1])+"; "
#     # full_query += "COMMIT;"

#     # full_query = "START TRANSACTION; "
#     # full_query += "INSERT INTO "+model_to_send+ " (data, processed) "+"VALUES (%s, %s); "
#     # full_query += "DELETE FROM router WHERE id = %s "
#     # full_query += "COMMIT;"

#     # print("full query: "+full_query)
#     # add_employee = ("INSERT INTO "+model_to_send+ " "
#     #                "(data, processed) "
#     #                "VALUES (%s, %s)")

#     # data_employee = (tupla[0], 0, str(tupla[1]))

#     # # Insert new employee
#     # cursor.execute(add_employee, data_employee)
#     try:
#       # cursor.execute(full_query, data_employee)
#       cursor.execute(sql1)
#       cursor.execute(sql2)
#       # Make sure data is committed to the database
#       cnx.commit()
#     except errors.Error as e:
#       db.rollback()  # rollback changes
#       print("Rolling back ...")
#       print(e)
#     finally:
#       cursor.close()
#       cnx.close()
    
#   # cnx.close()

#   # cursor.close()
#   # cnx.close()

#   # for tupla in return_list:
#   #   print("tupla: "+tupla)
#   return return_list

















  # #while True:
  # cnx = mysql.connector.connect(user='root', password='root',
  #                              host='db',
  #                              database='MYSQL_DATABASE')
  # cursor = cnx.cursor()
  # query = ("SELECT id, data, processed FROM router "
  #           "WHERE processed = 0")

  # # print("modelo:"+modelo)
  # cursor.execute(query)


  # return_list = []
  # delete_list = []

  # print("lendo router: ")

  # for (id, data, processed) in cursor:
  #   print("{}, {}, {}".format(
  #     id, data, processed))
  #   return_list.append([data, id])


  # print(return_list)

  # # cursor.close()
  # # cnx.close()

  # modelos_list = ["m1","m2","m3"]

  # for tupla in return_list:
  #   model_to_send = random.choice(modelos_list)

  #   print("tupla: "+tupla[0]+" indo para modelo : "+model_to_send)

  #   add_employee = ("INSERT INTO "+model_to_send+ " "
  #                  "(data, processed) "
  #                  "VALUES (%s, %s)")

  #   data_employee = (tupla[0], 0)

  #   # # Insert new employee
  #   # cursor.execute(add_employee, data_employee)
  #   try:
  #     cursor.execute(add_employee, data_employee)
  #     # Make sure data is committed to the database
  #     cnx.commit()
  #   except mysql.connector.Error as err:
  #     print("Failed inserting on database: {}".format(err))

  # cursor.close()
  # cnx.close()

  # # for tupla in return_list:
  # #   print("tupla: "+tupla)
  # return return_list

   # time.sleep(5)

#!/usr/bin/python
# -*- coding: latin-1 -*-

#https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html

# import mysql.connector
# from mysql.connector import errorcode

# print("1")
# # cnx = mysql.connector.connect(user='root', password='root',
# #                               host='db',
# #                               database='MYSQL_DATABASE')
# try:
#   cnx = mysql.connector.connect(user='root', password='root',
#                                host='db',
#                                database='MYSQL_DATABASE')
# except mysql.connector.Error as err:
#   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#     print("Something is wrong with your user name or password")
#   elif err.errno == errorcode.ER_BAD_DB_ERROR:
#     print("Database does not exist")
#   else:
#     print(err)
# else:
#   cnx.close()
# print("2")
# #host="db", user="root", passwd="root", db="MYSQL_DATABASE"

## *-- CRIA TODO O BANCO --*

# from __future__ import print_function

# import mysql.connector
# from mysql.connector import errorcode

# DB_NAME = 'MYSQL_DATABASE'

# TABLES = {}
# TABLES['employees'] = (
#     "CREATE TABLE `employees` ("
#     "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
#     "  `birth_date` date NOT NULL,"
#     "  `first_name` varchar(14) NOT NULL,"
#     "  `last_name` varchar(16) NOT NULL,"
#     "  `gender` enum('M','F') NOT NULL,"
#     "  `hire_date` date NOT NULL,"
#     "  PRIMARY KEY (`emp_no`)"
#     ") ENGINE=InnoDB")

# TABLES['departments'] = (
#     "CREATE TABLE `departments` ("
#     "  `dept_no` char(4) NOT NULL,"
#     "  `dept_name` varchar(40) NOT NULL,"
#     "  PRIMARY KEY (`dept_no`), UNIQUE KEY `dept_name` (`dept_name`)"
#     ") ENGINE=InnoDB")

# TABLES['salaries'] = (
#     "CREATE TABLE `salaries` ("
#     "  `emp_no` int(11) NOT NULL,"
#     "  `salary` int(11) NOT NULL,"
#     "  `from_date` date NOT NULL,"
#     "  `to_date` date NOT NULL,"
#     "  PRIMARY KEY (`emp_no`,`from_date`), KEY `emp_no` (`emp_no`),"
#     "  CONSTRAINT `salaries_ibfk_1` FOREIGN KEY (`emp_no`) "
#     "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE"
#     ") ENGINE=InnoDB")

# TABLES['dept_emp'] = (
#     "CREATE TABLE `dept_emp` ("
#     "  `emp_no` int(11) NOT NULL,"
#     "  `dept_no` char(4) NOT NULL,"
#     "  `from_date` date NOT NULL,"
#     "  `to_date` date NOT NULL,"
#     "  PRIMARY KEY (`emp_no`,`dept_no`), KEY `emp_no` (`emp_no`),"
#     "  KEY `dept_no` (`dept_no`),"
#     "  CONSTRAINT `dept_emp_ibfk_1` FOREIGN KEY (`emp_no`) "
#     "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE,"
#     "  CONSTRAINT `dept_emp_ibfk_2` FOREIGN KEY (`dept_no`) "
#     "     REFERENCES `departments` (`dept_no`) ON DELETE CASCADE"
#     ") ENGINE=InnoDB")

# TABLES['dept_manager'] = (
#     "  CREATE TABLE `dept_manager` ("
#     "  `emp_no` int(11) NOT NULL,"
#     "  `dept_no` char(4) NOT NULL,"
#     "  `from_date` date NOT NULL,"
#     "  `to_date` date NOT NULL,"
#     "  PRIMARY KEY (`emp_no`,`dept_no`),"
#     "  KEY `emp_no` (`emp_no`),"
#     "  KEY `dept_no` (`dept_no`),"
#     "  CONSTRAINT `dept_manager_ibfk_1` FOREIGN KEY (`emp_no`) "
#     "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE,"
#     "  CONSTRAINT `dept_manager_ibfk_2` FOREIGN KEY (`dept_no`) "
#     "     REFERENCES `departments` (`dept_no`) ON DELETE CASCADE"
#     ") ENGINE=InnoDB")

# TABLES['titles'] = (
#     "CREATE TABLE `titles` ("
#     "  `emp_no` int(11) NOT NULL,"
#     "  `title` varchar(50) NOT NULL,"
#     "  `from_date` date NOT NULL,"
#     "  `to_date` date DEFAULT NULL,"
#     "  PRIMARY KEY (`emp_no`,`title`,`from_date`), KEY `emp_no` (`emp_no`),"
#     "  CONSTRAINT `titles_ibfk_1` FOREIGN KEY (`emp_no`)"
#     "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE"
#     ") ENGINE=InnoDB")


# cnx = mysql.connector.connect(user='root', password='root',
#                                host='db',
#                                database='MYSQL_DATABASE')
# cursor = cnx.cursor()

# def create_database(cursor):
#     try:
#         cursor.execute(
#             "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
#     except mysql.connector.Error as err:
#         print("Failed creating database: {}".format(err))
#         exit(1)

# try:
#     cursor.execute("USE {}".format(DB_NAME))
# except mysql.connector.Error as err:
#     print("Database {} does not exists.".format(DB_NAME))
#     if err.errno == errorcode.ER_BAD_DB_ERROR:
#         create_database(cursor)
#         print("Database {} created successfully.".format(DB_NAME))
#         cnx.database = DB_NAME
#     else:
#         print(err)
#         exit(1)

# for table_name in TABLES:
#     table_description = TABLES[table_name]
#     try:
#         print("Creating table {}: ".format(table_name), end='')
#         cursor.execute(table_description)
#     except mysql.connector.Error as err:
#         if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
#             print("already exists.")
#         else:
#             print(err.msg)
#     else:
#         print("OK")

# cursor.close()
# cnx.close()


# *-- INSERT --*

# from __future__ import print_function
# from datetime import date, datetime, timedelta
# import mysql.connector

# cnx = mysql.connector.connect(user='root', password='root',
#                                host='db',
#                                database='MYSQL_DATABASE')
# cursor = cnx.cursor()

# tomorrow = datetime.now().date() + timedelta(days=1)

# add_employee = ("INSERT INTO employees "
#                "(first_name, last_name, hire_date, gender, birth_date) "
#                "VALUES (%s, %s, %s, %s, %s)")
# add_salary = ("INSERT INTO salaries "
#               "(emp_no, salary, from_date, to_date) "
#               "VALUES (%(emp_no)s, %(salary)s, %(from_date)s, %(to_date)s)")

# data_employee = ('Geert', 'Vanderkelen', tomorrow, 'M', date(1977, 6, 14))

# # Insert new employee
# cursor.execute(add_employee, data_employee)
# emp_no = cursor.lastrowid

# # Insert salary information
# data_salary = {
#   'emp_no': emp_no,
#   'salary': 50000,
#   'from_date': tomorrow,
#   'to_date': date(9999, 1, 1),
# }
# cursor.execute(add_salary, data_salary)

# # Make sure data is committed to the database
# cnx.commit()

# cursor.close()
# cnx.close()

# PRA PUXAR DADOS DO BANCO

# import datetime
# import mysql.connector

# cnx = mysql.connector.connect(user='root', password='root',
#                                host='db',
#                                database='MYSQL_DATABASE')
# cursor = cnx.cursor()

# query = ("SELECT first_name, last_name, hire_date FROM employees "
#          "WHERE hire_date BETWEEN %s AND %s")

# hire_start = datetime.date(1900, 1, 1)
# hire_end = datetime.date(2200, 12, 31)

# cursor.execute(query, (hire_start, hire_end))

# for (first_name, last_name, hire_date) in cursor:
#   print("{}, {} was hired on {:%d %b %Y}".format(
#     last_name, first_name, hire_date))

# cursor.close()
# cnx.close()