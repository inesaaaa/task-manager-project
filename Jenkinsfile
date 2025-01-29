pipeline {
    agent {
        docker {
            image 'jetbrains/qodana-python:2024.3'
            args '--entrypoint="" -v ${WORKSPACE}:/data/project'
        }
    }
    environment {
        QODANA_TOKEN = credentials('qodana-token')
        QODANA_ENDPOINT = 'https://qodana.cloud'
    }
    stages {
        stage('Qodana Run') {
            steps {
                sh 'qodana'
            }
        }
    }
}