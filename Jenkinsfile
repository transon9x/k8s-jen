pipeline {
  agent {
    kubernetes {
      idleMinutes 5
      yamlFile 'agent.yaml'  
      defaultContainer 'python'  
    }
  }

  environment {
      DOCKERHUB_PW = credentials('docker-passwd')
  }
  
  stages {
      stage('Python runner env') {
          steps {
              sh 'python -V'
          }
      }
      stage('Python install lib') {
          steps {
              sh 'pip3 install -r requirements.txt'
          }
      }
      stage('Python run app.py') {
          steps {
              sh 'python app.py'
          }
      }
      
      stage('Build and push Docker Im') {
          steps {
            container('docker') {  
              sh "docker build -t sontran9xz/python-simple-app:$BUILD_NUMBER ."
              sh "docker login -u sontran9xz -p $DOCKERHUB_PW"
              sh "docker push sontran9xz/python-simple-app:$BUILD_NUMBER"
            }
          }
      }
  }
}
