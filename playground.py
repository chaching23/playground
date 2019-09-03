from flask import Flask, render_template  
app = Flask(__name__)    

@app.route('/play/')          
def hello():
    print("function")
    return render_template("index.html", phrase="hello", times=1) 



@app.route('/play/<xxx>')          
def hello_2(xxx):
    return render_template("index.html", phrase="hello", times=int(xxx)) 


@app.route('/play/<xxx>/<zz>')          
def hello_3(xxx,zz):
    return render_template("index.html", phrase="hello", times=int(xxx), color=zz) 



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.








