(let* (
       (exit_OFF (lambda (e) ))
       (enter_OFF (lambda (e) (f1exit e)))
       (handle_OFF (lambda (e message)
		     (cond ((eq (port message) "pwr")
			    ((next (comp self)) e "ON"))
