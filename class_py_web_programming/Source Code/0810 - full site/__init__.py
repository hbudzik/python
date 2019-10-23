from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    try:

        return render_template('index.html')
    except Exception as e:
        return(str(e))


@app.route("/about/")
def aboutpage():
    try:
        return render_template('about.html')
    except Exception as e:
        return(str(e))


@app.route("/page-one/")
def pageone():
    try:
        button_type = 'info'
        name = "Python"
        example_list = ["2.5", "2.6", "2.7", "3.1", "3.3", "3.4"]
        return render_template('page-one.html',button_type=button_type, name = name, example_list = example_list)
    except Exception as e:
        return(str(e))

@app.errorhandler(404)
def four_oh_four(e):
    
    return render_template("404.html")








    

    
    

if __name__ == "__main__":
    app.run()
