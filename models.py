from flask_sqlalchemy import SQLAlchemy

database = SQLAlchemy()

class Account(database.Model):
    id = database.Column(database.Integer, primary_key = True)
    name = database.Column(database.String(50), nullable = False)
    balance = database.Column(database.Float, nullable = False)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance


class TransactionModel(database.Model):
    id = database.Column(database.Integer, primary_key = True)
    registeredTime = database.Column(database.BigInteger, nullable = False)
    execTime = database.Column(database.BigInteger, nullable = False)
    success = database.Column(database.Boolean, nullable = False)
    amount = database.Column(database.Integer, nullable = False)
    sourceID = database.Column(database.Integer, database.ForeignKey('account.id'), nullable = False)
    destID = database.Column(database.Integer, database.ForeignKey('account.id'), nullable = False)

    sourceAcc = database.relationship('Account', foreign_keys = [sourceID])
    destAcc = database.relationship('Account', foreign_keys = [destID])