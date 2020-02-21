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

```
serverless deploy
```