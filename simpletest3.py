from simpletestbench3 import SimpleTestBench3
from message import Message

tb = SimpleTestBench3 (None, 'simpletestbench3')
#tb = SimpleTestBench (None, 'simpletestbench3')
tb.inject (Message (tb, 'start', True, None))
tb.run ()
print (tb.outputs ())
