from flask import *  
app = Flask(__name__)  
 
@app.route('/')  
def upload():  
    return render_template("file.html")  
 
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']  
        f.save(f.filename)  
        return "successfully uploaded file.." 
  
if __name__ == '__main__':  
    app.run(debug = True)  