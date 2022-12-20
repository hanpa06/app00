pipeline{
    agent {
        docker { image 'python:3.10' }
    }
    stages{
        stage('stage00'){
            steps{
                echo 'step00-00'
                echo 'step00-01'
            }
        }
        stage('stege01'){
            steps{
                echo 'step01-00'
                echo 'step01-01'
            }
        }
        stage('test'){
            steps{
                sh 'pip install -U pip && pip install pytest'
                sh 'pytest'
            }
        }
    }
}