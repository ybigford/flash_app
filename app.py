#initialize flask
from flask import Flask, render_template
app = Flask(__name__)

#define home page route
@app.route('/')
def home():
    return render_template ('index.html')

#define about page route
@app.route('/about')
def about():
    return render_template ('about.html')

#define contact page route
@app.route('/contact')
def contact():
    return render_template ('contact.html')


#define function to initialize database
def init_db():

    #create a connection to SQlite database - data.db    
    with sqlite3.connect('data.db') as conn:
        
        #execute SQL command to create 'entries' table
        #the created table has 2 column, id column (primary key) and name column (text)
        conn.execute('CREATE TABLE IF NOT EXISTS entries (id INTEGER PRIMARY KEY, name TEXT)')
        
        #commit to the change to the database
        conn.commit()
    
#define a route for route URL '/' and use GET and POST methods
@app.route('/', methods=['GET','POST'])
def index():
    
     #if the request is equal to POST (form was submitted)
     if request.method == 'POST':
        
        #get the value submitted from the form input field (name)
        name = request.form['name']
        
        #connect to SQLite database and insert the submitted name into the 'entries' table
        with sqlite3.connect('data.db') as conn:
            conn.execute('INSERT INTO entries (name) VALUES (?)', (name,))
            conn.commit()      
    #render 'index.html' template, which should contain the form and show entries
     return render_template('index.html')
    
#this block runs the application only if this script is executed directly
if __name__ == '__main__':
    
    #start the Flask development server with debugging enabled
    app.run(debug=True)
    
    
   
#echo "# flash_app" >> README.md
#git init
#git add .
#git commit -m "first commit"
#git branch -M main
#git remote add origin https://github.com/ybigford/flash_app.git
#git push -u origin main