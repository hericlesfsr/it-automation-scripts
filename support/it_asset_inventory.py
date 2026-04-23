from flask import Flask, request, redirect, render_template_string
from datetime import datetime

app = Flask(__name__)

assets = []

html = """
<!DOCTYPE html>
<html>
<head>
<title>IT Asset Inventory</title>

<style>
body{
    font-family: Arial;
    background:#f4f6f8;
    margin:40px;
}

h1{
    color:#222;
}

form{
    background:white;
    padding:20px;
    border-radius:8px;
    width:430px;
    box-shadow:0 0 10px rgba(0,0,0,0.08);
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
    box-shadow:0 0 10px rgba(0,0,0,0.08);
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

<h1>IT Asset Inventory Dashboard</h1>

<form method="POST" action="/add">

<label>Hostname</label>
<input type="text" name="hostname" required>

<label>Assigned User</label>
<input type="text" name="user" required>

<label>Sector</label>
<input type="text" name="sector" required>

<label>Asset Tag</label>
<input type="text" name="tag" required>

<label>Status</label>
<select name="status">
<option>Active</option>
<option>Maintenance</option>
<option>Reserve</option>
</select>

<button type="submit">Register Asset</button>

</form>

<table>
<tr>
<th>ID</th>
<th>Hostname</th>
<th>Assigned User</th>
<th>Sector</th>
<th>Asset Tag</th>
<th>Status</th>
<th>Date</th>
</tr>

{% for item in assets %}
<tr>
<td>{{ item.id }}</td>
<td>{{ item.hostname }}</td>
<td>{{ item.user }}</td>
<td>{{ item.sector }}</td>
<td>{{ item.tag }}</td>
<td>{{ item.status }}</td>
<td>{{ item.date }}</td>
</tr>
{% endfor %}

</table>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html, assets=assets)

@app.route("/add", methods=["POST"])
def add():
    item = {
        "id": len(assets) + 1,
        "hostname": request.form["hostname"],
        "user": request.form["user"],
        "sector": request.form["sector"],
        "tag": request.form["tag"],
        "status": request.form["status"],
        "date": datetime.now().strftime("%d/%m/%Y %H:%M")
    }

    assets.append(item)

    return redirect("/")

app.run(debug=True)