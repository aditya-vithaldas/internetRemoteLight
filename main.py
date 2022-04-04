from flask import Flask, render_template, request
app = Flask('app')

@app.route('/')
def main_remote_page():
  return render_template('start.html')

@app.route('/buttonclick')
def button_click():
  name = request.args.get("function")
  f = open("file.txt", "w")
  f.write(name)
  f.close()
  return "file is written"

@app.route('/getcontrol')
def get_control():
  f = open("file.txt", "r")
  ret = f.read()
  f.close()
  return ret
  
app.run(host='0.0.0.0', port=8080)