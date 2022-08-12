(defparameter clr-yellow
  (make-instance 'State
                 :name "yellow"
                 :enter (lambda (self) #+nil(send self "state" "YELLOW" nil))
                 :exit (lambda (self) #+nil(send self "state" "x-YELLOW" nil))
                 :handle (lambda (self message)
                           (cond ((string= "colour" (port message))
                                  (next self clr-green))
                                 ((delegate self message) t)
                                 (t (unhandled-message self message))))))

(defparameter clr-green
  (make-instance 'State
                 :name "green"
                 :enter (lambda (self) #+nil(send self "state" "GREEN" nil))
                 :exit (lambda (self) #+nil(send self "state" "x-GREEN" nil))
                 :enter (lambda (self) (declare (ignore self)))
                 :exit (lambda (self) (declare (ignore self)))
                 :handle (lambda (self message)
                           (cond ((string= "colour" (port message))
                                  (next self clr-red))
                                 ((delegate self message) t)
                                 (t (unhandled-message self message))))))

(defparameter clr-red
  (make-instance 'State
                 :name "red"
                 :enter (lambda (self) #+nil(send self "state" "RED" nil))
                 :exit (lambda (self) #+nil(send self "state" "x-RED" nil))
                 :handle (lambda (self message)
                           (cond ((string= "colour" (port message))
                                  (next self clr-yellow))
                                 ((delegate self message) t)
                                 (t (unhandled-message self message))))))

(defclass Colour (SubHSM)
  ()
  (:default-initargs
   :states (list clr-yellow clr-green clr-red)
   :default-state clr-yellow))

(defmethod initialize-instance :after ((self Colour)  &key &allow-other-keys)
  (enter-default self))
