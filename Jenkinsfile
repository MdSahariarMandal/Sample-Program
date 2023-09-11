pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Check out the code from the GitHub repository
                script {
                    checkout scm
                }
            }
        }

        stage('Run Python File Locally') {
            steps {
                // Run a specific Python file on your local machine
                script {
                    sh 'ASCII.py' // Replace 'your-python-file.py' with the actual file name
                }
            }
        }
    }
}
