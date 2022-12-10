import json

# import requests


def lambda_handler(event, context):
    """Sample pure Lambda function"""
    num1= event["num1"]
    num2= event["num2"]

    print(add(num1,num2))
    print(sub(num1,num2))
    print(multi(num1,num2))

def add(num1,num2):
    return num1 + num2

def sub(num1,num2):
    return num1 - num2

def multi(num1,num2):
    return num1 * num2    