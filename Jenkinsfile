pipeline {
    agent any

    stages {
        stage("Get Code") {
            steps {
                script {
                    // Display the start of the process
                    bat 'echo ***********************************************************************'
                    
                    // Check Python version
                    bat 'python --version'

                    // Install pytest
                    bat 'pip install pytest'

                    // Check pytest version
                    bat 'pytest --version'
                }
            }
        }
        
        stage("Run Test") {
            steps {
                script {
                    // Run the pytest command on the specified test file
                    bat 'pytest ExerciceSpark/Glue code/exercice/test/test.py'
                }
            }
        }
    }
}
