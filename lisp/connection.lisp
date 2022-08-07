(defclass Connection ()
  ((instance :accessor instance :initarg :instance)
   (port :accessor port :initarg :port)
   (net :accessor net :initarg :net)))

(defmethod has-sender ((self Connection) instance port-name)
  (and (eq (instance self) instance)
       (eq (port self) port-name)))
