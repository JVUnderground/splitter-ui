from flask import Flask, render_template
from forms import SequenceForm
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.secret_key = 'brunaisanidiot'
csrf = CSRFProtect(app)

@app.route("/", methods=["GET"])
def index():
    '''
    Index page for splitter-ui
    '''
    form = SequenceForm()
    return render_template("index.html", form=form)

if __name__ == "__main__":
    app.run()

@app.route("/split/", methods=["GET", "POST"])
def split_sequence():
    '''
    Split spaceless sequence using genetic-split algorithm.
    '''
    
    return ""
