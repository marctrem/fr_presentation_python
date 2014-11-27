#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Vous devez compléter le code de la fonction provide_groups déclarée plus bas.

from codecs import encode

groups_from_users = {'Shrek': ['swamplords', 'ogres'],
                     'Fiona': ['admins', 'princesses']}

def fetch_user_from_session_id(session_id):
    return encode(session_id, 'rot13')

def provide_user(mon_endpoint):

    def nouvelle_fn(*args, **kwargs):
        session_id = kwargs['req_headers']['session_id']
        mon_endpoint.__globals__['user'] = fetch_user_from_session_id(session_id)
        return mon_endpoint(*args, **kwargs)
    return nouvelle_fn

def provide_groups(mon_endpoint):
    raise NotImplementedError('Remplacer ça par votre code!')



@provide_user
@provide_groups
def page_secrete(req_headers=None):
    global user, groups

    return 'Bienvenue %s. Tu utilises %s. Tu fais parti des groupes %s.' % (user, req_headers['user_agent'], groups)


# On fait une requête:
# Session de Fiona: Svban
# Session de Shrek: Fuerx

response = page_secrete(req_headers={'session_id': 'Fuerx',
                                'user_agent': 'Shrek Explorer 20'})


if response == "Bienvenue Shrek. Tu utilises Shrek Explorer 20. Tu fais parti des groupes ['swamplords', 'ogres'].":
    print("Bravo!!!", response)
else:
    print('Essaie encore :(', response)