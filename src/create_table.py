import boto3

db = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url='http://dynamodb-local:8000')
table = db.create_table(
    TableName='ut_table',
    AttributeDefinitions=[
        {
            'AttributeName': 'primary',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'second',
            'AttributeType': 'N'
        },
    ],
    KeySchema=[
        {
            'AttributeName': 'primary',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'second',
            'KeyType': 'RANGE'
        },
    ],
    BillingMode='PAY_PER_REQUEST',
)