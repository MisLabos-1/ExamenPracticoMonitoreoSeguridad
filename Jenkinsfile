pipeline {

    agent any

    environment {

        IMAGE_NAME = "examenfinal-app"
        IMAGE_TAG = "${BUILD_NUMBER}"

    }

    stages {

        stage('Checkout') {

            steps {

                echo '================================='
                echo 'ETAPA 1 - CHECKOUT'
                echo '================================='

                checkout scm

            }

        }

        stage('Secret Scan') {

            steps {

                echo '================================='
                echo 'ETAPA 2 - GITLEAKS'
                echo '================================='

                sh '''
                    docker run --rm \
                    -v "$WORKSPACE":/workspace \
                    zricethezav/gitleaks:latest \
                    detect \
                    --source=/workspace \
                    --no-git
                '''

            }

        }

        stage('Application Tests') {

            steps {

                echo '================================='
                echo 'ETAPA 3 - TESTS'
                echo '================================='

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

        stage('Docker Build') {

            steps {

                echo '================================='
                echo 'ETAPA 4 - BUILD'
                echo '================================='

                sh '''
                    docker build \
                    -t ${IMAGE_NAME}:${IMAGE_TAG} \
                    -t ${IMAGE_NAME}:latest \
                    ./app
                '''

            }

        }

        stage('Container Security Scan') {

            steps {

                echo '================================='
                echo 'ETAPA 5 - TRIVY'
                echo '================================='

                sh '''
                    docker run --rm \
                    -v /var/run/docker.sock:/var/run/docker.sock \
                    aquasec/trivy:latest \
                    image \
                    --severity HIGH,CRITICAL \
                    --exit-code 1 \
                    ${IMAGE_NAME}:${IMAGE_TAG}
                '''

            }

        }

        stage('Deploy') {

            steps {

                echo '================================='
                echo 'ETAPA 6 - DEPLOY'
                echo '================================='

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

        stage('Health Check') {

            steps {

                echo '================================='
                echo 'ETAPA 7 - VALIDATION'
                echo '================================='

                sh '''

                    echo "Esperando inicio de servicios..."

                    sleep 10

                    curl -f \
                    http://nginx/health

                '''

            }

        }

        stage('Container Status') {

            steps {

                echo '================================='
                echo 'ESTADO DE CONTENEDORES'
                echo '================================='

                sh '''

                    docker compose ps

                '''

            }

        }

    }

    post {

        success {

            echo '================================='
            echo 'PIPELINE COMPLETADO CORRECTAMENTE'
            echo '================================='

        }

        failure {

            echo '================================='
            echo 'PIPELINE FALLÓ'
            echo '================================='

        }

        always {

            echo '================================='
            echo 'FINALIZANDO PIPELINE'
            echo '================================='

        }

    }

}