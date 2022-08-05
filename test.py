from simpletestbench import SimpleTestBench
from message import Message

tb = SimpleTestBench (None, 'simple.test.bench')
tb.inject (Message (tb, 'start', True, None))
tb.run ()
print (tb.outputs ())
