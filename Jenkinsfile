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
               sh '''
                    python3 -m venv env
                    . env/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage("Test") {
            steps {
                sh '''
                    . env/bin/activate
                    pytest --alluredir=allure-results
                '''
            }
        }

        stage('Generate Allure report') {
            steps {
                sh 'allure generate allure-results -o allure-report --clean'
            }
        }

        stage('Publish report') {
            steps {
                publishHTML(target: [
                    reportDir: 'allure-report',
                    reportFiles: 'index.html',
                    reportName: 'Allure Report'
                ])
            }
        }
    }
}