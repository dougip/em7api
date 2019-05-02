======
em7api
======

An unofficial Python wrapper for the Science Logic EM7 API

GitHub: https://github.com/dougip/em7api/
PyPI: https://pypi.org/project/em7api/

Getting Started
===============

Installation
------------

Install from the PyPI repository


.. code-block:: python

    pip install em7api

Prerequisites
-------------

The following are required:

- URI of an existing EM7 portal
- username
- password

Configuration file
------------------

Create a file named .em7api located in one of these locations:

- Home directory: ~/.em7api
- Present working directory: ./.em7api

File format:


.. code-block:: ini

    [DEFAULT]
    uri = https://em7.example.com
    username = myEM7user
    password = myEM7password

More than one environment can be configured by adding additional sections:


.. code-block:: ini

    [DEFAULT]
    uri = https://em7.example.com
    username = myEM7user
    password = myEM7password
    
    [PRODUCTION]
    uri = https://prod.em7.example.com
    username = prodEM7user
    password = prodEM7user

    [DEV]
    uri = https://dev.em7.example.com

Usage
=====

Passing credentials to the constructor
--------------------------------------

The non-default environments can be chosen by passing the environment parameter to the constructor:


.. code-block:: python

    import em7api
    
    dev_session = em7api.EM7API(environment='DEV', verify_ssl=False)

The credentials and URI can also be passed as parameters instead of configured in a file:


.. code-block:: python
    
    import em7api

    session = em7api.EM7API(uri='https://em7.example.com', \
                           username='myEM7user', \
                           password = 'myEM7pass', \
                           verify_ssl=False)

verify_ssl option
-----------------

If SSL verification fails, the API call will fail with an SSL error.  The easiest way to deal with this is to disable ssl by setting verify_ssl to False when calling the constructor.  The verify_ssl value just gets passed to requests's verify value and can be either True, False, or the location of a CA_bundle.  This is not disabled by default due to the obvious security implications.

 
.. code-block:: python
    
    import em7api

    dev_session = em7api.EM7API(verify_ssl=False)

get
---

Read operations are done with a get.  Doing a get with the URI of a resource will usually return a list of the related objects


.. code-block:: python

    print session.get('/api/account')


Each object will have its own URI, and doing a get on that will return details of that specific object

.. code-block:: python
    
    print session.get('/api/account/1')

limit parameter
---------------

By default, EM7 limits its search to 100.  If the data set is greater than that, the limit parameter needs to be specified


.. code-block:: python
    
    print session.get('/api/powerpack', parameters={'limit': 200})

Filters
-------

The filter parameter can be sent to filter the results.  The available filters can be found in the API browser or in the API manual

.. code-block:: python
    
    print session.get('/api/powerpack', parameters={'limit': 1000, \
                                                    'filter.0.name.begins_with': 'Science'})

More than one filter can be added.  Each additional filter needs its number incremented.

.. code-block:: python
    
    print session.get('/api/powerpack', parameters={'limit': 1000, \
                                                    'filter.0.name.begins_with': 'Science', \
                                                    'filter.1.name.contains': 'EM7'})

post
----

Adding and updating objects is done with a post.  The data dictionary contains the details that need to be set for the new or updated object.  Whatever is not specified in the data dictionary will mostly be left alone or set to a default value.  The following would add a new organization, specifying the company name and leaving the rest blank:

.. code-block:: python
    
    session.post('/api/organization', data={'company': 'My Company'})

To update an existing object, specify its own URI as the resource, and pass the changes in the data dictionary

.. code-block:: python
    
    session.post('/api/organization/1', data={'company': 'Your Company'})

put
---

Updates can also be done with a put.  This is more restrictive, as it requires the object to already exist and requires a larger set of the objects' details to be sent in the data dictionary, otherwise it will result in an error.

.. code-block:: python
    
    session.put('/api/organization/1', data={'company': 'Another Company', \
                                             'address': '', \
                                             'city': 'New York', \
                                             'state': 'NY', \
                                             'zip': '', \
                                             'country': 'US', \
                                             'contact_fname': '', \
                                             'contact_lname': '', \
                                             'title': '', \
                                             'dept': '', \
                                             'billing_id': '', \
                                             'crm_id': '', \
                                             'phone': '', \
                                             'fax': '', \
                                             'tollfree': '', \
                                             'email': '', \
                                             'date_create': None, \
                                             'date_edit': '', \
                                             'updated_by': '/api/account/1', \
                                             'theme': '1', \
                                             'longitude': '', \
                                             'latitude': '', \
                                             'notification_append': None})

delete
------

Objects can be removed with a delete.

.. code-block:: python
    
    session.delete('/api/organization/1')

Acknowledgments
===============

This project relies on the requests module to make the API calls

License
=======

This project is licensed under the `MIT license`_

.. _`MIT license`: https://github.com/dougip/em7api/blob/master/LICENSE.md
