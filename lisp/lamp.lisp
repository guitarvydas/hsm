(defparameter ls-off 
  (make-instance 'State
                 :enter (lambda (self) (maybe-create-sub-machines self))
                 :exit (lambda (self) (declare (ignore self)))
                 :handle (lambda (self message)
                           (cond ((string= "pwr" (port message))
                                  (next self 'ls-on))
                                 (t (unhandled-message self message))))))

(defparameter ls-on 
  (make-instance 'State
                 :enter (lambda (self) (maybe-create-sub-machines self))
                 :exit (lambda (self) (declare (ignore self)))
                 :handle (lambda (self message)
                           (cond ((string= "pwr" (port message))
                                  (next self 'ls-off))
                                 ((delegate self message))
                                 (t (unhandled-message self message))))))

(defclass Lamp (HSM)
  ()
  (:default-initargs
   :states `(("off" . ,ls-off) ("on" . ,ls-on))
   :sub-machine-class 'Brightness
   :default-state ls-off))

(Defmethod initialize-instance :after ((self Lamp) &key &allow-other-keys)
  (enter-default self))

