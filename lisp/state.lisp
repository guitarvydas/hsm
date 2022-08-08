(defclass State ()
  ((name :accessor name :initarg :name)
   (enter :accessor enter :initarg :enter)
   (exit  :accessor exit  :initarg :exit)
   (fhandle :accessor fhandle :initarg :handle)
   (sub :accessor sub :initarg :sub)))
  
