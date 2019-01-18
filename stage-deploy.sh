# !/bin/bash
ssh -o StrictHostKeyChecking=no ubuntu@${STAGE_SERVER} "docker login -u gitlab-ci-token -p $DOCKER_TOKEN registry.gitlab.com"

ssh -o StrictHostKeyChecking=no ubuntu@${STAGE_SERVER} 'docker network create --subnet=172.24.0.0/16 exporter-service-network'

ssh -o StrictHostKeyChecking=no ubuntu@${STAGE_SERVER} 'docker container stop exporter'
ssh -o StrictHostKeyChecking=no ubuntu@${STAGE_SERVER} 'docker container stop exporter-swagger'

ssh -o StrictHostKeyChecking=no ubuntu@${STAGE_SERVER} 'docker container rm exporter'
ssh -o StrictHostKeyChecking=no ubuntu@${STAGE_SERVER} 'docker container rm exporter-swagger'

ssh -o StrictHostKeyChecking=no ubuntu@${STAGE_SERVER} 'docker image rm $(docker images registry.gitlab.com/gusisoft/onelike/exporter-service/exporter-swagger -q)'
ssh -o StrictHostKeyChecking=no ubuntu@${STAGE_SERVER} 'docker image rm $(docker images registry.gitlab.com/gusisoft/onelike/exporter-service/exporter -q)'

ssh -o StrictHostKeyChecking=no ubuntu@${STAGE_SERVER} "docker run -d --restart always -e 'API_URL=definitions/swagger.yml' --name exporter-swagger --network exporter-service-network --ip 172.24.0.3 $REGISTRY_REPO/$SWAGGER:$TAG"
ssh -o StrictHostKeyChecking=no ubuntu@${STAGE_SERVER} "docker run -d --restart always -e 'FLASK_ENV=development' -e 'FLASK_APP=manage.py' -e 'APP_SETTINGS=project.config.DevelopmentConfig' -e 'SECRET_KEY=secret_key' -e USERS_SERVICE_URL=$USERS_SERVICE_URL -e AUTH_SERVICE_URL=$AUTH_SERVICE_URL --name exporter --network exporter-service-network --ip 172.24.0.2 $REGISTRY_REPO/$EXPORTER:$TAG"

ssh -o StrictHostKeyChecking=no ubuntu@${STAGE_SERVER} 'docker network connect onelike-network --ip 172.18.0.14 exporter'
ssh -o StrictHostKeyChecking=no ubuntu@${STAGE_SERVER} 'docker network connect onelike-network --ip 172.18.0.15 exporter-swagger'

ssh -o StrictHostKeyChecking=no ubuntu@${STAGE_SERVER} 'echo OK'
