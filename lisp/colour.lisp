(defparameter clr-yellow
  (make-instance 'State
                 :enter (lambda (self) (maybe-create-sub-machines self))
                 :exit (lambda (self) (declare (ignore self)))
                 :handle (lambda (self message)
                           (cond ((string= "colour" (port message))
                                  (next self 'br-mid))
                                 ((delegate self message))
                                 (t (unhandled-message self message))))))

(defparameter clr-green
  (make-instance 'State
                 :enter (lambda (self) (maybe-create-sub-machines self))
                 :exit (lambda (self) (declare (ignore self)))
                 :handle (lambda (self message)
                           (cond ((string= "colour" (port message))
                                  (next self 'br-high))
                                 ((delegate 'self message))
                                 (t (unhandled-message self message))))))

(defparameter clr-red
  (make-instance 'State
                 :enter (lambda (self) (maybe-create-sub-machines self))
                 :exit (lambda (self) (declare (ignore self)))
                 :handle (lambda (self message)
                           (cond ((string= "colour" (port message))
                                  (next self 'br-dim))
                                 ((delegate self message))
                                 (t (unhandled-message self message))))))

(defclass Colour (HSM)
  ()
  (:default-initargs
   :states '(("yellow" . clr-yellow) ("green" . clr-green) ("red" .  clr-red))
   :default-state clr-yellow))

(defmethod initialize-instance :after ((self Colour)  &key &allow-other-keys)
  (enter-default self))
