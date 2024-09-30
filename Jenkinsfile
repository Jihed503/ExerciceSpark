pipeline {
    agent {
        docker {
            image 'python:3.10-slim' // Utilisation d'une image Docker contenant Python 3.10
            args '-u root' // Exécuter avec les droits root pour installer des packages si nécessaire
        }
    }
    stages {
        stage("get_code") {
            steps {
                git branch: 'main', url: 'https://github.com/Jihed503/ExerciceSpark.git'
            }
        }
        stage("install pytest") {
            steps {
                sh '''
                # Vérifier la version de Python
                python --version
                
                # Installer pytest via pip
                pip install pytest
                pytest --version
                '''
            }
        }
    }
  }
