pipeline {
    agent any
    stages {
        stage("get_code") {
            steps {
                git 'https://github.com/Jihed503/ExerciceSpark'
            }
        }
        stage("install pip and pytest") {
            steps {
                // Install pip if it's not already installed (Windows)
                bat '''
                @echo off
                python -m ensurepip --upgrade || (
                    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
                    python get-pip.py
                )
                '''
                // Install pytest
                bat 'pip install pytest'
            }
        }
        stage("run test") {
            steps {
                bat 'pytest ExerciceSpark/Glue code/exercice/test/test.py'
            }
        }
    }
    post {
        always {
            // Generate test reports
            junit '**/test-results.xml'
        }
    }
}
