# Stage 2:

This stage will volume and networking definitions to the project without any actual configuration.

Useful links:

- https://docs.docker.com/engine/storage/volumes/
- https://docs.docker.com/compose/how-tos/networking/

## Objectives

Modify the `docker-compose.yaml` file by adding a network and a permanent volume for the service:
- Define the volume with the `mongo-data` name;
- Define the network with the `hyper-task-manager-network` name;
- Add the network to the `mongodb` service.
- Add the volume to the `mongodb` service and map it to the container's `/data/db` directory.
