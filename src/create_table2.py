import boto3

db = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url='http://dynamodb-local:8000')
table = db.create_table(
    TableName='test_table',
    AttributeDefinitions=[
        {
            'AttributeName': 'pk',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'sort',
            'AttributeType': 'N'
        },
    ],
    KeySchema=[
        {
            'AttributeName': 'pk',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'sort',
            'KeyType': 'RANGE'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 100,
        'WriteCapacityUnits': 100
    },
)