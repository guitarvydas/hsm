(defclass BaseMessage ()
  ((data :accessor data :initarg :data)))

(defmethod value ((self BaseMessage))
  (data self))


(defclass Message (BaseMessage)
  ((sender :accessor sender :initarg :sender)
   (port :accessor port :initarg :port)
   (trail :accessor trail :initarg :trail :initform nil)
   (state :accessor state :initform "?")))

(defmethod update-state ((self Message) new-state)
  (setf (state self) new-state))

(defmethod print-object ((self Message) stream)
  (format stream "<~a: ~a>" (port self) (data self)))