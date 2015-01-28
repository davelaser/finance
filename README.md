Finance
========

Personal Finance application for Andre Venancio Limited

* OAuth 2.0 Facebook Authentication


## TODO

### Facebook

#### Facebook Deauthorization url 

1. Facebook App Config

Facebook allows you to provide a Deauthorization URL for your application. You can enter this for your Facebook App here:

    https://developers.facebook.com/apps/YOUR_APP_ID/settings/advanced/ -> Deauthorize Callback URL

This is fired when a User revokes access to your App from their Facebook settings. Importantly it will only ever be an HTTP(S) POST Request, so ensure your Webapp2 RequestHandler has a POST method to receive the data.


Your Request Handler will look the same as your other ones you have created, e.g.

    class MyFacebookDeauthorizeCallback(utils.BaseHandler):
        # Only HTTP(S) POST will be issued by Facebook, so use a post() method in the Class
        def post(self):

            # Well, let's take a look at what Facebook has sent us, shall we?

            for key, value in self.context['request_args'].items():
                logging.info(str(key) + ': ' + str(value))


You already have a URL prepared -> urls.serviceFacebookDeauthorizationCallback.

So add your URL and Handler name as a mapping in your main.py module, the same as the other mappings.

2. Client Revoke Access

It is also possible for your client application to revoke access for the current authenticated User, using JavaScript. It requires that you have the User's access token available in the client:

    *AngularJS example*

    $http({
        method:"DELETE",
        url:'https://graph.facebook.com/v2.2/me/permissions',
        data:{
            accessToken:USER_ACCESS_TOKEN
        }
    })
    .then(function(response) {
        $log.info('Did Facebook revoke access worked??? Inspect the response below');
        $log.info(response);
    });

You wuld implement this perhaps as a "delete my account" feature.

#### Facebook Logout


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