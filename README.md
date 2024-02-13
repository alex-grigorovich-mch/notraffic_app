# No Traffic App

## Requirements
* Docker
* Docker Compose
* make [optional]

## How to 

### start
```shell
make up
make up-build # if you need to rebuild app
docker-compose up # if you have no make
```

### test
```shell
make test
docker-compose exec backend pytest . # if you have no make
```

### lint
```shell
make lint
# if you have no make:
docker-compose exec backend black .
docker-compose exec backend flake8 .
docker-compose exec backend isort .
```

### debug
```
# to debug backend with debugpy:
docker-compose -f docker-compose.debug.yml up --build
```

## Project Structure
```
├── back
│   ├── api
│   ├── build
│   ├── common
│   ├── config
│   ├── manage.py
│   ├── notraffic
│   ├── poetry.lock
│   ├── pyproject.toml
├── front
│   ├── Dockerfile
│   ├── index.html
│   ├── package.json
│   ├── package-lock.json
│   ├── public
│   ├── src
│   ├── tsconfig.json
│   ├── tsconfig.node.json
│   └── vite.config.ts
├── docker-compose.debug.yml
├── docker-compose.yml
├── Makefile
└── README.md
```
### Front folder
As usual contains all default files as file structure for React project as package.json, lock file and so on. I decided to go on with Component Driven Design to create generic components to reach reusability.
`src` folder contains:
* `assets` - with public assets
* `components` - with generic components to be used in future
* `pages` - page representation of views, assembled from `components`


### Back folder
A common Django structure with some adjustments:
* `api` - a package used to collect all api accoring to routing, it makes easier to maintain API (for example `/api/v1/notraffic/` route similar with import api.v1.notraffic )
* `build` - any files related with building projects, some entrypoints, Dockerfiles, configs
* `common` - package with some utilities could be used across all application (it feature could be separeted into custom library)
* `config` - default django main package
* `notraffic` - django app with model 
* `tests` - unit tests for application

## Some possible future adjustments
1. Due to time limitations (4 hours), not all the desired functionality was implemented.
1. Pagination. At the moment, there were no page numbers on the projects. This means that all data will be downloaded at this moment. 
2. Proper error handling on frontend. For now, the interface simply hides API errors by displaying a generic modal window.
3. Managing streets. At the moment we have only two streets to create intersections but for the futher project development
it makes sense to increase number of streets and connect them with the real maps eg. Google maps. 
4. Postgres + PostGIS. Use postgres with its powerful geographic data indexing features.