# splitter-ui
Web interface to genetic-split algorithm.

# Install
```
virtualenv env
source env/bin/activate
pip install -i requirements.txt
```

# Run
```
gunicorn --worker-class eventlet -w 1 splitr:APP
```