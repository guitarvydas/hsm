(defclass Lamp (HSM)
  :states '(ls-off ls-on)
  :default-state 'ls-off)

(defparameter ls-off 
  '(make-state
    :enter (lambda (self) )
    :exit (lambda (self) )
    :handle (lambda (self message)
	      (cond ((string= "pwr" (port message))
		     (next self 'ls-on))
		    (t (unhandled-message self message))))))

(defparameter ls-on 
  '(make-state
    :enter (lambda (self) )
    :exit (lambda (self) )
    :handle (lambda (self message)
	      (cond ((string= "pwr" (port message))
		     (next self 'ls-off))
		    ((delegate 'Brightness self message))
		    (t (unhandled-message self message))))))

(defmethod initialize-instance :after ((self Lamp) parent instance-name)
  (enter-default self))
