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
                sh 'python -m venv venv00'
                sh './venv00/bin/pip install -U pip && ./venv00/bin/pip install --user pytest'
                sh './venv00/bin/pytest'
            }
        }
    }
}