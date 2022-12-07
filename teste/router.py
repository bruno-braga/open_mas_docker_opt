import time
import requests

if __name__ == '__main__':
    print ('Starting router...')
    while True:
        retorno = False
        while retorno == False:
            try:
                response = requests.get('http://api:5000/api/v1/resources/process_agents_on_router')
                print('Response from API: ' + response.text)
                response.raise_for_status()
                time.sleep(5)
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
        # try:
        #     response = requests.get('http://api:5000/api/v1/resources/process_agents_on_router')
        #     print('Response from API: ' + response.text)
        #     response.raise_for_status()
        #     time.sleep(5)
        # except requests.exceptions.HTTPError as errh:
        #     print(errh)
        # except requests.exceptions.ConnectionError as errc:
        #     print(errc)
        # except requests.exceptions.Timeout as errt:
        #     print(errt)
        # except requests.exceptions.RequestException as err:
        #     print(err)
        # except:
        #     time.sleep(1)
        #     print('Error executing the router')

# 18.08/22 - Código 100% funcional importando do db_python_netlogo. Acima, é testando passando esse código pra API
# from db_python_netlogo import process_agents_on_router
# import time

# if __name__ == '__main__':
# 	print("Starting router...")
# 	while True:
# 		time.sleep(5)
# 		print("5s")
# 		try:
# 			process_agents_on_router()
# 		except:
# 			time.sleep(1)
# 			print("Error executing the router")