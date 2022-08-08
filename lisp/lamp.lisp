(defparameter ls-off 
  (make-instance 'State
                 :name "off"
                 :enter (lambda (self) (declare (ignore self)))
                 :exit (lambda (self) (declare (ignore self)))
                 :handle (lambda (self message)
                           (cond ((string= "pwr" (port message))
                                  (next self ls-on))
                                 ((delegate self message) t)
                                 (t (unhandled-message self message))))))

(defparameter ls-on 
  (make-instance 'State
                 :name "on"
                 :enter (lambda (self) (declare (ignore self)))
                 :exit (lambda (self) (declare (ignore self)))
                 :handle (lambda (self message)
(let ((debug nil))
(format *standard-output* "ls-on begin debug~%")                                  
                           (cond ((string= "pwr" (port message))
                                  (next self ls-off))
                                 ((setf debug (delegate self message)) t)
                                 (t
(format *standard-output* "ls-on debug=~a~%" debug)                                  
                                  (unhandled-message self message)))))))

(defclass Lamp (HSM)
  ()
  (:default-initargs
   :states (list ls-off ls-on)
   :sub-machine-class 'Brightness
   :default-state ls-off))

(Defmethod initialize-instance :after ((self Lamp) &key &allow-other-keys)
  (enter-default self))

