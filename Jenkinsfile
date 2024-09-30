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
                // Install pip if it's not already installed (Windows)
                bat '''
                @echo off
                python -m ensurepip --upgrade || (
                    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
                    python get-pip.py
                )
                '''
                // Install pytest
                bat 'pip install pytest'
            }
        }
        stage("run test"){
            steps {
              bat 'pytest ExerciceSpark/Glue code/exercice/test/test.py --junitxml=test-results.xml'
            }
        }
    }
     post {
        always {
            // Génération de rapports de tests
            junit '**/test-results.xml'
        }
    }
  }
