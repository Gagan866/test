pipeline{
    agent any
    stages{
        stage("Checkout code"){
            steps{
                git url:"https://github.com/Gagan866/test.git", branch:"main"
            }
        }
        stage("Install dependencies"){
            steps{
                bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate
                    python -m pip install --upgrade pip
                    pip install requirements.txt
                    '''
            }
        }
        stage("Run tests"){
            steps{
                bat '''
                    call venv\\Scripts\\activate
                    pytest test_con.py --maxfail=1 --disable-warnings
                    '''
            }
        }
        stage("Deploy"){
            steps{
                echo "Deploying application"
                bat '''
                    call venv\\Scripts\\activate
                    python conditions.py
                    '''
            }
        }

    }
    post{
        success{
            echo "pipeline executed successfully"
        }
        failure{
            echo "pipelime execution failed"
        }
    }
}