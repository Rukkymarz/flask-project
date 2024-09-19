pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/Rukkymarz/flask-project.git' 
        DEPLOY_DIR = '/home/ubuntu/' 
        EMAIL_RECIPIENTS = 'rukkymarz@gmail.com' 
    }

    stages {
        stage('Clone Repository') {
            steps {
                git "${REPO_URL}"
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }

        stage('Deploy to Production') {
            steps {
                sh '''
                    cp -r * ${DEPLOY_DIR}
                    cd ${DEPLOY_DIR}
                    # Example command to restart the Flask app
                    if pgrep -f "flask run"; then
                        pkill -f "flask run"
                    fi
                    nohup flask run --host=0.0.0.0 --port=5000 &
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
            mail to: "${EMAIL_RECIPIENTS}",
                 subject: "Jenkins Build Successful: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: "Good news! The build was successful.\n\nCheck console output at: ${env.RUN_DISPLAY_URL}"
        }
        failure {
            echo 'Pipeline failed!'
            mail to: "${EMAIL_RECIPIENTS}",
                 subject: "Jenkins Build Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: "Unfortunately, the build failed.\n\nCheck console output at: ${env.RUN_DISPLAY_URL}"
        }
    }
}
