from db_python_netlogo import teste_router
import time

if __name__ == '__main__':
	print("Starting router...")
	while True:
		time.sleep(5)
		print("5s")
		try:
			teste_router()
		except:
			time.sleep(1)
			print("Error executing the router")