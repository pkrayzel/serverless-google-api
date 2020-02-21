# serverless-google-api

This repo is based on this article for serverless: https://serverless.com/blog/serverless-python-packaging/

## Prerequisities

- node
- npm
- python 3.6
- AWS credentials configured

## Local setup

Create & activate virtual environment 

```
virtualenv google -p python3.6
source google/bin/activate
```

Install dependencies

``` 
pip install -r hello-world/requirements.txt
```

## Deployment to AWS

If you have configured AWS credentials in **~/.aws/credentials** then you can just run:

```
serverless deploy
```

Otherwise you can specify the credentials using:

``` 
serverless config credentials --provider aws --key 1234 --secret 5678
```

Then you should be able to run

```
serverless deploy
```

See https://serverless.com/framework/docs/providers/aws/cli-reference/config-credentials/