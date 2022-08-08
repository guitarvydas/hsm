(defclass HSM (Leaf)
  ((states :accessor states :initarg :states)
   (state :accessor state)
   (default-state :accessor default-state :initarg :default-state)
   (sub-machine :accessor sub-machine :initform nil)
   (sub-machine-class :accessor sub-machine-class :initarg :sub-machine-class :initform nil)))

(defmethod enter ((self HSM))
  (cond ((sub-class self)
         (setf (sub self) (make-instance (sub-class self))))
        (t))
  (funcall (enter (state self)) self))

(defmethod exit ((self HSM))
  (funcall (exit (state self)) self))

(defmethod handle ((self HSM) message)
  (funcall (fhandle (state self)) self message))

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

(defmethod delegate ((self HSM) message)
  (cond ((sub self) (funcall (sub self) message))
        (t)))

(defmethod maybe-create-sub-machines ((self HSM))
  (cond ((sub-machine-class self)
         (setf (sub-machine self) (make-instance (sub-machine-class self))))
        (t)))

(defclass SubHSM (HSM) ())

(defmethod send ((self SubHSM) portname data causing-message)
  (let ((sender (parent self)))
    (send sender portname data causing-message)))
    
