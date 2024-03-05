## Deployment of FastAPI, Transformer with AWS Fargate using CDK

### Overview
![aws.png](..%2Fimages%2Faws.png)
### Deploying the stack

Execute the following commands to install CDK and make sure you have the right dependencies:

```
npm install -g aws-cdk@2.51.1
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

Once this is installed, you can execute the following commands to deploy the inference service into your account:

```![img_1.png](img_1.png)
ACCOUNT_ID=$(aws sts get-caller-identity --query Account | tr -d '"')
AWS_REGION=$(aws configure get region)
cdk bootstrap aws://${ACCOUNT_ID}/${AWS_REGION}
cdk deploy --parameters ProjectName=mlflow --require-approval never
```
![img 2.png](..%2Fimages%2Fimg%202.png)
## Load Balancer URL (Ready for testing)
```
FastAP-FastA-LwNQPNCUV6mk-1271608237.us-east-2.elb.amazonaws.com
```
## Endpoint with cosine similarities
```
curl --location --request POST 'http://FastAP-FastA-LwNQPNCUV6mk-1271608237.us-east-2.elb.amazonaws.com/query/details' --header 'Content-Type: application/json' --data-raw '{"sentence": "feeling like a million bucks", "labels": ["happy", "sad", "rich"]}'
```
## Endpoint with single output
```
curl --location --request POST 'http://FastAP-FastA-LwNQPNCUV6mk-1271608237.us-east-2.elb.amazonaws.com/query' --header 'Content-Type: application/json' --data-raw '{"sentence": "feeling like a million bucks", "labels": ["happy", "sad", "rich"]}'
```
****
