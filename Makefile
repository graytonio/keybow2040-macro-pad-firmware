
upload_path := /media/${USER}/CIRCUITPY

upload: upload-lib upload-code

upload-lib:
	@echo "Uploading Libraries to ${upload_path}/lib"
	cp -r lib/ ${upload_path}/lib

upload-code:
	@echo "Uploading Code files to ${upload_path}"
	cp *.py ${upload_path}

upload-config:
	@echo "Uploading Config file to ${upload_path}"
	cp config.py ${upload_path}