from flask import Flask, render_template,request, jsonify, json, redirect, request
import sys
import os
import sqlite3 as sql

app = Flask(__name__)

#connect to the database
conn = sql.connect("db.db") 
c = conn.cursor()

c.execute("SELECT * FROM 'Transaction'")
transactions = c.fetchall()

#list of transactions in JSON format
formatted_transactions = []

#for each transaction append the dictionary to the formated transactions
for transaction in transactions:
	dict = {'id': transaction[0],
			'dateOfTransaction': transaction[1],
			'currencyCode': transaction[3],
			'amount': transaction[2],
			'merchant': transaction[4],
			'description': transaction[5],
			'more info': {'created date': transaction[6]}
			}
			
	formatted_transactions.append(dict)

#main page where the user can access API
@app.route('/')
def index():
	return render_template('index.html') #load the template


#gets API in json format
@app.route('/get_api', methods=['GET'])
def getAPI():
	return jsonify({'Transaction_info': formatted_transactions})

#gets the specific entry in the API, search by transaction id
@app.route('/get_api/<int:transaction_id>', methods=['GET'])
def getSelectedAPI(transaction_id):
	t =  [transaction for transaction in transactions if transaction[0] == transaction_id]

	return jsonify({'transaction': formatted_transactions[transaction_id-1]})

#deletes the specific entry in the API, search by transaction id
@app.route('/delete_api/<int:transaction_id>', methods=['GET','DELETE'])
def deleteSelectedAPI(transaction_id):

	t =  [transaction for transaction in transactions if transaction[0] == transaction_id]

	c.execute("SELECT id FROM 'Transaction' WHERE id = %d" %(transaction_id))
	found = c.fetchall()

	if not found:
		outcome = "Fail: The transaction with that id was not found"

	else:
		try:
			c.execute("DELETE FROM 'Transaction' WHERE id = %d" %(transaction_id))
			conn.commit()
			del formatted_transactions[transaction_id-1]
			outcome = "Success: The transaction has now been deleted"
		except:
			outcome = "Error: please try again later"

	return outcome

#adds new transaction to the database (Client API)
@app.route('/addNewTransaction',  methods=['POST'])
def addNewTransaction():

	if request.method == 'POST':
		date = request.form.get('date')
		amount = request.form.get('amount')
		currencyCode = request.form.get('currency_code')
		merchant = request.form.get('merchant')
		description = request.form.get('description')

		c.execute("INSERT INTO 'Transaction' ('date', amount, currencyCode, merchant, description) VALUES(?, ?, ?, ?, ?)", (date, amount, currencyCode, merchant, description))
		conn.commit()

	return redirect("/") 

if __name__ == "__main__":
    app.run()