"""
Comment validator using Voluptuous
"""

# library
from voluptuous import Schema, All, In, Required, Range
from voluptuous.util import Upper
from voluptuous.validators import Email

# Validates a comment
comment_schema = Schema({
    # IDs should be non-negative
    'id': All(int, Range(min=0)),
    'post_id': All(int, Range(min=0)),
    # Email has a special validator
    'email': All(str, Email()),
    'name': str,
    'body': str,
    # This allows us to provide a nullable default value
    Required('user_id', default=None): In((int, None))
}, required=True)

# Validates a list of comments
comments_schema = Schema([comment_schema])
