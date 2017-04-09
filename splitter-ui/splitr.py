import time
from flask import Flask, render_template, request
from forms import SequenceForm
from flask_wtf.csrf import CSRFProtect
from flask_socketio import SocketIO, emit

from genetic_split.genetic_split import GeneticSplitter

APP = Flask(__name__)
APP.secret_key = 'splitrnotsosecretkey'
SOCKETIO = SocketIO(APP)
CSRF = CSRFProtect(APP)
SPLITTER = None

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
    global SPLITTER
    sequence = request.form['sequence']
    SPLITTER = GeneticSplitter(sequence)
    SPLITTER.evolve_population(50)
    solution = SPLITTER.solution
    return str(solution)

@SOCKETIO.on('initialize')
def initialize_splitter(sequence):
    global SPLITTER
    SPLITTER = GeneticSplitter(sequence)
    emit('splitter-ready')
    print "Population Initialized"

@SOCKETIO.on('split')
def split():
    SPLITTER.evolve_population(15)
    solution = SPLITTER.solution
    time.sleep(0.5)

    if SPLITTER.stopped:
        emit('split-ended', str(solution))
        print "Split sequence ended"
    else:
        emit('split-sequence', str(solution))
        print "New split sequence emitted"


if __name__ == "__main__":
    SOCKETIO.run(APP)
