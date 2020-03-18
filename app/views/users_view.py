from app import app
from app import db
from app.forms import delete
from app.forms import signup
from app.models import user
from flask import redirect
from flask import render_template


@app.route("/users")
def index():
    users = user.User.query.all()
    return render_template("users/index.html", users=users)


@app.route("/users/new", methods=["GET", "POST"])
def new():
    signup_form = signup.SignupForm()
    if signup_form.validate_on_submit():
        email = signup_form.email.data
        searchAt = email.split("@")
        if len(searchAt[0]) > 0:
            if len(searchAt) == 2:
                if len(searchAt[1]) > 0:
                    searchDot = searchAt[1].split(".")
                    if len(searchDot) > 0:
                        if len(searchDot[len(searchDot) - 1]) > 0:
                            new_user = user.User(
                                first_name=signup_form.first_name.data,
                                last_name=signup_form.last_name.data,
                                email=signup_form.email.data,
                                password=signup_form.password.data
                            )
                            db.session.add(new_user)
                            db.session.commit()
                            return redirect("/users")
        return render_template("users/problem.html", warning="Email is invalid.")
    return render_template("users/new.html", form=signup_form)


@app.route("/users/del", methods=["GET", "POST"])
def remove_user():
    delete_form = delete.DeleteForm()
    if delete_form.validate_on_submit():
        if user.User.query.filter_by(email=delete_form.email.data).first():
            if delete_form.password.data == user.User.query.filter_by(email=delete_form.email.data).first().password:
                delete_this = user.User.query.filter_by(email=delete_form.email.data).all()[0]
                db.session.delete(delete_this)
                db.session.commit()
                return redirect("/users")
            else:
                return render_template("users/problem.html", warning="Invalid password.")
        else:
            return render_template("users/problem.html", warning="Invalid email.")
    return render_template("users/delete.html", form=delete_form)
