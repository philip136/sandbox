pipeline {
    agent any
    stages {
        stage("Checkout") {
            steps {
                git branch: "master", url: "https://github.com/philip136/sandbox.git"
            }
        }

        stage("Build") {
            steps {
                sh "python3 -m venv env"
                sh "source /env/bin/activate"
                sh "pip install -r requirements.txt"
            }
        }

        stage("Test") {
            sh "pytest"
        }
    }
}