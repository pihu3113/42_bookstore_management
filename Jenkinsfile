pipeline {
    agent {
        docker {
            image 'python:3.9-slim'
        }
    }
    
    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'python manage.py check'
            }
        }
        
        stage('Test') {
            steps {
                sh 'python manage.py test'
            }
        }
        
        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                sh 'python manage.py collectstatic --noinput'
                sh 'python manage.py migrate'
                
                // Here you would typically deploy to your server
                echo 'Deploying to production server...'
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
        success {
            echo 'Build, Test, and Deploy successful!'
        }
        failure {
            echo 'Build or tests failed. Check the logs for details.'
        }
    }
} 