pipeline {
    agent any

    triggers {
        githubPush()             // declenche par le webhook GitHub (relaye via ngrok)
        pollSCM('* * * * *')     // filet de securite : verifie le depot chaque minute
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/DQuentinD/devops-158-helder_quentin-tp.git'
            }
        }

        stage('Pull latest code') {
            steps {
                dir('/var/lib/jenkins/devops-158-helder_quentin-tp') {
                    git branch: 'main', url: 'https://github.com/DQuentinD/devops-158-helder_quentin-tp.git'
                }
            }
        }

        stage('Install dependencies') {
            steps {
                dir('/var/lib/jenkins/devops-158-helder_quentin-tp') {
                    sh '''
                        [ -d venv ] || python3 -m venv venv
                        . venv/bin/activate
                        pip install flask pytest
                    '''
                }
            }
        }

        stage('Run unit tests') {
            steps {
                dir('/var/lib/jenkins/devops-158-helder_quentin-tp') {
                    sh '''
                        . venv/bin/activate
                        python -m pytest test_app.py -v --tb=short
                    '''
                }
            }
            post {
                success {
                    echo 'Tous les tests unitaires sont passes avec succes !'
                }
                failure {
                    echo 'Echec des tests unitaires. Le deploiement est annule.'
                }
            }
        }

        stage('Restart Flask app') {
            steps {
                script {
                    sh 'pkill -f "python app.py" || true'
                    sh '''
                        cd /var/lib/jenkins/devops-158-helder_quentin-tp
                        . venv/bin/activate
                        JENKINS_NODE_COOKIE=dontKillMe nohup python app.py > flask.log 2>&1 &
                    '''
                }
            }
        }
    }

    post {
        success {
            echo 'Deploiement automatique reussi ! BRAVO DAMN'
        }
        failure {
            echo 'Echec du pipeline. - AIE AIE AIE CA PUE'
        }
    }
}
