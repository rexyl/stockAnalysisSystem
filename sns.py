import boto.sns
import _config as cfg

c = boto.sns.connect_to_region("us-east-1", aws_access_key_id=cfg.AccessKeyID, aws_secret_access_key=cfg.SecretAccessKey)
topicname = "stock_topic"
topicarn = "arn:aws:sns:us-east-1:355140900634:stock_topic"
emailaddress = "yanglu1589@gmail.com"

sns_client = boto.sns.SNSConnection(aws_access_key_id=cfg.AccessKeyID, aws_secret_access_key=cfg.SecretAccessKey)
def send(msg):
	pub = c.publish(topic=topicarn, message=msg)
