
pipeline {
    agent any

    environment {
        IMAGE_NAME = 'student-management'
        CONTAINER_NAME = 'student-app'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t student-management:${BUILD_NUMBER} .'
            }
        }

        stage('Test') {
            steps {
                sh '''
                    docker run --rm \
                      --entrypoint python \
                      student-management:${BUILD_NUMBER} \
                      -m pytest -v
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker rm -f student-app || true

                    docker run -d \
                      --restart unless-stopped \
                      --name student-app \
                      -p 5000:5000 \
                      student-management:${BUILD_NUMBER}
                '''
            }
        }

        stage('Verify') {
            steps {
                sh '''
                    for i in 1 2 3 4 5 6 7 8 9 10; do
                        if curl -fsS http://localhost:5000/health; then
                            exit 0
                        fi
                        sleep 2
                    done

                    docker logs student-app
                    exit 1
                '''
            }
        }
    }

    post {
        success {
            echo 'Application deployed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check console output.'
        }
    }
}

pipeline {
    agent any

    environment {
        IMAGE_NAME = 'student-management'
        CONTAINER_NAME = 'student-app'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t student-management:${BUILD_NUMBER} .'
            }
        }

        stage('Test') {
            steps {
                sh '''
                    docker run --rm \
                      --entrypoint python \
                      student-management:${BUILD_NUMBER} \
                      -m pytest -v
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker rm -f student-app || true

                    docker run -d \
                      --restart unless-stopped \
                      --name student-app \
                      -p 5000:5000 \
                      student-management:${BUILD_NUMBER}
                '''
            }
        }

        stage('Verify') {
            steps {
                sh '''
                    for i in 1 2 3 4 5 6 7 8 9 10; do
                        if curl -fsS http://localhost:5000/health; then
                            exit 0
                        fi
                        sleep 2
                    done

                    docker logs student-app
                    exit 1
                '''
            }
        }
    }

    post {
        success {
            echo 'Application deployed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check console output.'
        }
    }
}
