  pipeline{
    agent any
    stages{
        stage("get_code"){
            steps {
                git branch: 'main', url: 'https://github.com/Jihed503/ExerciceSpark.git'
            }
        }
        stage("set python environment") {
            steps {
                // Set PYTHONHOME and PATH environment variables
                withEnv(['PYTHONHOME=C:/Program Files/Python310', 'PATH=C:/Program Files/Python310;C:/Program Files/Python310/Scripts;%PATH%']) {
                    bat 'python --version'
                    bat 'pip install pytest'
                    bat 'pytest --version'
                }
            }
        }
    }
  }
