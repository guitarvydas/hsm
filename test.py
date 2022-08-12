from lamp import Lamp
from message import Message

l = Lamp (None, 'lamp')
l.inject (Message (l, 'pwr', True, None))
l.inject (Message (l, 'brightness', True, None))
l.run ()
print (l.outputs ())

