'''
This is an example project to create Python based API
Resource: 
https://realpython.com/flask-connexion-rest-api/
https://github.com/realpython/materials/tree/master/flask-connexion-rest

We will also use Python connecxion library and Swagger Configuration 
'''


# import - Libraries in python to create the API
from flask import (
    Flask,
    render_template
)
import connexion

# app - Creating an app instance (Flask based app)
# app = Flask(
#     __name__,
#     template_folder="templates"
# )

# app - Connexion based app
app = connexion.App(__name__, specification_dir='./')

# configuration - Swagger configuration for end points
app.add_api('swagger.yml')

# route - Creating a route to / in our application


@app.route("/")
def home():
    """
    This functions responds to http://localhost:5000
    Returns a web page from templates folder, home.html
    """
    return render_template('home.html')


# run - running the app
if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)
