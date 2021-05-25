import boto3

class DbHandler:
    dynamodb = boto3.resource('dynamodb')

    def subscribe(self, email, application):
        
        table = self.dynamodb.Table('subscribers')

        response = table.update_item(
            Key={
                'email': email
            },
            UpdateExpression="Add apps :application",

            ExpressionAttributeValues={
                ':application': {application}
            },
            ReturnValues="UPDATED_NEW"
        )
        return response

    def unsubscribe(self, email, application):
        table = self.dynamodb.Table('subscribers')
        
        response = table.update_item(
            Key={
                'email': email
            },
            UpdateExpression="delete apps :application",

            ExpressionAttributeValues={
                ':application': {application}
            },
            ReturnValues="UPDATED_NEW"
        )
        return response