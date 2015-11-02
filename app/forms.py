from flask.ext.wtf import Form
from wtforms import StringField, RadioField
from wtforms.validators import DataRequired

class SearchForm(Form):
    search = StringField('search', validators = [DataRequired()])
    #radio = RadioField('radio', validators = [DataRequired()], choices = [
    #                ('KMeans', 'K-Means'), ('Ward', 'Ward'), ('FCA', 'FCA'),
    #                ('STC', 'STC')])