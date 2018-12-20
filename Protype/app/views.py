from flask import render_template, flash, redirect, session, url_for, request, g
from flask_admin.contrib.sqla import ModelView
from flask_wtf.csrf import CsrfProtect
 

from app import app, db, admin
from .models import TestModel
from .forms import TestModelForm

admin.add_view(ModelView(TestModel, db.session))



@app.route('/create_TestModel', methods=['GET','POST'])
def create_item():
    form = TestModelForm()
    flash('Errors="%s"' %
          (form.errors))
    if request.method == 'POST' and form.validate():
      t = TestModel(title=form.title.data,content=form.content.data, date=form.date.data)
      db.session.add(t)
      db.session.commit()
      #flash('Thanks for registering')
      return redirect('/')
    '''if form.validate_on_submit():
        t = TestModel(title=form.title.data,content=form.content.data, date=form.date.data)
        db.session.add(t)
        db.session.commit()
        return redirect('/')'''

    return render_template('create_item.html',
                           title='Create TestModel',
                           form=form)

@app.route('/', methods=['GET'])
def get_list():
    TestModel = TestModel.query.order_by('Date').all()
    return render_template('form_view.html',
                           title='All TestModel',
                           TestModel=TestModel)

@app.route('/form_view_yes', methods=['GET'])
def get_list_True():
    TestModel = TestModel.query.order_by('Date').filter(TestModel.status==True).all()
    return render_template('form_view.html',
                           title='Complete TestModel',
                           TestModel=TestModel)

@app.route('/form_view_no', methods=['GET'])
def get_list_False():
    TestModel = TestModel.query.order_by('Date').filter(TestModel.status==False).all()
    return render_template('form_view.html',
                           title='Uncomplete TestModel',
                           TestModel=TestModel)


@app.route('/delete_TestModel/<id>', methods=['GET'])
def delete_TestModel(id):
    TestModel = TestModel.query.get(id)
    db.session.delete(TestModel)
    db.session.commit()
    return redirect('/')

@app.route('/complete_TestModel/<id>', methods=['GET'])
def complete_TestModel(id):
    TestModel = TestModel.query.get(id)
    TestModel.status=True
    db.session.commit()
    return redirect('/')

#csrf保护
CsrfProtect(app)
