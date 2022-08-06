from simpletestbench2 import SimpleTestBench2
from message import Message

tb = SimpleTestBench2 (None, 'simpletestbench2')
#tb = SimpleTestBench (None, 'simpletestbench2')
tb.inject (Message (tb, 'start', True, None))
tb.run ()
print (tb.outputs ())
