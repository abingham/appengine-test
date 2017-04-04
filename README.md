# appengine-test
A sandbox for figuring out appengine

This is currently the start of an attempt to recover some experiments I did a
while back. None of this is very meaningful, but at some point I managed to get
an appengine endpoint sending messages through pubsub to a script running on a
compute engine VM, and I want to eventually revisit that. So, as I recall...

monitor.py is the script that ran on the compute engine node. It subscribed to a
pubsub topic and waited for a message, printing it when/if it arrived.

python-gae-quickstart/ is a clone of some python-appengine quickstart repo. The
main point of interest here is main.py's "/" route wherein I send a message to
pubsub. This is the whole point of the exercise...how to make an appengine
endpoint send a message through to a compute engine process. Once I can do this,
a lot of options become available.
