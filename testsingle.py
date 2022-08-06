from lamptester import LampTester
from message import Message

lamptester = LampTester (None, 'lamp tester')
lamptester.inject (Message (lamptester, 'start', True, None))
lamptester.run ()
print (lamptester.outputs ())
