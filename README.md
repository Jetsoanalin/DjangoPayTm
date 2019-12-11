# Paytm Python Django Latest working 2020 (For python 3)
Paytm Payment Gateway Example On Python Django

* First clone the project, open your terminal and enter the command

```javascript
git clone https://github.com/Jetsoanalin/DjangoPayTm.git
```

* Activate the virtual environment
```javascript
source env/bin/activate
```
* Now enter into the project folder
```javascript
cd DjangoPayTm/payments/
```
* Now install the requirements 
```javascript
pip3 install -r requirements.txt
```
* Now go to payments ->settings.py and enter your credentials
```
PAYTM_MERCHANT_KEY=  "<YOUR-PAYTM-MERCHANT-KEY>"
PAYTM_MERCHANT_ID = "<YOUR-PAYTM-MERCHANT-ID>"
PAYTM_CALLBACK_URL = "http://localhost:8000/response/"
```

*Make Migrations
```
python3 manage.py makemigrations
```

*Migrate the App for transactions details
```
python3 manage.py migrate
```

*Create Super user
```
python3 manage.py createsuperuser
```

* Now in terminal run the server and go to http://localhost:8000/admin/
```
python3 manange.py runserver
```

*Go to
```
1) http://localhost:8000/admin/
    - Log in using superuser credentials
2) http://localhost:8000/paytm/

This should redirect you to test page where pay now will be displayed
Test Credentials to use for login:
Mobile Number – <use your mobile no itself> you will recieve a OTP
card details (enter any random card detail from here for test )- https://www.getcreditcardinfo.com/generatevisacreditcard.php

```
* For Testing Directly
```
https://djangopaytm.herokuapp.com/admin/
login with :
username - jetso
password - jetsoanalin

then goto the paytm page and test the transaction
https://djangopaytm.herokuapp.com/paytm/

```

### Documentation Refered to create the Test app:

 * [PAYTM API DOCUMENTATION](http://paywithpaytm.com/developer/paytm_api_doc/) 
 * [SDK DOCUMENTATION](http://paywithpaytm.com/developer/paytm_sdk_doc/) 
