pipeline {
    agent any

    environment {
        IMAGE_NAME = 'world-of-games'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/slyw0w/WorldOfGames.git'
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Run') {
            steps {
                sh 'docker run -d -p 8777:8777 -v $PWD/Scores.txt:/Scores.txt --name world-of-games $IMAGE_NAME'
                sh 'sleep 5'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 e2e.py'
            }
        }

        stage('Finalize') {
            steps {
                sh 'docker stop world-of-games'
                sh 'docker rm world-of-games'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up'
            sh 'docker rm -f world-of-games || true'
        }
    }
}
