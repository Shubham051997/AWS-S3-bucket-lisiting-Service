from flask import Flask, jsonify, request
import boto3
import os

app = Flask(__name__)

# Configure AWS S3 client
s3_client = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)

BUCKET_NAME = 'my-second-bucket-on2n'  # mybucket name on aws console

@app.route('/list-bucket-content', defaults={'path': ''}, methods=['GET'])
@app.route('/list-bucket-content/<path:path>', methods=['GET'])
def list_bucket_content(path):
    try:
        response = s3_client.list_objects_v2(Bucket=BUCKET_NAME, Prefix=path, Delimiter='/')
        content = []
        if 'CommonPrefixes' in response:
            for prefix in response['CommonPrefixes']:
                content.append(prefix['Prefix'].rstrip('/').split('/')[-1])
        if 'Contents' in response:
            for obj in response['Contents']:
                if obj['Key'] != path and '/' not in obj['Key'][len(path):]:
                    content.append(obj['Key'].split('/')[-1])
        return jsonify({"content": content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="192.168.56.1", port="5000", debug=True)
