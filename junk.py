from fifo import FIFO

fifo = FIFO ()
fifo.enqueue ('a')
fifo.enqueue ('b')
print (fifo._elements)
for v in fifo.asList ():
    print (v)
