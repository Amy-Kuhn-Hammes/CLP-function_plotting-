VENV := venv


install:
	python3 -m venv $(VENV)
	. $(VENV)/bin/activate && pip install flask flask-cors matplotlib numpy

run:
	. $(VENV)/bin/activate && python app.py

#Caso de estudo
study:
	@echo "Iniciando servidor" 
	. $(VENV)/bin/activate && python app.py &
	sleep 2
	@echo "Abrindo página"
	xdg-open index.html || open index.html || start index.html

clean:
	rm -rf $(VENV) __pycache__ *.pyc
