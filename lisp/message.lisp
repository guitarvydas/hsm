(defclass BaseMessage ()
  ((data :accessor data)))

(defmethod initialize-instance :after ((self BaseMessage) datum)
  (setf (data self) datum))

(defmethod value ((self BaseMessage))
  (data self))


(defclass Message (BaseMessage)
  ((sender :accessor sender)
   (port :accessor port)
   (trail :accessor trail)
   (state :accessor state)))

(defmethod initialize-instance :after ((self Message) sender port datum trail)
  (setf (sender self) sender)
  (setf (port self) port)
  (setf (data self) datum)
  (setf (trail self) trail)
  (setf (state self) "?")

(defmethod update-state ((self Message) new-state)
  (setf (state self) new-state))
