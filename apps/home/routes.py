# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from platform import machine
import string
from this import d
from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound


@blueprint.route('/index')
@login_required
def index():

    return render_template('home/index.html', segment='index')


@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
messages = []
nameOfMachine = []
numberOfMachine = []
EnergySim = []
use = []
levelCapacity = []
energyConsumption = []
date = []


@blueprint.route('/fetch/', methods=['GET', 'POST'])
def fetch():
    
    filterValue = request.form['search']
    table = filterValue.split(',')
    nameOfMachine.append(table[0])
    numberOfMachine.append(table[1])
    EnergySim.append(table[2])
    use.append(table[3])
    levelCapacity.append(table[4])
    energyConsumption.append(table[5])
    date.append(table[6])
    number = len(messages)
    consumption = 0
    cost = 0
    i =0
    coefficient = 217
    unit = ''
    unit_price = ''
    stringCons = ''
    cost_str = ''
    for i in range(number):
        if EnergySim[i] == 'E':
            unit = 'MW'
        consumption = consumption + int(numberOfMachine[i])*(int(use[i])*int(levelCapacity[i])*int(energyConsumption[i]))
        stringCons = str(consumption) + unit
        cost = cost + consumption * coefficient
        cost_str = ' '+str(cost) + "$"
    messages.append(table[0])
    i = i+1
    val = 1
    return render_template('home/author.html', consommation = stringCons,cout = cost_str, j = i,boo = val)

@blueprint.route('/fetch2/', methods=['GET', 'POST'])
def fetch2():
    value = 1
    stringCons = '3,75MW'
    cost_str = ' 590$'
    return render_template('home/author.html',boolean = value,conso = stringCons,prix = cost_str)





