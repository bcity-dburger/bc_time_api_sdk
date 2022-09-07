# Project description
Package Version Python Versions License

bc_time is the Binary City (BC) Time Application Programming Interface (API) Software Development Kit (SDK) for Python, that allows Python developers to develop integration with [BC Time](https://time.bcity.me).

bc_time is maintained and published by [Binary City](https://bcity.me).

# Getting started
Assuming that you have a supported version of Python installed, you can first set up your environment with:

$ python venv .venv
...
$ . .venv/bin/activate
Then, you can install bc_time from PyPI with:

$ python pip install bc_time
or install from source with:
~~~
$ git clone git@bitbucket.org:dburger/bc_time_api_sdk.git
$ cd bc_time_api_sdk
$ python pip install -r requirements.txt
$ python pip install -e .
~~~

# Using bc_time
After you've installed bc_time, the next step is to set-up your credentials at:\
$HOME/.bc_time/credentials

~~~
[default]
client_id = YOUR_CLIENT_ID
client_secret = YOUR_CLIENT_SECRET
crypt_key = YOUR_CRYPT_KEY
grant_type = YOUR_GRANT_TYPE ; authorisation_code | client_credentials | urn:ietf:params:oauth:grant-type:jwt-bearer
private_key_file_path = FILE_PATH_TO_YOUR_PRIVATE_KEY
~~~

## How to create a private/public key pair
Using OpenSSL, follow these to steps to generate a private & public key par
~~~
 openssl genrsa -out privatekey.pem 1024
 openssl req -new -x509 -key privatekey.pem -out publickey.cer -days 1825
 ~~~

Then, from a Python interpreter:
~~~
>>> import bc_time
>>> visitors = bc_time.Visitors()
>>> response_data = visitors.get_all_using_pagination(filters={'filter_status': bc_time.Status.active})
>>> if response_data['status'] == bc_time.RequestStatus.success:
                for visitor in response_data['data']:
                        print(visitor)
~~~

You also have the option to specify your credentials via the constructor of the Api class:
~~~
>>> import bc_time
>>> api = bc_time.Api(
                client_id='YOUR_CLIENT_ID',
                client_secret='YOUR_CLIENT_SECRET',
                crypt_key='YOUR_CRYPT_KEY',
                grant_type='YOUR_GRANT_TYPE' # Consider using the bc_time.GrantType constants, for example bc_time.GrantType.CLIENT_CREDENTIALS
        )
>>> visitors = bc_time.Visitors(api)
>>> response_data = visitors.get_all_using_pagination()
>>> if response_data['status'] == bc_time.RequestStatus.success:
                for visitor in response_data['data']:
                        print(visitor)
~~~

# Available enumerators
* ApiAuthorisationType
* DeviceCommunicationType
* GrantType
* RequestStatus
* Status

# Available classes
* Api

# Available objects
* ApiAuthorisations
* Branches
* CompanyProfiles
* Controllers
* Departments
* Devices
* DailyOvertimeData
* Employees
* EmployeeLeave
* Settings
* Visitors
* VisitorGroups

# Available methods

## For (most) objects
* create
* create_many
* update
* update_many
* get_all_using_pagination
* get_one
* get_many

## For membership/group objects
Please note that group objects also has access the the methods as defined for Objects.

* add_visitor_to_group
* remove_visitor_from_group
* get_all_members_using_pagination

All methods will return a Dictionary that - depending on the response - may contain the following keys:
* status
* data

Status IDs can be referenced using the enumerator bc_time.RequestStatus.


# Documentation

Please consult our [BC Time API documentation](https://docs.google.com/document/d/1sI0mUy8-65NuDfVKKBxzJSyY9olkjWp3xmtRnR58Lkg/) for more information.