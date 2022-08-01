from flask import Flask, render_template, request, redirect
from models import db, EmployeeModel

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///table.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.before_first_request
def create_table():
    db.create_all()

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('trying.html')

    if request.method == 'POST':
        name = request.form['name']
        place = request.form['place']
        email = request.form['email']
        employee = EmployeeModel( name=name, place=place, email = email)
        db.session.add(employee)
        db.session.commit()
        return redirect('/create')

@app.route('/data')
def RetrieveDataList():
    employees = EmployeeModel.query.all()
    return render_template('datalist.html',employees = employees)

@app.route('/data/<string:name>')
def RetrieveEmployee(name):
    employee = EmployeeModel.query.filter_by(name=name).first()
    if employee:
        return render_template('data.html', employee = employee)
    return f"Employee with name {name} Doesn't exist"

@app.route('/update')
def DeleteHome():
        return render_template('updatehome.html')

@app.route('/update/<string:name>', methods=['GET', 'POST'])
def update(name):
    employee = EmployeeModel.query.filter_by(name = name).first()
    if request.method == 'POST':
        if employee:
            db.session.delete(employee)
            db.session.commit()
            name = request.form['name']
            place = request.form['place']
            email = request.form['email']
            employee = EmployeeModel(name=name, place=place, email = email)
            db.session.add(employee)
            db.session.commit()
            return redirect(f'/data/{name}')
        return f"Employee with name  {name} Does not exist"

    return render_template('update.html', employee=employee)

@app.route('/delete')
def UpdateHome():
        return render_template('deletehome.html')


@app.route('/delete/<string:name>', methods=['GET', 'POST'])
def delete(name):
    employee = EmployeeModel.query.filter_by(name = name).first()
    if request.method == 'POST':
        if employee:
            db.session.delete(employee)
            db.session.commit()
            return redirect('/data')


    return render_template('delete.html')


app.run(host='localhost', port=5000)