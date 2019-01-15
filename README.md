# Exporter Service
You must choose the docker-compose file depending on the desired environment and replace the `%docker-file%` placeholders on the commands above
```
Development: docker-compose-dev.yml
```

## Start Project
```
docker-compose -f %docker-file% up -d --build
```
Service is now up on http://localhost:5004, you can check the service's health on http://localhost:5004/exporter-service/health

## Lint
```
docker container exec exporter flake8 project
```

## Run Test
```
docker container exec exporter python manage.py test
```
or
```
./test.sh
```

## Autorun test on file changes
```
./test.sh watch
```

## Run a specific test file
```
docker container exec exporter python manage.py test --file=health_test
```

## Run Code Coverage
```
docker container exec exporter python manage.py cov
```

## Run Shell
```
docker container exec exporter python flask shell
```
