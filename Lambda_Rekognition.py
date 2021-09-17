from decimal import Decimal
import json
import urllib.request
import urllib.parse
import urllib.error
import urllib
import boto3
import uuid
import os
import logging

print('Loading function')

rekognition = boto3.client('rekognition')
client = boto3.client('sns')
s3_client = boto3.client("s3")


# --------------- Helper Functions to call Rekognition APIs ------------------



def detect_labels(bucket, key):
    response = rekognition.detect_labels(Image={"S3Object": {"Bucket": bucket, "Name": key}})

    # Sample code to write response to DynamoDB table 'MyTable' with 'PK' as Primary Key.
    # Note: role used for executing this Lambda function should have write access to the table.
    #table = boto3.resource('dynamodb').Table('MyTable')
    #labels = [{'Confidence': Decimal(str(label_prediction['Confidence'])), 'Name': label_prediction['Name']} for label_prediction in response['Labels']]
    #table.put_item(Item={'PK': key, 'Labels': labels})
    return response



# --------------- Main handler ------------------


def lambda_handler(event, context):
    '''Demonstrates S3 trigger that uses
    Rekognition APIs to detect faces, labels and index faces in S3 Object.
    '''
    #print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
    destination_bucket_name = "analyzedimage"
    try:


        # Calls rekognition DetectLabels API to detect labels in S3 object
        response = detect_labels(bucket, key)
       
        tosend = ""
        #for Label in response["Labels"][0]:
            #print(Label)
        #print(response["Labels"])
        Label = response["Labels"][0]
        if Label["Name"] == 'Horse' and Label["Confidence"] >= 98:
            print('Quality test is passed. Image detected as: {0} - {1}%'.format(Label["Name"], Label["Confidence"]))
            tosend += 'Quality test is passed. Image detected as: {0} - {1}%'.format(Label["Name"], Label["Confidence"])
            test = "passed"
        else:
            print('Quality test is not passed for Horse')
            tosend += 'Quality test is not passed for Horse'
            test = "failed"
               
        # Copy Source Object
        copy_source_object = {'Bucket': bucket, 'Key': key}
    
        # S3 copy object operation
        fileNameComponents = key.split('.')
        s3_client.copy_object(CopySource=copy_source_object, Bucket=destination_bucket_name, Key=fileNameComponents[0]+"_"+test+"."+fileNameComponents[1])


        # Print response to console.
        print(response)
       
        #response = client.publish(TargetArn='arn:aws:sns:us-east-1:033661994053:New_SNS_Topic:7c55483d-f3fb-4548-8bd8-0454f7975bf8', Message=tosend, Subject='Uploaded Image Labels')
