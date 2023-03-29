pipeline {
  agent any
  stages {
    stage('Install requirements') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'pip install requests'
            }
        }
    stage('UAT Checks Before Deployment') {
      steps {
        // sh 'echo "----------Stage 0 is Started----------"'
        sh 'python3 UAT_Checks.py'
        sh 'echo "----------Stage 0 is Finished----------"'
      }
    }
    stage('Pre Checks Before Deployment') {
      steps {
        // sh 'echo "----------Stage 1 is Started----------"'
        sh 'python3 PreChecks.py'
        sh 'echo "----------Stage 1 is Finished----------"'
      }
    }
    stage('Deployment') {
      steps {
        // sh 'echo "----------Stage 2 is Started----------"'
        sh 'python3 Deployment.py'
        sh 'echo "----------Stage 2 is Finished----------"'
      }
    }
    stage('Post Checks After Deployment') {
      steps {
        // sh 'echo "----------Stage 3 is Started----------"'
        sh 'python3 PostChecks.py'
        sh 'echo "----------Stage 3 is Finished----------"'
      }
    }
    stage('UAT Checks after Deployment') {
      steps {
        // sh 'echo "----------Stage 4 is Started----------"'
        sh 'python3 UAT_Checks.py'
        sh 'echo "----------Stage 4 is Finished----------"'
      }
    }
    stage('Final Application Test') {
      steps {
        // sh 'echo "----------Stage 5 is Started----------"'
        sh 'python3 CleanUp.py'
        sh 'echo "----------Stage 5 is Finished----------"'
      }
    }
  }
}
