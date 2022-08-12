(defclass Net ()
  ((name :accessor name :initarg :name)
   (receivers :accessor receivers :initarg :receivers)))

(defmethod receiver-list ((self Net))
  (receivers self))
