
pipeline {
    agent any

    stages {
        stage('GitHub Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Pytest') {
            steps {
                bat 'python -m pip install pytest'
            }
        }

        stage('Run Python Tests') {
            steps {
                bat 'python -m pytest -v'
            }
        }

        stage('Docker Build') {
            steps {
                bat 'docker build -t student-grade-app .'
            }
        }

        stage('Docker Test') {
            steps {
                bat 'docker run --rm student-grade-app python -m pytest -v'
            }
        }
    }
}

