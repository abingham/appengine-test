# Imports the Google Cloud client library
from google.cloud import pubsub
from google.cloud.pubsub.subscription import AutoAck
# Instantiates a client
pubsub_client = pubsub.Client()
# The name for the new topic
topic_name = 'work-requests'
# Prepares the new topic
topic = pubsub_client.topic(topic_name)
subscription = topic.subscription('worker')
if not subscription.exists():
    subscription.create()
with AutoAck(subscription, max_messages=1) as ack:
    for ack_id, message in list(ack.items()):
        try:
            print(message.message_id, message.data, message.attributes)
        except Exception:  # pylint: disable=broad-except
            del ack[ack_id]
