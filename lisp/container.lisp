(defclass Container (HSM)
  ((children :accessor children)
   (nets :accessor nets)
   (connections :accessor connections)))
  

(defmethod step1 ((self Container))
  (let ((work-done (step-any-child self)))
    (cond (work-done t)
	  ((is-ready self)
	   (let ((m (dequeue-input self)))
	     (handle self m)
	     t))
	  (t nil))))

(defmethod run ((self Container))
  (cond ((is-ready self)
	 (let ((m (dequeue-input self)))
	   (handle self m)))
	(t))
  (let ((work-done (step-any-child self)))
    (loop while work-done
          do (setf work-done (step-any-child self)))))

(defmethod is-busy ((self Container))
  (mapc #'(lambda (child)
	    (cond ((is-busy child) (return-from is-busy t))
		  (t)))
	(children self)))

(defmethod reset ((self Container))
  (mapc #'(lambda (child)
	    (reset child))
	(children self)))

;; internal
(defmethod handle ((self Container) message)
  (let ((net (find-net self self (port message))))
    (route self message net)))

(defmethod step-any-child ((self Container))
    (mapc #'(lambda (child)
              (let ((child-acted (step1 child)))
                (if child-acted
                    (progn
                      (route-child-outputs self child)
                      (return-from step-any-child t)))))
	  (children self)))

(defmethod enter ((self Container))
  (setf (state self) (lookup-state self "default")))

(defmethod noop ((self Container))
  )

(defmethod find-net ((self Container) instance port-name)
  (mapc #'(lambda (connection)
	    (cond ((has-sender connection instance port-name)
		   (return-from find-net (net connection)))
		  (t)))
	(connections self))
  (error (format nil "internal error: no connection for ~a/~a" (name instance) port-name)))


(defmethod route ((self Container) message net)
  (cond (net
	 (let ((receiver-list (receiver-list net)))
	   (mapc #'(lambda (receiver-tuple)
		     (let ((receiver (first receiver-tuple))
			   (port (second receiver-tuple)))
		       (let ((m (make-instance 'Message :sender (sender message) :port port :data (value message) :trail (trail message))))
			 (cond ((eq receiver self)
				(update-state m "output")
				(enqueue-output receiver m))
			       (t
				(update-state m "input")
				(enqueue-input receiver m))))))
		 receiver-list)))
	(t)))

(defmethod route-child-outputs ((self Container) child)
  (let ((outputs (outputs child)))
    (clear-outputs child)
    (mapc #'(lambda (message)
	      (let ((net (find-net self child (port message))))
		(route self message net)))
	  outputs)))

(defmethod initialize-container-default ((self Container))
  (let ((default (make-instance 'State :name "default" :enter #'noop :exit #'noop :handle #'handle :sub nil)))
    (setf (states self) (list default))
    (setf (default-state self) default)
    (setf (state self) default)
    (enter self)))

(defmethod initialize-instance :after ((self Container) &key &allow-other-keys)
  (initialize-container-default self))
