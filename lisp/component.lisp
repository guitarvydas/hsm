(defclass Component ()
  ((parent :accessor parent :initarg :parent)
   (instance-name :accessor instance-name :initarg :name)
   (inputq :accessor inputq :initform (make-instance 'FIFO))
   (outputq :accessor outputq :initform (make-instance 'FIFO))))

(defgeneric run (self))
(defgeneric step1 (self))
(defgeneric reset (self))
(defgeneric is-busy (self))

(defmethod inject ((self Component) message)
  (enqueue (inputq self) message))

(defmethod outputs ((self Component))
  (as-list (outputq self)))

(defmethod is-ready ((self Component))
  (> (len (inputq self)) 0))

(defmethod name ((self Component))
  (cond ((null (parent self))
	 (instance-name self))
	(t (format nil "~a/~a" (name (parent self)) (instance-name self)))))

;; internal
(defmethod enqueue-input ((self Component) message)
  (enqueue (inputq self) message))

(defmethod enqueue-output ((self Component) message)
  (enqueue (outputq self) message))

(defmethod dequeue-input ((self Component))
  (dequeue (inputq self)))

(defmethod send ((self Component) portname data causing-message)
  (let ((trail (cond ((null causing-message) nil)
		     (t (cons causing-message (trail causing-message))))))
    (let ((m (make-instance 'Message :sender self :port portname :data data :trail trail)))
      (update-state m "output")
      (enqueue (outputq self) m))))

(defmethod unhandled-message ((self Component) message)
  (error (format nil "unhandled message in ~a[~a] ~a" (name self) (name (state self)) (port message))))

(defmethod output-queue ((self Component))
  (outputq self))

(defmethod clear-outputs ((self Component))
  (setf (outputq self) (make-instance 'FIFO)))
