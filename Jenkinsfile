  pipeline{
    agent any
    stages{
        stage("get_code"){
            steps {
                git branch: 'main', url: 'https://github.com/Jihed503/ExerciceSpark.git'
            }
        }
        stage("install pytest"){
            steps {
              bat 'pip install pytest'
              bat 'pytest --version'

    }
  }
    }
  }
