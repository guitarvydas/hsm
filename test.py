from lamp import Lamp
from message import Message

lamp = Lamp (None, 'lamp')
lamp.inject (Message (lamp, 'pwr', True, None))
lamp.inject (Message (lamp, 'brightness', True, None))
lamp.inject (Message (lamp, 'colour', True, None))
lamp.inject (Message (lamp, 'pwr', True, None))
lamp.run ()
