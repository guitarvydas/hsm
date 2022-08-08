(defclass FIFO ()
  ((lis :accessor lis :initform nil)))

(defmethod len ((self FIFO))
  (length (lis self)))

(defmethod is-empty ((self FIFO))
  (zerop (len self)))

(defmethod enqueue ((self FIFO) item)
  (push item (lis self)))

(defmethod dequeue ((self FIFO))
  ;; optimize later
  (let ((item (first (last (lis self)))))
    (setf (lis self) (butlast (lis self)))
    item))
