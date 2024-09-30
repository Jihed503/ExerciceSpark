  pipeline{
    agent any
    stages{
        stage("get_code"){
            steps {
                git branch: 'main', url: 'https://github.com/Jihed503/ExerciceSpark.git'
            }
        }
        stage("install pytest"){
            steps{
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
