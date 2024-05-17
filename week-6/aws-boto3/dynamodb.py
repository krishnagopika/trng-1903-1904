import boto3

dynamodb = boto3.resource('dynamodb')

# Creating a table
table = dynamodb.create_table(
    TableName='Music',
    KeySchema=[
        {
            'AttributeName': 'Artist',
            'KeyType':'HASH'
        },
        {
            'AttributeName': 'SongTitle',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'Artist',
            'AttributeType':'S'
        },
        {
            'AttributeName': 'SongTitle',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

print(table.table_status)


table = dynamodb.Table('Music')

table.put_item(
    Item={
        'Artist':'Taylor Swift',
        'SongTitle': 'Exile',
        'AlbumTitle': 'Folklore',
        'Genre':'Pop'

    }
)

response = table.get_item(
    Key={
        'Artist': 'Taylor Swift',
        'SongTitle': 'Exile'
    }
)


result = response.get("Item")

result["SongTitle"] = "Blank Space"
result["AlbumTitle"] = "1989 TV"


table.put_item(Item=result)


response = table.get_item(
    Key={
        'Artist': 'Taylor Swift',
        'SongTitle': 'Blank Space'
    }
)

result = response["Item"]

print(result)


# delete item 
table.delete_item(
    Key={
        'Artist': 'Taylor Swift',
        'SongTitle': 'Blank Space'
    }
)

