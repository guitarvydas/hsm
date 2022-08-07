(defclass Brightness (HSM)
  ()
  (:default-initargs
   :states '(br-dim br-mid br-high)
   :default-state 'br-dim
   :sub-class 'Colour))

(defparameter br-dim
  (make-state
   :enter (lambda (self) (cond ((sub-class self) (setf (sub self) (make-instance (sub-class self)))) (t)))
   :exit (lambda (self) )
   :handle (lambda (self message)
             (cond ((string= "brightness" (port message))
                    (next self 'br-mid))
                   ((delegate 'Colour self message))
                   (t (unhandled-message self message))))))

(defparameter br-mid
  (make-state
    :enter (lambda (self) )
    :exit (lambda (self) )
    :handle (lambda (self message)
	      (cond ((string= "brightness" (port message))
		     (next self 'br-high))
		    ((delegate 'Colour self message))
		    (t (unhandled-message self message))))))

(defparameter br-high
  '(make-state
    :enter (lambda (self) )
    :exit (lambda (self) )
    :handle (lambda (self message)
	      (cond ((string= "brightness" (port message))
		     (next self 'br-dim))
		    ((delegate 'Colour self message))
		    (t (unhandled-message self message))))))

(defmethod initialize-instance :after ((self Brightness) &key &allow-other-keys)
  (enter-default self))
