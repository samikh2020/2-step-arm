pipeline {
    agent {dockerfile {filename 'Dockerfile' }}

    stages {
        stage('checkout') {
            steps {
                checkout scm
            }
        }
        stage('input1') {
            steps {
                    CMD [ "python", "./ip_print_final.py", "input1.json" ]
            }
        }
        stage('input2') {
            steps {
                   CMD [ "python", "./ip_print_final.py", "input2.json" ]
            }
        }
    }
}