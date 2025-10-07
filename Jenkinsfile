pipeline {
    agent any

    environment {
        APP_IMAGE     = 'online-voting-system'
        COMPOSE_FILE  = 'docker-compose.yml'
        WEB_SERVICE   = 'web'
        REDIS_SERVICE = 'redis'
    }

    stages {
        stage('Cleanup Old Containers') {
            steps {
                echo 'Cleaning up old containers and networks...'
                sh '''
                  docker-compose -f ${COMPOSE_FILE} down -v || true
                  docker ps -aq | xargs -r docker rm -f || true
                  docker network prune -f || true
                '''
            }
        }

        stage('Build & Start Services') {
            steps {
                echo 'Building and starting containers...'
                sh "docker-compose -f ${COMPOSE_FILE} up -d --build"

                echo 'Waiting for Redis to be ready...'
                sh """
                for i in {1..30}; do
                    if docker-compose exec -T ${REDIS_SERVICE} redis-cli ping 2>/dev/null | grep -q PONG; then
                        echo 'Redis is ready!'
                        break
                    fi
                    echo 'Waiting for Redis...'
                    sleep 1
                done
                """
            }
        }

        stage('Run Unit & Integration Tests') {
            steps {
                echo 'Running pytest inside the web container (excluding Selenium tests)...'
                sh """
                docker-compose exec -T ${WEB_SERVICE} /bin/bash -c '
                    export PYTHONPATH=/app &&
                    pytest -v --maxfail=1 --disable-warnings \
                           --ignore=tests/test_ui.py \
                           --junitxml=/tmp/report.xml || true
                '
                """
                echo 'Copying test report...'
                sh "docker cp \$(docker-compose ps -q ${WEB_SERVICE}):/tmp/report.xml report.xml || true"
            }
        }

        stage('Run Selenium Tests') {
            steps {
                echo 'Running Selenium (UI) tests in headless mode...'
                sh """
                docker-compose exec -T ${WEB_SERVICE} /bin/bash -c '
                    export PYTHONPATH=/app &&
                    pytest -v --disable-warnings tests/test_ui.py \
                           --junitxml=/tmp/selenium-report.xml || true
                '
                """
                echo 'Copying Selenium report...'
                sh "docker cp \$(docker-compose ps -q ${WEB_SERVICE}):/tmp/selenium-report.xml selenium-report.xml || true"
            }
        }

        stage('Publish Test Reports') {
            steps {
                echo 'Publishing all test results...'
                junit allowEmptyResults: true, testResults: 'report.xml, selenium-report.xml'
            }
        }

        stage('Tear Down') {
            steps {
                echo 'Stopping containers...'
                sh "docker-compose -f ${COMPOSE_FILE} down -v"
            }
        }
    }
}