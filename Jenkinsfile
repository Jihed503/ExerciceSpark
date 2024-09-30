pipeline {
    agent any
    stages {
        stage("get_code") {
            steps {
                git branch: 'main', url: 'https://github.com/Jihed503/ExerciceSpark'
            }
        }
        stage('Install pip and pytest') {
    steps {
        bat 'python -m ensurepip'
        bat 'python -m pip install --upgrade pip'
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
