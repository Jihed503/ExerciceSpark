pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                script {
                    def gitBranch = 'main'
                    checkout([
                        $class: 'GitSCM',
                        branches: [[name: gitBranch]],
                        userRemoteConfigs: [[url: 'https://github.com/Jihed503/ExerciceSpark.git']]
                    ])
                }
            }
        }
        stage('Install pip and pytest') {
            steps {
                bat 'python -m ensurepip'
                bat 'python -m pip install --upgrade pip'
                bat 'pip install pytest'
            }
        }
        stage('Run Tests') {
            steps {
                bat 'pytest ExerciceSpark/Glue\\ code/exercice/test/test.py --junitxml=test-results.xml'
            }
        }
    }
    post {
        always {
            junit '**/test-results.xml' // Génération de rapports de tests
        }
    }
}
