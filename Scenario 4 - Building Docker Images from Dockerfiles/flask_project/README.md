This is an example project showing how an existing Flask web application can be turned from a standalone
app into a containerized application that can be run in Docker

# Flask Application Requirements

* Python 3.10
* Flask 3.1.0
* gunicorn 23.0.0

# To run Web Application:

Gunicorn configuration inside of gunicorn_config.py

Default port for gunicorn web server: 8000

```bash
gunicorn -c gunicorn_config.py
```

To access webpage, open up web browser and navigate to: [http://localhost:8000](http://localhost:8000)

