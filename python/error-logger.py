LOG_FORMATTER = "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s"
LOG_FILENAME = 'error.log'
LOG_FILE_SIZE = 10000000    # Rotate log file at 10MB

if __name__ == '__main__':
	formatter = logging.Formatter(LOG_FORMATTER)
	handler = RotatingFileHandler(LOG_FILENAME, maxBytes=LOG_FILE_SIZE, backupCount=10)
	handler.setLevel(logging.DEBUG)
	handler.setFormatter(formatter)
	app.logger.addHandler(handler)
	app.run('0.0.0.0')
