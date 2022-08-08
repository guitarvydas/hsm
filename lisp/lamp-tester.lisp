(defparameter lt-default
  (make-instance 'State
                 :name "default"
		 :enter (lambda (self) (declare (ignore self)))
		 :exit (lambda (self) (declare (ignore self)))
		 :handle (lambda (self message)
			   (cond ((string= "start" (port message))
				  (send self "pwr" t nil)
				  (send self "brightness" t nil)
				  (send self "colour" t nil))
				 (t (unhandled-message self message))))))


(defclass Lamp-Tester (HSM)
  ()
  (:default-initargs
   :states (list lt-default)
   :default-state lt-default))

(defmethod initialize-instance :after ((self Lamp-Tester) &key &allow-other-keys)
  (enter-default self))

