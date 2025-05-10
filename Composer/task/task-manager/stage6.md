# Stage 6:

In this stage name convention changed so we will update the services names.

We will also use the built API for the first time according to `api_documentation.md`.

## Objectives

We need to:

- Modify the `docker-compose.yml` file and rename your resources with the following values:
  - Application container and service - rename both to `task-manager-app`;
  - Database container - rename it to `task-manager-db`;
  - Volume - give it the `task-manager-data` name;
  - Network - give it the `task-manager-network` name;
- Build and restart the services;
- Create a task with the title `Study` and the description `Study DevOps`.
