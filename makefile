PY=python3
MAIN=main
DIR=$(PWD)
.SUFFIXES: .py
FILES = \
	task.py\
   
All: 
	echo " $(PY) $(DIR)/$(FILES) " \"'$$1'\" > while
	chmod +x while
    
clean:
	rm -f while
	rm -rf __pycache__
