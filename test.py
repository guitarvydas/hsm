from testbench import TestBench
from message import Message

tb = TestBench (None, 'simpletestbench')
tb.inject (Message (tb, 'start', True, None))
tb.run ()
print (tb.outputs ())
