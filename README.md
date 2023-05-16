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



## Video

The `videos` folder contains two study cases of the architecture.

[Example without GUI](videos/GUI_OFF.mp4)
[Example using GUI](videos/GUI_ON.mp4)