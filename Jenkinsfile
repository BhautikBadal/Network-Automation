pipeline {
  agent any
  stages {
    stage('Install requirements') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'pip install requests'
            }
        }
    stage('Pre Checks Before Deployment') {
      steps {
        sh 'python3 PreChecks.py'
        sh 'echo "This is Stage 1"'
      }
    }
    stage('Deployment') {
      steps {
        sh 'python3 Deployment.py'
        sh 'echo "This is Stage 2"'
      }
    }
    stage('Post Checks After Deployment') {
      steps {
        sh 'python3 PostChecks.py'
        sh 'echo "This is Stage 3"'
      }
    }
    stage('Final Application Test') {
      steps {
        sh 'python3 CleanUp.py'
        sh 'echo "This is Stage 4"'
      }
    }
  }
}
