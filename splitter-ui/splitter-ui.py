from flask import Flask, render_template, request
from forms import SequenceForm
from flask_wtf.csrf import CSRFProtect
from genetic_split.genetic_split import GeneticSplitter

APP = Flask(__name__)
APP.secret_key = 'splitrnotsosecretkey'
CSRF = CSRFProtect(APP)

@APP.route("/", methods=["GET"])
def index():
    '''
    Index page for splitter-ui
    '''
    form = SequenceForm()
    return render_template("index.html", form=form)


@APP.route("/split/", methods=["POST"])
def split_sequence():
    '''
    Split spaceless sequence using genetic-split algorithm.
    '''
    sequence = request.form['sequence']
    gs = GeneticSplitter(sequence)
    gs.evolve_population()
    solution = gs.solution
    return str(solution)

if __name__ == "__main__":
    APP.run()