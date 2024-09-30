pipeline {
    agent any
    stages {

        stage('Install pip and pytest') {
            steps {

                bat 'pip install pytest'
                bat 'pytest --version'


            }
        }
        stage('Run Tests') {
            steps {
                bat 'pytest ExerciceSpark/Glue/exercice/test/test.py '
            }
        }
    }
}
