from flask import Blueprint, render_template, session, request

import pymysql

host = '0.0.0.0'
user_name = 'root'
password = None
db_name = 'delership'

db = pymysql.connect(host, user_name, password, db_name)
# cursor = db.cursor()


index_blueprint = Blueprint('index', __name__)


@index_blueprint.route("/")
def index():
    return render_template("index.html", q1=getQuery1(), q2=getQuery2(), q3=getQuery3(), q4=getQuery4())


def getTable(data):
    first = True
    result = """
    <table>
    <tr>
    """
    for elem in data[0]:
        result += "<th>" + str(elem) + "</th>"

    data.pop(0)

    result += "</tr>"

    for row in data:
        result += "<tr>"
        for elem in row:
            result += "<td>" + str(elem) + "</td>"
        result += "</tr>"

    result += "</table>"

    return result

def getQuery1():
    cursor = db.cursor()

    query = """
    SELECT Count(sid), Eid
    FROM Sales
    GROUP by Eid;
    """
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    print(type(data))
    data = [("Count(sid)", "Eid"), *list(data)]

    return getTable(data)


def getQuery2():
    cursor = db.cursor()

    query = """
    select Count(S.Sid), E.Eid, E.Name
    from Sales S, Employees E
    where S.Eid = E.Eid
    group by E.Eid;
    """
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()

    data = [("Count(S.Sid)", "E.Eid", "E.Name"), *list(data)]

    return getTable(data)


def getQuery3():
    cursor = db.cursor()

    query = """
    SELECT C.Pid, C.Name
    From Customers C
    Where Not Exists ( Select S.Pid 
        From Sales S
        Where S.Pid = C.Pid);
    """
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()

    data = [("C.Pid", "C.Name"), *list(data)]

    return getTable(data)


def getQuery4():
    cursor = db.cursor()

    query = """
    SELECT C.Pid, C.Name, C.Email
    From Customers C
    Where Exists ( SELECT S.Pid
        From Sales S
        Where S.Pid = C.Pid
        Group By S.Pid
        Having Count(*) > 1);
    """
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()

    data = [("C.Pid", "C.Name", "C.Email"), *list(data)]

    return getTable(data)
