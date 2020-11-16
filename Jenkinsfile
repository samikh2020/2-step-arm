pipeline {
    agent {    dockerfile {
        filename 'Dockerfile'
        dir './'
        label 'python-docker'
    }

    stages {
        stage('checkout') {
            steps {
                checkout scm
            }
        }
        stage('input1') {
            steps {
                    sh """
                    python ip_print_final.py input1.json
                    """
            }
        }
        stage('input2') {
            steps {
                    sh """
                    python ip_print_final.py input2.json
                    """            }
        }
    }
}
