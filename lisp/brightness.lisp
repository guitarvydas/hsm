(defparameter br-dim
  (make-instance 'State
                 :name "dim"
                 :enter (lambda (self) (send self "state" "DIM" nil))
                 :exit (lambda (self) (send self "state" "x-DIM" nil))
                 :handle (lambda (self message)
                           (cond ((string= "brightness" (port message))
                                  (next self br-mid))
                                 ((delegate self message) t)
                                 (t (unhandled-message self message))))))

(defparameter br-mid
  (make-instance 'State
                 :name "mid"
                 :enter (lambda (self) (send self "state" "MID" nil))
                 :exit (lambda (self) (send self "state" "x-MID" nil))
                 :handle (lambda (self message)
                           (cond ((string= "brightness" (port message))
                                  (next self br-high))
                                 ((delegate self message) t)
                                 (t (unhandled-message self message))))))

(defparameter br-high
  (make-instance 'State
                 :name "high"
                 :enter (lambda (self) (send self "state" "HIGH" nil))
                 :exit (lambda (self) (send self "state" "x-HIGH" nil))
                 :handle (lambda (self message)
                           (cond ((string= "brightness" (port message))
                                  (next self br-dim))
                                 ((delegate self message) t)
                                 (t (unhandled-message self message))))))


(defclass Brightness (SubHSM)
  ()
  (:default-initargs
   :states (list br-dim br-mid br-high)
   :default-state br-dim
   :sub-machine-class 'Colour))

(defmethod initialize-instance :after ((self Brightness) &key &allow-other-keys)
  (enter-default self))
