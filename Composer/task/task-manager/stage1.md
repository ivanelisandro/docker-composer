# Stage 1:

This stage will add a database as storage.

Use official [Mongo image](https://hub.docker.com/_/mongo).

## Objectives

- In the docker-compose.yaml file, define the name as `hyper-task-manager`;
- Define one service with the attributes below:
  - Define the service with the `mongodb` name;
  - Use the official `mongo:6.0.8` image;
  - Define a container name with the `hyper-mongo` value;
  - Map the host port as `27017` to the container port `27017`;
  - Define the `MONGO_INITDB_ROOT_USERNAME` environment variable with the `${MONGO_INITDB_ROOT_USERNAME}` value;
  - Define the `MONGO_INITDB_ROOT_PASSWORD` environment variable with the `${MONGO_INITDB_ROOT_PASSWORD}` value;
  - Define the `env_file` option for the `.env` file.
