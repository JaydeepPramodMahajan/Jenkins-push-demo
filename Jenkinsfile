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
    }
    post{
        always{
            bat "Finished Succesfully"
        }
        success{
            bat "Run Succesfully XXXXXX"
        }
        failure{
            bat "------------++=+++_-------Error"
        }
    }
}