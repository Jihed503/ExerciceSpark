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
                // Install Python if it's not installed (Windows)
                bat '''
                @echo off
                python --version || (
                    echo Installing Python...
                    curl -o python-installer.exe https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe
                    start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1
                    python3 --version
                )
                '''

                // Install pip if it's not installed
                bat '''
                python -m ensurepip --upgrade || (
                    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
                    python3 get-pip.py
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
