Finance
========

Personal Finance application for Andre Venancio Limited

* OAuth 2.0 Facebook Authentication


## TODO

### Facebook
* Facebook Deauthorization url 
* Facebook Logout


### GAE
* Verify is GAE Session is correctly implemented.
* Add logout method that destroys session.

#### Client Model
* add 'Client' to Models
Example:
```javascript
Client: {
    name: 'Razorfish',
    uid: [RANDOM_GENERATED_ID]
}
```

* add client to database
* edit client in database
* delete client from database

#### Transaction Model
* add 'Transaction' Entity to Models
```javascript
Transaction: {
    type: [EXPENSE, INCOME, ETC],
    uid: [RANDOM_GENERATED_ID],
    value: 480.35,
    currency: [POUND, EURO, DOLLAR],
    client_uid: [CLIENT_UID],
    date_added: [CURRENT_DATE],
    date_last_modified: [DATE],
    modified_by: [USER]
}
```
* add transaction to database
* edit transaction in database
* delete transaction from database
* get transaction by ID, or date, or client