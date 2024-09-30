pipeline{
    agent any
    stages{
        stage("get_code"){
            steps{
 
                bat 'python --version'
                bat 'pip install pytest'
                bat 'pytest --version'
            }
        }
        stage("run test"){
            steps{
                bat 'pytest ExerciceSpark/Glue code/exercice/test/test.py'
        }
    }
 
 
    }
}
