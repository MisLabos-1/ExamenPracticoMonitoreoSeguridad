vpipeline {

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

        stage('Secret Scan - Gitleaks') {

            steps {

                echo 'Buscando secretos'

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

        stage('Tests') {

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

        stage('Vulnerability Scan - Trivy') {

            steps {

                echo 'Analizando vulnerabilidades'

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