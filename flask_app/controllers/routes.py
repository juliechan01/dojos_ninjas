from flask import Flask, render_template, request, redirect
from flask_app.models.dojos import Dojos
from flask_app.models.ninjas import Ninja
from flask_app import app

@app.route('/dojos/create', methods=['POST']) # ADDS A DOJO
def add_dojo():
    Dojos.save_dojo(request.form)
    return redirect('/dojos')

@app.route('/dojos') # DISPLAYS ALL DOJOS
def display_dojo():
    all_dojos = Dojos.get_all()
    print(all_dojos)
    return render_template("dojos.html", dojos=all_dojos)

@app.route('/dojos/<int:id>') # SHOWS ONE DOJO & ITS STUDENTS
def get_dojo(id):
    dojo = Dojos.ninjas_in_dojo(id)
    print(dojo)
    return render_template("one_dojo.html", dojo=dojo)

@app.route('/ninjas/new', methods=['POST']) # ADD A NINJA 
def new_ninja():
    Ninja.save_ninja(request.form)
    return redirect(f"/dojos/{request.form['dojos_id']}")

@app.route('/ninjas')
def get_ninja():
    return render_template("new_ninja.html")

@app.route('/ninjas/edit/<int:id>', methods=['POST']) # UPDATE A NINJA
def edit_ninja(id):
    data = {"id":id, "first_name":request.form['first_name'], "last_name":request.form['last_name'], "age":request.form['age']}
    Ninja.update(data)
    return redirect(f"/dojos/{request.form['dojos_id']}")

@app.route('/ninjas/get/<int:id>')
def update(id):
    ninja = Ninja.get_one(id)
    return render_template("edit_ninja.html", ninja=ninja)

@app.route('/ninjas/delete/<int:id>/<int:dojos_id>') # DELETE A NINJA
def delete(id, dojos_id):
    Ninja.delete(id)
    return redirect(f"/dojos/{dojos_id}")