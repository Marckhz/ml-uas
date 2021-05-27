import joblib
import boto3
import os
import requests
from io import BytesIO

def main(data):
    #args recieve a dict
    target = data['review']
    s3 = (
            boto3.session.Session(aws_access_key_id=data['aws_access_key_id'],
                                aws_secret_access_key=data['aws_secret_access_key'])
                                .client('s3', region_name='us-south',
                    endpoint_url=data['endpoint_url'])
        )
    url = s3.generate_presigned_url('get_object', Params={'Bucket':data['bucket'], 'Key':data['model_name']}, ExpiresIn=600)
    url_request = BytesIO(requests.get(url).content)
    pipe = joblib.load(url_request)
    prediction = pipe.predict([target]).tolist()[0]
    return {
        'body':{
            'data':{
                'sentiment':prediction
            }
        },
        'statusCode':200,
        'headers':{'Content-Type':'application/json'}
    }
