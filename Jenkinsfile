pipeline {
    agent: any

    parameters {
        string(name: "output", defaultValue: "")
    }

    stage("Read file") {
        steps {
            tmp_param =  sh (script: 'cat test_first.py', returnStdout: true).trim()
            env.output = tmp_param
        }
    }

    stage("Output") {
        steps {
            sh "echo ${env.output}"
        }
    }
}