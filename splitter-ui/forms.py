from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class SequenceForm(Form):
    '''
    Basic string form that accepts a spaceless sequence of characters

    NEEDS WORK (validating that it is in fact spaceless and no punctuation)
    '''
    sequence = StringField('Sequence', validators=[DataRequired()])

    