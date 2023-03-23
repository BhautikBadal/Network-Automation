pipeline {
  agent any
  stages {
    stage('Countdown 1') {
      steps {
        sh 'python countdown.py'
        sh 'echo "This is Stage 1"'
      }
    }
    stage('Countdown 2') {
      steps {
        sh 'python countdown.py'
        sh 'echo "This is Stage 2"'
      }
    }
    stage('Countdown 3') {
      steps {
        sh 'python countdown.py'
        sh 'echo "This is Stage 3"'
      }
    }
    stage('Final Countdown') {
      steps {
        sh 'python countdown.py'
        sh 'echo "This is Stage 4"'
      }
    }
  }
}
