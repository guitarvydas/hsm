(defclass State ()
  (enter :accessor enter :initarg :enter)
  (exit  :accessor exit  :initarg :exit)
  (handle :accessor handle :initarg :handle))
