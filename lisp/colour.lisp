(defclass Colour (HSM)
  ()
  (:default-initargs
   :states '(clr-yellow clr-green clr-red)
   :default-state 'br-dim))

(defparameter cl-yellow
  '(make-state
    :enter (lambda (self) )
    :exit (lambda (self) )
    :handle (lambda (self message)
	      (cond ((string= "colour" (port message))
		     (next self 'br-mid))
		    ((delegate 'Colour self message))
		    (t (unhandled-message self message))))))

(defparameter clr-green
  '(make-state
    :enter (lambda (self) )
    :exit (lambda (self) )
    :handle (lambda (self message)
	      (cond ((string= "colour" (port message))
		     (next self 'br-high))
		    ((delegate 'Colour self message))
		    (t (unhandled-message self message))))))

(defparameter clr-red
  '(make-state
    :enter (lambda (self) )
    :exit (lambda (self) )
    :handle (lambda (self message)
	      (cond ((string= "colour" (port message))
		     (next self 'br-dim))
		    ((delegate 'Colour self message))
		    (t (unhandled-message self message))))))

(defmethod initialize-instance :after ((self Colour)  &key &allow-other-keys)
  (enter-default self))
