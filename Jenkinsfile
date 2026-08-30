pipeline {

    agent any

    environment {

        IMAGE_NAME = "examenfinal-app"
        IMAGE_TAG = "latest"

    }

    stages {

        stage('Checkout') {

            steps {

                echo 'Obteniendo código fuente'

                checkout scm

            }

        }

        stage('Test') {

            steps {

                echo 'Ejecutando pruebas'

                sh '''
                    docker run --rm \
                    -v "$WORKSPACE":/workspace \
                    -w /workspace \
                    python:3.12-slim \
                    bash -c "
                        pip install --no-cache-dir -r app/requirements.txt &&
                        pytest -v
                    "
                '''

            }

        }

        stage('Build Docker Image') {

            steps {

                echo 'Construyendo imagen Docker'

                sh '''
                    docker build \
                    -t ${IMAGE_NAME}:${IMAGE_TAG} \
                    ./app
                '''

            }

        }

        stage('Deploy') {

            steps {

                echo 'Desplegando aplicación'

                sh '''
                    cd /workspace

                    docker compose up -d \
                    --build \
                    app1 \
                    app2 \
                    nginx
                '''

            }

        }

        stage('Verification') {

            steps {

                echo 'Verificando aplicación'

                sh '''
                    sleep 10

                    curl -f http://nginx/health
                '''

            }

        }

    }

}