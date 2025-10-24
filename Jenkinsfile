pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
}


        stage('Run tests') {
            steps {
                sh 'pytest test_app.py'
            }
        }

        stage('Build Docker image') {
            steps {
                script {
                    docker.build('my-data-app:latest')
                }
            }
        }
    }

    post {
        success {
            echo '✅ Build and tests passed successfully!'
        }
        failure {
            echo '❌ Build or tests failed!'
        }
    }
}
