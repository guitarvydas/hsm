from simpletestbench5 import SimpleTestBench5
from message import Message

tb = SimpleTestBench5 (None, 'simpletestbench5')
#tb = SimpleTestBench (None, 'simpletestbench5')
tb.inject (Message (tb, 'start', True, None))
tb.run ()
print (tb.outputs ())
