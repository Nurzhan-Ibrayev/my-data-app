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
                sh '''
                    . venv/bin/activate
                    pytest test_app.py
                '''
            }
}

        stage('Build Docker image') {
            steps {
                sh '''
                    docker build -t myapp:latest .
                '''
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
