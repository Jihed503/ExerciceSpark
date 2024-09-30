pipeline {
    agent {
        docker {
            image 'pytest/pytest' // Utilisation d'une image Docker contenant pytest
            args '-u root' // Exécuter avec les droits root si nécessaire
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
  
