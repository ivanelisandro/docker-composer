# Stage 4:

For this stage we will map a port, create a network and define a dependency to ensure the proper functioning of the `hyper-task-manager` service.

Useful links:

- https://docs.docker.com/reference/compose-file/services/#depends_on

## Objectives

We will add more attributes to the `hyper-service` service:

- Map the host port `8000` to the container port `8000`;
- Add the `hyper-task-manager-network` network;
- Define the dependency on the `mongodb` service.
