(proclaim '(optimize (debug 3) (safety 3) (speed 0)))
	  
(Defparameter *root* (format nil "~aquicklisp/local-projects/hsm/lisp/" (cd)))

(defun rooted (s)
  (format nil "~a~a" *root* s))

(load (rooted "state.lisp"))
(load (rooted "connection.lisp"))
(load (rooted "net.lisp"))
(load (rooted "message.lisp"))
(load (rooted "fifo.lisp"))
(load (rooted "component.lisp"))
(load (rooted "leaf.lisp"))
(load (rooted "hsm.lisp"))
(load (rooted "container.lisp"))

(load (rooted "lamp.lisp"))
(load (rooted "brightness.lisp"))
(load (rooted "colour.lisp"))

(load (rooted "lamp-tester.lisp"))
(load (rooted "testbench.lisp"))
(load (rooted "test.lisp"))
