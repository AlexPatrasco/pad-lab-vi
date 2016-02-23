from flask import Flask, request
from warehouse import DataWarehouse
import json
app = Flask(__name__)
dw = DataWarehouse()

def get_employees():
  emps = dw.get_employees()
  json_emps = "["
  for e in emps:
    json_emps += "{\"name\":\"" + e[0] + "\",\"surname\":\"" + e[1] + "\",\"position\":\"" + e[2] + "\",\"id\":\"" + str(e[3]) + "\"},"
  json_emps = json_emps[:-1]
  json_emps += "]"
  return json_emps


@app.route("/employees", methods = ['GET', 'POST'])
def index():
  if request.method == 'GET':
    return get_employees()
  else:
    employee = json.loads(request.data)['employee']
    dw.post_employee(employee)
    return '{"code":"200"}'

@app.route("/employees/<id>")
def employee(id):
  if request.method == 'GET':
    emp = dw.get_employee(id)
    json_emp = "{\"id\":\"" + str(emp[0]) + "\",\"gender\":\"" + emp[1] + "\",\"name\":\"" + emp[2] + "\",\"position\":\"" + emp[3] + "\",\"salary\":\"" + str(emp[4]) + "\",\"surname\":\"" + emp[5] + "\"}"
    print json_emp
    return json_emp
  
@app.route("/employee", methods = ['UPDATE'])
def edit():
    employee = json.loads(request.data)['employee']
    dw.update_employee(employee)
    return '{"code":"200"}'

  

  
if __name__ == "__main__":
    app.run(debug = True)