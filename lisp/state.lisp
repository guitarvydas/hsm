(defclass State ()
  ((name :accessor name :initarg :name)
   (fenter :accessor fenter :initarg :enter)
   (fexit  :accessor fexit  :initarg :exit)
   (fhandle :accessor fhandle :initarg :handle)
   (sub-machine :accessor sub-machine :initform nil)
   (sub-machine-class :accessor sub-machine-class :initarg :sub-machine-class :initform nil)))

(defmethod enter ((self State))
  (when (sub-machine-class self)
    (setf (sub-machine self) (make-instance (sub-machine-class self) :parent self :name (sub-machine-class self))))
  (funcall (fenter self) self))

(defmethod exit ((self State))
  (funcall (fexit self) self))

(defmethod handle ((self State) message)
  (funcall (fhandle self) self message))

  
					    
