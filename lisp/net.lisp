(defclass Net ()
  ((name :accessor name :initarg :name)
   (receivers :accessor receivers :initarg :receivers)))

(defmethod receiverList ((self Net))
  (receivers self))
