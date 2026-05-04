Passer au contenu principal
Conditions d’achèvement
pipeline {
    agent any

    triggers {
        pollSCM('* * * * *')  // vérifie toutes les minutes
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'VOTRE LIEN GIT'
            }
        }

        stage('Pull latest code') {
            steps {
                dir('VOTRE CHEMIN DU DOSSIER DU PROJET') {
                    git branch: 'main', url: 'VOTRE LIEN GIT'
                }
            }
        }

        stage('Install dependencies') {
            steps {
                dir('VOTRE CHEMIN DU DOSSIER DU PROJET') {
                    sh '''
                        source venv/bin/activate
                        pip install flask
                    '''
                }
            }
        }

        stage('Restart Flask app') {
            steps {
                script {
                    sh 'pkill -f "python app.py" || true'
                    sh '''
                        cd VOTRE CHEMIN DU DOSSIER DU PROJET
                        source venv/bin/activate
                        nohup python app.py > flask.log 2>&1 &
                    '''
                }
            }
        }
    }

    post {
        success {
            echo 'Déploiement automatique réussi ! BRAVO DAMN'
        }
        failure {
            echo 'Échec du pipeline. - AIE AIE AIE CA PUE'
        }
    }
}

