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
              virtualenv venv --distribute
              . venv\bin\activat                    
              pip install pytest
                    bat 'pytest --version'
                }
            }
        }
    }
  }
