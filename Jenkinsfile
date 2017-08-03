pipeline {
  agent {
    node {
      label 'docker-slave-jenkins'
    }
    
  }
  stages {
    stage('Build') {
      steps {
        sh 'ls -ltr /'
      }
    }
  }
}