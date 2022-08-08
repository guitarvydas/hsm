(defclass HSM (Leaf)
  ((states :accessor states :initarg :states)
   (state :accessor state)
   (default-state :accessor default-state :initarg :default-state)
   (sub-machine :accessor sub-machine :initform nil)
   (sub-machine-class :accessor sub-machine-class :initarg :sub-machine-class :initform nil)))

(defmethod lookup-state ((self HSM) state-name)
  (lookup-state-helper (states self) state-name))

(defun lookup-state-helper (state-list state-name)
  (if (null state-list)
      nil
    (if (string= state-name (name (first state-list)))
        (first state-list)
      (lookup-state-helper (rest state-list) state-name))))

(defmethod enter ((self HSM))
  (cond ((sub-machine-class self)
         (setf (sub-machine self) (make-instance (sub-machine-class self))))
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
  (cond ((sub-machine self) (funcall (sub-machine self) message))
        (t)))

(defmethod maybe-create-sub-machines ((self HSM))
  (cond ((sub-machine-class self)
         (setf (sub-machine self) (make-instance (sub-machine-class self))))
        (t)))

(defclass SubHSM (HSM) ())

(defmethod send ((self SubHSM) portname data causing-message)
  (let ((sender (parent self)))
    (send sender portname data causing-message)))
    
