import requests
from requests.auth import HTTPBasicAuth
import urllib3
import json
from ConfigParser import SafeConfigParser
import os

class EM7API:

  def __init__(self, \
               uri=None, \
               username=None, \
               password=None, \
               verify_ssl=True, \
               environment='DEFAULT'):
      
    parser = SafeConfigParser({'uri': uri, 'username': username, 'password': password})

    # accept config files from multiple locations
    parser.read([os.path.expanduser('~/.em7api'), '.em7api'])
    
    self._base_uri = parser.get(environment, 'uri').rstrip('/')
    self._username = parser.get(environment, 'username')
    self._password = parser.get(environment, 'password')

    if not self._base_uri:
      raise ValueError('URI required')
    if not self._username:
      raise ValueError('username required')
    if not self._password:
      raise ValueError('password required')
    
    self._session = requests.Session()
    self._session.auth = HTTPBasicAuth(self._username, self._password)

    self._verify_ssl = verify_ssl
    if not self._verify_ssl:
      # supress SSL warnings from getting printed
      urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

  def __get_uri(self, resource):
    return '{}/{}'.format(self._base_uri, resource.lstrip('/'))

  def get(self, resource, parameters={}):
    return self._session.get(self.__get_uri(resource), \
                             verify=self._verify_ssl, \
                             params=parameters).json()

  def post(self, resource, parameters={}, data={}):
    return self._session.post(self.__get_uri(resource), \
                              verify=self._verify_ssl, \
                              params=parameters, \
                              data=json.dumps(data)).json()

  def put(self, resource, parameters={}, data={}):
    return self._session.put(self.__get_uri(resource), \
                             verify=self._verify_ssl, \
                             params=parameters, \
                             data=json.dumps(data)).json()

  def delete(self, resource, parameters={}):
    return self._session.delete(self.__get_uri(resource), \
                                verify=self._verify_ssl, \
                                params=parameters)
