"""
Example presents usage of the successful submissions.getMulti() API method
"""
from sphere_engine import CompilersClientV4

# define access parameters
accessToken = '<access_token>'
endpoint = '<endpoint>'

# initialization
client = CompilersClientV4(accessToken, endpoint)

# API usage
response = client.submissions.getMulti([2017, 2018])
