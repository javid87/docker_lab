# The application to run (python module name:app name)
# The module name is flask_website.py
# The app name is app, which is the name of the Flask() object inside the flask_website.py file.
wsgi_app = "flask_website:app"

# The host and port to bind to. Bind to all interfaces on port 8000.
bind = "0.0.0.0:8000"

# Number of worker processes (default is 1, adjust as needed)
workers = 1

# Log level (e.g., debug, info, warning, error, critical)
loglevel = "debug"

# Optional: Timeout for workers
timeout = 30