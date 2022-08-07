(defclass Leaf (Component))

(defmethod is-busy ((self Leaf))
  nil)

(defmethod step ((self Leaf))
  (cond ((is-ready self)
	 (let ((m (dequeue-input self)))
	   (handle self m)
	   t))
	(t nil)))

(defmethod run ((self Leaf))
  (cond ((not (is-ready self)) (return-from run))
	(t (step self) (run self))))
