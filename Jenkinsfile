// pipeline {
//     agent any

//     stages {
//         stage('Print Working Directory') {
//             steps {
//                 bat 'cd'
//             }
//         }

//         stage('Check Python Version') {
//             steps {
//                 bat 'python --version'
//             }
//         }

//         stage('Run Python Script') {
//             steps {
//                 bat 'python pythondemo.py'
//             }
//         }
//     }
// }

pipeline{
    agent any
    stages{
        stage("Listening the FIles"){
            steps{
            bat 'cd'
        }
        }
        stage("Python check version"){
            steps{
            bat 'python --version'
            }
        }
        stage("Running the file"){
            steps{
                bat 'python pythondemo.py'
            }
        }
        stage("Docker image pull"){
            steps{
                bat 'docker pull alpine:latest'
            }
        }
        stage("Docker run alpine"){
            steps{
                bat 'docker run -it --name AlpineRun alpine'
                bat 'docker ps -a'
            }
        }
        stage("Basics Alpine commnads"){
            step{
                 bat '''docker run --rm alpine:latest sh -c "echo Current Directory: && pwd && echo && echo Listing Files: && ls -la && echo && echo Kernel Info: && uname -a"
                 '''
                 }
        }
        stages("removiung the apline"){
            step{
                bat 'docker rm AlpineRun'
            }
        }
    }
    post{
        always{
            echo "Finished Succesfully"
        }
        success{
            echo "Run Succesfully XXXXXX"
        }
        failure{
            echo "------------++=+++_-------Error"
        }
    }
}