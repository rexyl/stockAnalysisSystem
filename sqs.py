import boto.sqs
import _config as cfg
from base64 import b64decode
from boto.sqs.message import RawMessage

conn = boto.sqs.connect_to_region("us-east-1", aws_access_key_id=cfg.AccessKeyID, 
	aws_secret_access_key=cfg.SecretAccessKey)
stock_queue = conn.get_queue('stock_queue')

def send(msg):
	RawMessage(stock_queue, b64decode(msg))