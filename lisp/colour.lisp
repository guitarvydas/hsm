(defclass Colour (HSM)
  :states '(br-dim br-mid br-high)
  :default-state 'br-dim)

(defparameter br-dim
  '(make-state
    :enter (lambda (self) )
    :exit (lambda (self) )
    :handle (lambda (self message)
	      (cond ((string= "colour" (port message))
		     (next self 'br-mid))
		    ((delegate 'Colour self message))
		    (t (unhandled-message self message))))))

(defparameter br-mid
  '(make-state
    :enter (lambda (self) )
    :exit (lambda (self) )
    :handle (lambda (self message)
	      (cond ((string= "colour" (port message))
		     (next self 'br-high))
		    ((delegate 'Colour self message))
		    (t (unhandled-message self message))))))

(defparameter br-high
  '(make-state
    :enter (lambda (self) )
    :exit (lambda (self) )
    :handle (lambda (self message)
	      (cond ((string= "colour" (port message))
		     (next self 'br-dim))
		    ((delegate 'Colour self message))
		    (t (unhandled-message self message))))))

(defmethod initialize-instance :after ((self Colour) parent instance-name)
  (enter-default self))
