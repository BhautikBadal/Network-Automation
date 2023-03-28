pipeline {
  agent any
  stages {
    stage('Pre Checks Before Deployment') {
      steps {
        sh 'pip install requests'
        sh 'python PreChecks.py'
        sh 'echo "This is Stage 1"'
      }
    }
    stage('Deployment') {
      steps {
        sh 'pip install requests'
        sh 'python Deployment.py'
        sh 'echo "This is Stage 2"'
      }
    }
    stage('Post Checks After Deployment') {
      steps {
        sh 'pip install requests'
        sh 'python PostChecks.py'
        sh 'echo "This is Stage 3"'
      }
    }
    stage('Final Application Test') {
      steps {
        sh 'pip install requests'
        sh 'python CleanUp.py'
        sh 'echo "This is Stage 4"'
      }
    }
  }
}
