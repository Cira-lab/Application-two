from flask import Flask,render_template,request,redirect,url_for
app=Flask(__name__)
storage=[]
@app.route("/")
def home():
    return render_template("index.html",files=storage)

@app.route("/uploads",methods=['POST'])
def uploads():
    filename=request.form.get('filename')
    if filename and filename not in storage:
        storage.append(filename)
    return redirect(url_for('home'))

@app.route("/update/<old_name>",methods=["POST"])
def update(old_name):
    newname=request.form.get('newname')
    if old_name in storage and newname:
        storage[storage.index(old_name)]=newname
    return redirect( url_for('home'))

@app.route("/delete/<deletefile>",methods=["POST"])
def delete(deletefile):
    if deletefile in storage:
        storage.remove(deletefile)
        

    return redirect(url_for('home'))


if __name__=="__main__":
    app.run(debug=True)
