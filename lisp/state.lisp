(defclass State ()
  ((enter :accessor enter :initarg :enter)
   (exit  :accessor exit  :initarg :exit)
   (fhandle :accessor fhandle :initarg :handle)
   (sub :accessor sub :initarg :sub)))
  
