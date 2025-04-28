# Stage 3:

This stage will integrate the main application as an additional service.

Useful links:

- https://docs.docker.com/reference/compose-file/build/

## Objectives

We will add another service to the `docker-compose.yaml` file with the attributes below:

- Define the service with the `hyper-service` name;
- Add the command to build the image for your service;
- Define the container name with the `hyper-task-manager` value;
- Define the `MONGO_INITDB_ROOT_USERNAME` environment variable with the `${MONGO_INITDB_ROOT_USERNAME}` value;
- Define the `MONGO_INITDB_ROOT_PASSWORD` environment variable with the `${MONGO_INITDB_ROOT_PASSWORD}` value;
- Define the `MONGO_HOST_NAME` environment variable with the `mongodb` value;
- Define the `MONGO_PORT_NUMBER` environment variable with the `27017` value;
- Define the `env_file` option for the `.env` file.