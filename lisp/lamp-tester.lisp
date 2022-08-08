(defclass Lamp-Tester (HSM)
  ()
  (:default-initargs
   :states '(("default" . lt-default))
   :default-state lt-default))

(defparameter lt-default
  (make-instance 'State
		 :enter (lambda (self) (declare (ignore self)))
		 :exit (lambda (self) (declare (ignore self)))
		 :handle (lambda (self message)
			   (cond ((string= "start" (port message))
				  (send self "pwr" t nil)
				  (send self "brightness" t nil)
				  (send self "colour" t nil))
				 (t (unhandled-message self message))))))

