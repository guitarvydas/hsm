(defclass Lamp (HSM)
  ()
  (:default-initargs
   :states '(("off" . ls-off) ("on" . ls-on))
   :sub (make-instance 'Brightness)
   :default-state 'ls-off))

(defparameter ls-off 
  (make-instance 'State
                 :enter (lambda (self) (declare (ignore self)))
                 :exit (lambda (self) (declare (ignore self)))
                 :handle (lambda (self message)
                           (cond ((string= "pwr" (port message))
                                  (next self 'ls-on))
                                 (t (unhandled-message self message))))))

(defparameter ls-on 
  (make-instance 'State
                 :enter (lambda (self) (declare (ignore self)))
                 :exit (lambda (self) (declare (ignore self)))
                 :handle (lambda (self message)
                           (cond ((string= "pwr" (port message))
                                  (next self 'ls-off))
                                 ((delegate self message))
                                 (t (unhandled-message self message))))))

(defmethod initialize-instance :after ((self Lamp) &key &allow-other-keys)
  (call-next-method))
