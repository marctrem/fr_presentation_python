#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from codecs import encode

groups_from_users = {'Shrek': {'swamplords', 'ogres'},
                     'Fiona': {'admins', 'princesses'}}


def fetch_user_from_session_id(session_id):
    return encode(session_id, 'rot13')


def provide_user(mon_endpoint):

    def nouvelle_fn(*args, **kwargs):
        session_id = kwargs['req_headers']['session_id']
        mon_endpoint.__globals__['user'] = fetch_user_from_session_id(session_id)
        return mon_endpoint(*args, **kwargs)
    return nouvelle_fn


def provide_groups(mon_endpoint):

    def nouvelle_fn(*args, **kwargs):

        if 'user' not in mon_endpoint.__globals__:
            print(mon_endpoint.__globals__)
            raise Exception('No. Please have user in the function\'s globals before calling this.')

        mon_endpoint.__globals__['groups'] = groups_from_users.get(mon_endpoint.__globals__['user'], None)
        return mon_endpoint(*args, **kwargs)
    return nouvelle_fn


def require_group(allowed_groups):
    def require_group_inner(mon_endpoint):

        def nouvelle_fn(*args, **kwargs):

            if 'groups' not in mon_endpoint.__globals__:
                print(mon_endpoint.__globals__)
                raise Exception('No. Please have groups in the function\'s globals before calling this.')

            if len(allowed_groups.intersection(mon_endpoint.__globals__['groups'])) > 0:
                return mon_endpoint(*args, **kwargs)
            else:
                raise Exception('Pas le droit d\'être ici!')

        return nouvelle_fn
    return require_group_inner


@provide_user
@provide_groups
@require_group({'admins'})
def page_secrete(req_headers=None):
    global user, groups

    return 'Bienvenue %s. Tu utilises %s. Tu fais parti des groupes %s.' % (user, req_headers['user_agent'], groups)


# On fait une requête:
# Session de Fiona: Svban
# Session de Shrek: Fuerx

response = page_secrete(req_headers={'session_id': 'Svban',
                                'user_agent': 'Shrek Explorer 20'})


if response == "Bienvenue Fiona. Tu utilises Shrek Explorer 20. Tu fais parti des groupes {'admins', 'princesses'}.":
    print("Bravo!!!", response)
else:
    print('Essaie encore :(', response)