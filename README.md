# **Under development**

## Description
Framework prototype based on Docker to develop Open Multiagent Systems (Open Multiagent Systems - Open MAS - OMAS).

## Prerequisites
```
Docker
```

## Configuration

Most of the configuration is done in the files: `docker-compose.yaml` and `.env`.

## Usage

### Full local
To execute the whole architecture locally, use this command:
```
docker-compose -f docker-compose-local.yaml  up -d
```

### Hybrid
To execute part of the architecture locally and the other remotely, on the cloud, for example, you should use locally:
```
docker-compose -f docker-compose-hybrid-local.yaml  up -d
```

And then, on the remote (server), use:

```
docker-compose -f docker-compose-hybrid-server.yaml  up -d
```

### Arm64

Every `docker-compose.yaml` has a `-arm64` version, to run on computers/VMs based on this architecture. If you're using an `arm64` architecture, for example, to run the architecture locally, instead of using:

```
docker-compose -f docker-compose-local.yaml  up -d
```

You should use:

```
docker-compose -f docker-compose-local-arm64.yaml  up -d
```

## Project Structure

### Video

The `videos` folder contains two study cases of the architecture.

[Example without GUI](videos/GUI_OFF.mp4) or watch online [here](https://streamable.com/rug2mr)<br />
[Example using GUI](videos/GUI_ON.mp4) or watch online [here](https://streamable.com/3rct7p)


### Shared_Volume

The `shared_volume` folder contains the most important important files of the architecture, besides the `docker-compose` files. Some files/folders to pay atention:

#### Dashboard

This folder is used by the `php` container. It is used to mount the output interface of the architecture, where the user can check real-time information about the simulation.

#### DB_File

This folder contains a `.sql` file used to build the DB that the architecture uses to register information about the agents.

#### Jacamo

This folder contains the structure used by the `jacamo` container. In the actual implementation, it has the `gold miners` model implemented.

#### Netlogo_Output

This folder contains some `.txt` files that comes from the NetLogo's simulation, providing information about real-time cycle, agents that ended the simulation alive and so on.

#### Py:

Files of the py extension, used by NetLogo, to use Python code within NetLogo. In architecture, it is used to run Python code that communicates with the architecture;
#### Init.py
Serves as a base for other Python codes used by the architecture;

#### Access_api.py
Intermediate between the Python code implemented in the NetLogo input/output and the API;
#### Api.py
Code used by the API container. Contains all API methods which are the core of the architecture;
#### Clean_simulation_files.py
File used by the clear_files container. Used to clear logs from previous simulations. The files that will be excluded can be chosen within this code;
#### Db_python_netlogo.py
File that NetLogo uses to access the API, through the py extension. NetLogo calls functions from this file, which in turn calls functions from access_api which ultimately communicates with the API;
#### Initialize_db.py
In case you don't use a structure ready for the DB, through the SQL file, the structure of the database can be assembled through this file. Must be run by the Register container;
#### Open_sugarscape_m1.nlogo and open_sugarscape_m2.nlogo
NetLogo file, which will be used by the model container;
#### Python_execute_netlogo.py
File used by optional trigger containers, which will condition the start of execution of model containers through some policy. Contains Python code to execute sockets that wait for the command to start executing the models;
#### Register.py
Code executed by the Register container, which contains functions to request the API to create the initial simulation agents;
#### Router.py
Code executed by the Router container. Contains a function in loop that calls the API in the method to process agents assigned to the Router. Contains routing policies. In this file, it is possible to determine a time between the processing of each agent, to allow the architecture to consume more resources and be able to process more agents per time interval, or to increase the time between processing, reducing machine overload;
#### Sugar-map.txt
File used by the other two NetLogo files, containing simulation information regarding the positions of the map containing sugar and its quantity.;

## Outputs

### Logs

#### NetLogo
By default, the main example (Sugarscape model) keeps some logs from the execution in files inside `shared_volume/netlogo_output`

#### JaCaMo
By default, the main example (Gold Miners model) keeps some logs from the execution of Jason in the file`shared_volume/jacamo/jacamo_model/mas.log`

JaCaMo exposes by default some information about Jason and CArtAgO, which are, respectively, Jason Mind Inspector and CArtAgO's Web View. We forward this information from the container to the host machine. By default, you can access Jason Mind Inspector using `localhost:3272` and CArtAgO's Web View using `localhost:3273` on the host machine.

#### Other Logs
By default, you can check everything that is running inside any container from the architecture, just use ** docker logs container_name ** where container_name is the name of the container that you want to check. More information in docker logs[here](https://docs.docker.com/engine/reference/commandline/logs/)

### Other Outputs

Besides Logs and the main execution from the models, you can get extra information from the simulation checking the exposed outputs from the `interface` and `phpmyadmin` (dbms) containers, accessible via `localhost/dashboard` and `localhost:8080` on the host machine by default.


## Extra Information

### GUI on and OFF
By default, the Docker container inside the architecture are made to run using just CLI. Even so, if you want to run models that uses GUI, the architecture is ready to comunicate with models running on the same host machine, outside Docker. For example, in order to run Gold Miners model outside Docker and it still communicate with the architecture, you need to ajust one parameter in 3 files:
1. `shared_volume/jacamo/jacamo_model/src/agt/mylib/my_create_ag.java` - change the `using_docker` variable to `false` - check commentaries on the file [here](shared_volume/jacamo/jacamo_model/src/agt/mylib/my_create_ag.java)
2. `shared_volume/jacamo/jacamo_model/src/agt/mylib/my_delete_ag.java` - change the `using_docker` variable to `false` - check commentaries on the file [here](shared_volume/jacamo/jacamo_model/src/agt/mylib/my_delete_ag.java)
3. `shared_volume/jacamo/jacamo_model/src/env/mining/MiningPlanet.java` - change the `hasGUI` variable to `true` - check commentaries on the file [here](shared_volume/jacamo/jacamo_model/src/env/mining/MiningPlanet.java)