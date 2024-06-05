1. python3 manage.py migrate
2. python3 manage.py csu to create superuser
3. python3 manage.py clear_permissions
4. python3 manage.py loaddata json_data/auth.json
5. python3 manage.py loaddata json_data/users.json to apply users(perms and logs below)
6. python3 manage.py fill to apply fixtures


logins:

    log: bla@mail.ru
    pw: 123
    perms: su

    log: jendoc@inbox.ru
    pw: SgD3mQRGmu
    perms: default user w/o perms
    
    log: olapopaola@mail.ru
    pw: YpyxBhJDeq
    perms: manager