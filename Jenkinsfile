pipeline {
    agent {
        docker {
            image 'atcsecure/pytest:latest' // Utilisation d'une image Docker contenant pytest
        }
    }
    stages {
        stage("get_code") {
            steps {
                git branch: 'main', url: 'https://github.com/Jihed503/ExerciceSpark.git'
            }
        }
        stage("run test") {
            steps {
                sh '''
                    pytest --version
                '''
            }
        }
    }
    }
  
