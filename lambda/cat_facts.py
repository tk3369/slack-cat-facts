import json
import requests

def handler(event, context):
    print('request: {}'.format(json.dumps(event)))
    return process()

def process():
    try:
        res = requests.get('https://catfact.ninja/fact')
        fact = res.json()['fact']
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'text': '😸😸😸 Did you know... ' + fact,
                'response_type': 'in_channel'
            })
        }
    except:
        print('Unable to process request.')
        return {
            'statusCode': 500,
        }
        
# for testing only
if __name__== "__main__":
    print('testing lambda function')
    print(process())