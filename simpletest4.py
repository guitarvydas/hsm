from simpletestbench4 import SimpleTestBench4
from message import Message

tb = SimpleTestBench4 (None, 'simpletestbench4')
#tb = SimpleTestBench (None, 'simpletestbench4')
tb.inject (Message (tb, 'start', True, None))
tb.run ()
print (tb.outputs ())
