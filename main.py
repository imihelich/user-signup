from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/register", methods=['POST'])
def register():

    user = request.form['username']
    email = ""
    email = request.form['email']
    pw = request.form['password']
    ver_pw = request.form['verpassword']

    if not user and not pw and not ver_pw:
        return redirect ("/?error=" + "you left the page blank")

    if pw != ver_pw: 
        return redirect ("/?error=" + "password and password verification fields must match" + "&user=" + user + "&em=" + email)

    if len(pw) < 3 or len(pw) > 20:
        return redirect ("/?error=" + "password must between 3 and 20 characters" + "&user=" + user + "&em=" + email)

    if len(user) < 3 or len(user) > 20:
        return redirect ("/?error=" + "username must between 3 and 20 characters" + "&em=" + email)

    if not user:
        return redirect ("/?error=" + "enter a username" + "&em=" + email)

    if email:
        if len(email) < 3 or len(email) > 20:
            return redirect ("/?error=" + "email must be between 3 and 20 characters" + "&user=" + user)
        if '.' not in email or '@' not in email:
            return redirect ("/?error=" + "a valid email contains a period and an @ symbol" + "&user=" + user)
        if ' ' in email:
            return redirect ("/?error=" + "a valid email contains no spaces" + "&user=" + user)
            
    return render_template("welcome.html", username=user)

@app.route("/")
def login_form():
    user = request.args.get("user",default="")
    em = request.args.get("em",default="")
    encoded_error = request.args.get("error")
    return render_template("form.html", username=user, email=em,  error=encoded_error)

if __name__ == '__main__':
    app.run()