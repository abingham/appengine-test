from flask import Flask
from google.cloud import pubsub

app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

# Instantiates a client
pubsub_client = pubsub.Client()
# The name for the new topic
topic_name = 'work-requests'
# Prepares the new topic
topic = pubsub_client.topic(topic_name)

counter = 0


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    global counter

    topic.publish('foobar {}'.format(counter).encode('utf-8'))
    counter += 1
    return '\'sup, World?'


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
