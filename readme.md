## Code Assignment - Bank API

This API allows users to view account details, transaction history, and perform money transfers between accounts. It is built using Flask and SQLAlchemy, with an SQLite database for data storage.

---


## Database Setup

An SQLite database (`bank.db`) is used to store account and transaction data. The database is initialized automatically when the application starts if it doesn't already exist.

The database contains two tables:
- **Accounts**: Stores account details.
- **Transactions**: Stores the transaction history of all money transfers.

NOTE: This version already comes with an existing database (`bank.db`). If you want to start fresh with new accounts, simply delete the `bank.db` file. A new database with sample accounts (Alice, Bob, and Charlie) will be created automatically upon first run.

## How to Run

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Make sure you have the required packages**:
    - **Python 3.x**
    - **Flask**
    - **Flask-SQLAlchemy**
  
    You can install the required packages using pip:
  
    ```bash
    pip install flask flask-sqlalchemy
    ```

4. **Run the Flask app**:

   ```bash
   python main.py
   ```

  App runs at `http://127.0.0.1:5000/` by default.


## Testing the API

Below is a step by step on how to use Postman to test the API

### **1. Get All Accounts**
  
#### Steps to Use in Postman:
1. **Open Postman**.
2. Select **GET** from the dropdown next to the URL bar.
3. In the URL bar, enter:
   ```
   http://127.0.0.1:5000/accounts
   ```
4. Click **Send**.

#### Expected Response:
You will receive a list of all accounts in JSON format, similar to the following:

```json
[
    {
        "balance": 1100.0,
        "id": 1,
        "name": "Alice"
    },
    {
        "balance": 100.0,
        "id": 2,
        "name": "Bob"
    },
    {
        "balance": 400.0,
        "id": 3,
        "name": "Charlie"
    }
]
```

### **2. Get All Transactions**

#### Steps to Use in Postman:
1. Select **GET** from the dropdown next to the URL bar.
2. In the URL bar, enter:
   ```
   http://127.0.0.1:5000/transactions
   ```
3. Click **Send**.

#### Expected Response:
You will get a list of all transaction records in JSON format, like this:

```json
[
    {
        "id": 1,
        "registeredTime": 1672322000000,
        "execTime": 1672322100000,
        "success": true,
        "amount": 100,
        "sourceID": 1,
        "destID": 2
    }
]
```

### **3. Transfer Money**

#### Steps to Use in Postman:
1. Select **POST** from the dropdown next to the URL bar.
2. In the URL bar, enter:
   ```
   http://127.0.0.1:5000/transfer
   ```
3. Click the **Body** tab, and select **raw** and **JSON** from the options.
4. In the body section, provide the JSON data for the transfer. For example:

   ```json
   {
       "sourceID": 1,
       "destID": 2,
       "amount": 100
   }
   ```

5. Click **Send**.

#### Expected Response:
If the transaction is successful, you will receive a confirmation in JSON format:

```json
{
    "id": 1,
    "registeredTime": 1672322000000,
    "execTime": 1672322100000,
    "success": true,
    "amount": 100,
    "sourceID": 1,
    "destID": 2
}
```

#### Possible Error Responses:
- **Invalid account**: If either the source or destination account does not exist:
  ```json
  {
      "error": "Invalid account"
  }
  ```
  
- **Insufficient funds**: If the source account does not have enough balance:
  ```json
  {
      "error": "Insufficient funds"
  }
  ```

- **Invalid amount**: If the amount is zero or negative:
  ```json
  {
      "error": "Invalid amount"
  }
  ```
