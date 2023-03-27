pipeline {
  agent any
  stages {
    stage('Pre Checks Before Deployment') {
      steps {
        sh 'python Hello.py'
        sh 'echo "This is Stage 1"'
      }
    }
    stage('Deployment') {
      steps {
        sh 'python Hello.py'
        sh 'echo "This is Stage 2"'
      }
    }
    stage('Post Checks After Deployment') {
      steps {
        sh 'python Hello.py'
        sh 'echo "This is Stage 3"'
      }
    }
    stage('Final Application Test') {
      steps {
        sh 'python Hello.py'
        sh 'echo "This is Stage 4"'
      }
    }
  }
}
