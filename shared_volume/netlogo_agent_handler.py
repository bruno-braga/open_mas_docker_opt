#!/usr/bin/python
#-*- coding: latin-1 -*-

import mysql.connector
from mysql.connector import errorcode

import random

import time

import requests

import os

def host_port():
  """ Internal function, to inform host and port to access the API """
  host = os.environ['host']
  #host = "api"
  #host = "144.22.197.41"
  port = "5000"
  return host, port

if __name__ == '__main__':
  print("")


def testing_exception(error):
  """ Function create for testing only, testing the creation of a custom exception """
  raise Exception(error)

def request_to_register(model, min, max):
  """ Function that requests to register to create a certain amount of agents. Asked by NetLogo. Calls the register_agents_on_platform endpoint on API """
  start = time.time()
  host, port = host_port()
  print("Start time request_to_register: "+str(start))
  print("Host: "+host)
  should_return = False
  while should_return == False:
    try:
      response = requests.post('http://'+host+':'+port+'/api/v1/resources/register_agents_on_platform', json = {"model":model, "min":min, "max":max}, timeout=120)
      print("Response from API: "+response.text)
      response.raise_for_status()
      
      #print(response)
      print("Function worked well")
      should_return = True
    except requests.exceptions.HTTPError as errh:
        print(errh)
        print("Error type HTTP, sleeping and retrying")
        time.sleep(1)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
        print("Error type ConnectionError, sleeping and retrying")
        time.sleep(1)
    except requests.exceptions.Timeout as errt:
        print(errt)
        print("Error type Timeout, sleeping and retrying")
        time.sleep(1)
    except requests.exceptions.RequestException as err:
        print(err)
        print("Error type RequestException, sleeping and retrying")
        time.sleep(1)

  print("Left loop")
  end = time.time()
  print("End time request_to_register: "+str(end - start))
  return should_return

def send_agent_to_alive(agent_id, model):
  """ Function used by NetLogo, when the simulation is over. It removes an agent from the simulation and sends it to the API (to be inserted in alive_agents table). Calls the model_to_alive endpoint on API """
  start = time.time()
  host, port = host_port()
  print("Start time send_agent_to_alive: "+str(start))
  should_return = False
  while should_return == False:
    try:
      response = requests.post('http://'+host+':'+port+'/api/v1/resources/model_to_alive', json = {"agent_id":agent_id, "model":model}, timeout=120)
      response.raise_for_status()

      #print(response)
      print("Function worked well")
      should_return = True
    except requests.exceptions.HTTPError as errh:
        print(errh)
        print("Error type HTTP, sleeping and retrying")
        time.sleep(1)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
        print("Error type Connection, sleeping and retrying")
        time.sleep(1)
    except requests.exceptions.Timeout as errt:
        print(errt)
        print("Error type Timeout, sleeping and retrying")
        time.sleep(1)
    except requests.exceptions.RequestException as err:
        print(err)
        print("Error type RequestException, sleeping and retrying")
        time.sleep(1)

  print("Left loop")
  end = time.time()
  print("End time send_agent_to_alive: "+str(end - start))
  return should_return

def send_agent_to_router(agent_id, data, path):
  """ Function used by NetLogo, to send agents to the platform. It removes an agent from the simulation and sends it to the API (to be inserted in the router table). Calls the model_to_router endpoint on API """
  start = time.time()
  host, port = host_port()
  print("Start time send_agent_to_router: "+str(start))
  should_return = False
  while should_return == False:
    try:
      response = requests.post('http://'+host+':'+port+'/api/v1/resources/model_to_router', json = {"agent_id":agent_id, "data":data, "path":path}, timeout=120)
      response.raise_for_status()

      #print(response)
      print("Function worked well")
      should_return = True
    except requests.exceptions.HTTPError as errh:
        print(errh)
        print("Error type HTTP, sleeping and retrying")
        time.sleep(1)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
        print("Error type Connection, sleeping and retrying")
        time.sleep(1)
    except requests.exceptions.Timeout as errt:
        print(errt)
        print("Error type Timeout, sleeping and retrying")
        time.sleep(1)
    except requests.exceptions.RequestException as err:
        print(err)
        print("Error type RequestException, sleeping and retrying")
        time.sleep(1)

  print("Left loop")
  end = time.time()
  print("End time send_agent_to_router: "+str(end - start))
  return should_return

def receiving_agents(modelo):
  """ Function used by NetLogo to receive agents from the platform. It receives an agent from the API and inserts it into the simulation. Calls the check_new_agents endpoint on API """
  start = time.time()
  host, port = host_port()
  print("Start time receiving_agents: "+str(start))
  str1 = ''
  return_list = []
  should_return = False
  while should_return == False:
    try:
      response = requests.get('http://'+host+':'+port+'/api/v1/resources/check_new_agents', params={"model":modelo}, timeout=120)
      response.raise_for_status()
      return_list = response.json()

      print("Function worked well")
      should_return = True
    except requests.exceptions.HTTPError as errh:
        print(errh)
        print("Error type HTTP, sleeping and retrying")
        time.sleep(1)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
        print("Error type Connection, sleeping and retrying")
        time.sleep(1)
    except requests.exceptions.Timeout as errt:
        print(errt)
        print("Error type Timeout, sleeping and retrying")
        time.sleep(1)
    except requests.exceptions.RequestException as err:
        print(err)
        print("Error type RequestException, sleeping and retrying")
        time.sleep(1)
  # return str1
  print("Left loop")
  end = time.time()
  print("End time receiving_agents: "+str(end - start))
  return return_list