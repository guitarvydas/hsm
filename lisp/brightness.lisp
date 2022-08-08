(defparameter br-dim
  (make-instance 'State
                 :enter (lambda (self) (maybe-create-sub-machines self))
                 :exit (lambda (self) (declare (ignore self)))
                 :handle (lambda (self message)
                           (cond ((string= "brightness" (port message))
                                  (next self 'br-mid))
                                 ((delegate self message))
                                 (t (unhandled-message self message))))))

(defparameter br-mid
  (make-instance 'State
                 :enter (lambda (self) (maybe-create-sub-machines self))
                 :exit (lambda (self) (declare (ignore self)))
                 :handle (lambda (self message)
                           (cond ((string= "brightness" (port message))
                                  (next self 'br-high))
                                 ((delegate self message))
                                 (t (unhandled-message self message))))))

(defparameter br-high
  (make-instance 'State
                 :enter (lambda (self) (maybe-create-sub-machines self))
                 :exit (lambda (self) (declare (ignore self)))
                 :handle (lambda (self message)
                           (cond ((string= "brightness" (port message))
                                  (next self 'br-dim))
                                 ((delegate self message))
                                 (t (unhandled-message self message))))))


(defclass Brightness (HSM)
  ()
  (:default-initargs
   :states '(("dim" . br-dim) ("mid" . br-mid) ("high" .  br-high))
   :default-state br-dim
   :sub-machine-class 'Colour))

(defmethod initialize-instance :after ((self Brightness) &key &allow-other-keys)
  (enter-default self))
