from flask import Flask, request, redirect, render_template_string
from datetime import datetime

app = Flask(__name__)

tickets = []

page = """
<!DOCTYPE html>
<html>
<head>
<title>Password Reset Requests</title>

<style>
body{
    font-family: Arial;
    background:#f3f5f7;
    margin:40px;
}

h1{
    color:#222;
}

form{
    background:white;
    padding:20px;
    width:420px;
    border-radius:8px;
    box-shadow:0 0 8px rgba(0,0,0,0.08);
    margin-bottom:30px;
}

input, select{
    width:100%;
    padding:10px;
    margin-top:8px;
    margin-bottom:15px;
    border:1px solid #ccc;
    border-radius:5px;
}

button{
    background:#0078d7;
    color:white;
    border:none;
    padding:10px 18px;
    border-radius:5px;
    cursor:pointer;
}

table{
    width:100%;
    border-collapse:collapse;
    background:white;
    box-shadow:0 0 8px rgba(0,0,0,0.08);
}

th, td{
    padding:12px;
    border-bottom:1px solid #ddd;
    text-align:left;
}

th{
    background:#0078d7;
    color:white;
}
</style>

</head>
<body>

<h1>Password Reset Requests</h1>

<form method="POST" action="/add">

<label>User Name</label>
<input type="text" name="user" required>

<label>Email</label>
<input type="text" name="email" required>

<label>Department</label>
<input type="text" name="department" required>

<label>Priority</label>
<select name="priority">
<option>Low</option>
<option>Medium</option>
<option>High</option>
</select>

<button type="submit">Open Request</button>

</form>

<table>
<tr>
<th>ID</th>
<th>User</th>
<th>Email</th>
<th>Department</th>
<th>Priority</th>
<th>Date</th>
</tr>

{% for item in tickets %}
<tr>
<td>{{ item.id }}</td>
<td>{{ item.user }}</td>
<td>{{ item.email }}</td>
<td>{{ item.department }}</td>
<td>{{ item.priority }}</td>
<td>{{ item.date }}</td>
</tr>
{% endfor %}

</table>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(page, tickets=tickets)

@app.route("/add", methods=["POST"])
def add():
    new_ticket = {
        "id": len(tickets) + 1,
        "user": request.form["user"],
        "email": request.form["email"],
        "department": request.form["department"],
        "priority": request.form["priority"],
        "date": datetime.now().strftime("%d/%m/%Y %H:%M")
    }

    tickets.append(new_ticket)

    return redirect("/")

app.run(debug=True)