from flask import Flask, request, jsonify
from models import database, Account, TransactionModel
import time

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bank.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

database.init_app(app)

with app.app_context():
    database.create_all()

    if Account.query.count() == 0:
        alice = Account("Alice", 1000)
        bob  = Account("Bob", 500)
        charlie = Account("Charlie", 100)
         
        database.session.add(alice)
        database.session.add(bob)
        database.session.add(charlie)
        database.session.commit()


@app.route("/")
def test():
    return "working yey"


@app.route("/accounts", methods = ["GET"])
def getAccounts():
    accounts = Account.query.all()
    accountsList = []
    for acc in accounts:
        account = {
            "id": acc.id,
            "name": acc.name,
            "balance": acc.balance
        }
        accountsList.append(account)
    return jsonify(accountsList), 200


@app.route("/transactions", methods = ["GET"])
def getTransactions():
    transactions = TransactionModel.query.all()
    transactionsList = []
    for trans in transactions:
        transaction = {
            "id": trans.id,
            "registeredTime": trans.registeredTime_,
            "execTime": trans.execTime_,
            "success": trans.success_,
            "amount": trans.amount_,
            "sourceID": trans.sourceID_,
            "destID": trans.destID_
        }
        transactionsList.append(transaction)
    return jsonify(transactionsList), 200


@app.route("/transfer", methods = ["POST"])
def transfer():
    try: 
        data = request.json
        sourceID = data.get("sourceID")
        destID = data.get("destID")
        amount = data.get("amount")

        sourceAcc = database.session.get(Account, sourceID)
        destAcc = database.session.get(Account, destID)

        if not sourceAcc or not destAcc:
            return jsonify({"error": "Invalid account"}), 400
        if sourceID == destID:
            return jsonify({"error": "Invalid transaction"}), 400
        if amount <= 0:
            return jsonify({"error": "Invalid amount"}), 400
        if sourceAcc.balance < amount:
            return jsonify({"error": "Insufficient funds"}), 400
        
        registeredTime = int(time.time() * 1000)
        
        sourceAcc.balance -= amount
        destAcc.balance += amount

        execTime = int(time.time() * 1000)

        transaction = TransactionModel(
            registeredTime = registeredTime, 
            execTime = execTime,
            success = True,
            amount = amount,
            sourceID = sourceID,
            destID = destID
        )   

        database.session.add(transaction)
        database.session.commit()
            
        transactionLog = {
            "id": transaction.id,
            "registeredTime": transaction.registeredTime,
            "execTime": transaction.execTime,
            "success": transaction.success,
            "amount": transaction.amount,
            "sourceID": transaction.sourceID,
            "destID": transaction.destID
        }

        return jsonify(transactionLog), 200

    except Exception as e:
        return jsonify({"error": str(e), "status": 500}), 500


if __name__ == '__main__':
    app.run(debug=False)

