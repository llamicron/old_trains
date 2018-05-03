import requests

from trains.data.mailgun import auth, domain

template_header = """
\n\n
Howdy!
\n\n
"""

template_footer = """
\n\n
Thanks!
\n\n
"""

class Mailer(object):
    def send(self, data):
        assert type(data) is dict
        assert data['from']
        assert data['to']
        assert data['subject']
        assert data['text']

        data['text'] = template_header + data['text'] + template_footer

        return requests.post(
            domain,
            auth=auth,
            data=data
        )

# data = {
#     'from': 'me <llamicron@gmail.com>',
#     'to': 'me <llamicron@gmail.com>',
#     'subject': 'wassup',
#     'text': """
#     test text
#     """
# }

# m = Mailer()
# print(m.send(data))
