import time
import requests
import os
import json
import random
from random import shuffle
from operator import itemgetter

host = os.environ['host']
port = os.environ['port']
route_type = os.environ['route_type']
delay = float(os.environ['delay'])

def calculate_route(agents_list):
    models_list = ["m1", "m2", "m3"]
    processed_agents = []

    #copying so we don't mess with the original list
    copied_list = agents_list

    #debug_only
    #route_type = "random"

    #ordering
    if (route_type == "random"):
        shuffle(copied_list)
    elif (route_type == "sequential"):
        print("Sorted Lists based on index 0: % s" % (sorted(copied_list, key=itemgetter(0))))

    for (id, agent_id, data, path, processed) in copied_list:
        model_to_send = random.choice(models_list)
        processed_agents.append([id, agent_id, data, path, processed, model_to_send])
    return processed_agents

def main():
    """ Loop function that receives and process agents in the router """
    print ('Starting router...')
    while True:
        retorno = False
        while retorno == False:
            try:
                response = requests.get('http://'+host+':'+port+'/api/v1/resources/get_unprocessed_agents_from_router')
                print('Response from API: ' + response.text)
                response.raise_for_status()

                agents_to_be_processed = response.json()

                if(len(agents_to_be_processed) > 0):
                    print("processed_agents before routing:")
                    print(agents_to_be_processed)

                    processed_agents = calculate_route(agents_to_be_processed)
                    
                    print("processed_agents after routing:")
                    print(processed_agents)

                    response = requests.post('http://'+host+':'+port+'/api/v1/resources/forward_processed_agents_from_router', json = processed_agents, timeout=120)
                    print('Response from API: ' + response.text)
                    response.raise_for_status()
                time.sleep(delay)
                print("Function worked well")
                retorno = True
            except requests.exceptions.HTTPError as errh:
                print(errh)
                print("Error type HTTP, sleeping and retrying")
                time.sleep(delay)
            except requests.exceptions.ConnectionError as errc:
                print(errc)
                print("Error type Connection, sleeping and retrying")
                time.sleep(delay)
            except requests.exceptions.Timeout as errt:
                print(errt)
                print("Error type Timeout, sleeping and retrying")
                time.sleep(delay)
            except requests.exceptions.RequestException as err:
                print(err)
                print("Error type RequestException, sleeping and retrying")
                time.sleep(delay)

        print("Left loop")

# def main():
#     """ Loop function that receives and process agents in the router """
#     print ('Starting router...')
#     while True:
#         retorno = False
#         while retorno == False:
#             try:
#                 response = requests.get('http://api:5000/api/v1/resources/process_agents_on_router')
#                 print('Response from API: ' + response.text)
#                 response.raise_for_status()
#                 time.sleep(5)
#                 print("Function worked well")
#                 retorno = True
#             except requests.exceptions.HTTPError as errh:
#                 print(errh)
#                 print("Error type HTTP, sleeping and retrying")
#                 time.sleep(1)
#             except requests.exceptions.ConnectionError as errc:
#                 print(errc)
#                 print("Error type Connection, sleeping and retrying")
#                 time.sleep(1)
#             except requests.exceptions.Timeout as errt:
#                 print(errt)
#                 print("Error type Timeout, sleeping and retrying")
#                 time.sleep(1)
#             except requests.exceptions.RequestException as err:
#                 print(err)
#                 print("Error type RequestException, sleeping and retrying")
#                 time.sleep(1)

#         print("Left loop")

if __name__ == '__main__':
    main()