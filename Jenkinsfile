pipeline {
  agent any
  stages {
    stage('error') {
      steps {
        echo 'running python script'
      }
    }
    stage('run') {
      steps {
        sh '''#!/usr/bin/env
python y_statistics.py --q "natural"'''
      }
    }
  }
}