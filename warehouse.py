from cassandra.cluster import Cluster
import datetime
import uuid

class DataWarehouse:
  last_update = None
  employees = []

  def __init__(self):
    self.cluster = Cluster()
    self.last_update = datetime.datetime.now()
    self.session = self.cluster.connect('pad')

  def get_employees(self):         
    self.employees = self.session.execute("select name, surname, position, id from employees;")
    return self.employees

  def get_employee(self, uid):
    query = "select * from employees where id = " + uid + ";"
    employee = self.session.execute(query)[0]
    return employee

  def post_employee(self, employee):
    query = "insert into employees(name, surname, position, salary, gender, id) values('" + employee['name'] + "', '" + employee['surname'] + "', '" + employee['position'] + "'," + employee['salary'] + ", '" + employee['gender'] + "', now());"
    self.session.execute(query)

  def update_employee(self, employee):
    query = "update employees set name = '" + employee['name'] + "', surname = '" + employee['surname'] + "', position = '" + employee['position'] + "', salary = " + employee['salary'] + ", gender = '" + employee['gender'] + "' where id = " + employee['id'] + ";"
    self.session.execute(query)

  def delete_employee(self, uid):
    query = "delete from employees where id = " + uid + ';'
    self.session.execute(query)

  