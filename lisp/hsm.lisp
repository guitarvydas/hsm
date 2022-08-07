(defclass HSM (Leaf)
  ((states :accessor states :initarg :states)
   (state :accessor state)
   (default-state :accessor states :initarg :default-state)))

(defmethod enter ((self HSM))
  (funcall (enter (state self) self)))

(defmethod exit ((self HSM))
  (funcall (exit (state self)) self))

(defmethod handle ((self HSM) message)
  (funcall (handle (state self)) self message))

(defmethod enter-default ((self HSM))
  (setf (state self) (default-state self))
  (enter self))

(defmethod next ((self HSM) next-state)
  (exit self)
  (setf (state self) next-state)
  (enter self))

(defmethod reset ((self HSM))
  (exit self)
  (enter-default self))


(defclass SubHSM (HSM))

(defmethod send ((self SubHSM) sub-instance portname data causing-message)
  (let ((sender (parent sub-instance)))
    (send sender portname data causing-message)))
    
