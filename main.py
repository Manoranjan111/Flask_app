from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
  return render_template('home.html')


@app.route("/about")
def about_form():
  return render_template('about.html')

@app.route("/project")
def project_form():
  return render_template('project.html')

@app.route("/contact")
def contact_form():
  return render_template('contact.html')


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
