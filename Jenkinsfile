pipeline { 
    agent any

    environment {
        registry = "satson88"  // Replace with your Docker registry URL
        DOCKERHUB_CREDENTIALS= credentials('docker-satson88')
        imageName = "python-demo"  // Replace with your desired image name
        containerName = "python-app-container"  // Replace with your desired container name
        dockerfilePath = "./Dockerfile"  // Replace with the path to your Dockerfile
        dockerArgs = "-p 8085:5000"  // Replace with your desired container arguments
        version = sh(script: 'jq \'.version\' version.json', returnStdout: true).trim()
    }
    stages {
        stage('Clean WS') { 
            steps { 
                cleanWs()
            }
        }
        stage('SCM'){
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/satson88/python-demo.git']])
            }
        }
        
        stage('Docker Login') {
            steps {
                   sh 'echo $DOCKERHUB_CREDENTIALS_PSW | sudo docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'     		 
                }
            }
        

        stage('Build') {
            steps {
                
                sh "sudo docker build -t ${registry}/${imageName}:${version} -f ${dockerfilePath} ."
            }
        }
        
        stage('Push to Artifcatory') {
            steps {
                sh "sudo docker push ${registry}/${imageName}:${version}"
            }
        }

         /*stage('Code Analysis') {
            steps {
                sh "/opt/sonar-scanner/bin/sonar-scanner \
                    -Dsonar.projectKey=python-demo \
                    -Dsonar.sources=. \
                    -Dsonar.host.url=http://sonar.manolabs.co.in:9000 \
                    -Dsonar.login=sqp_e0ba0ddf058d127efdd87598d5d6ec0a66e1680f"
            }
        }*/

        stage('Deploy') {
            steps {
                 sh '''
                ssh root@10.0.1.205 <<  EOF
                
                docker rm  -f ${containerName} 1> /dev/null 2>&1

                sleep 5

                docker run -d --name ${containerName} ${dockerArgs} ${registry}/${imageName}:${version}

                exit

                EOF

                '''
            }
        }
    }
}
