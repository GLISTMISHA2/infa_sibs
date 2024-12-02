'''Данные об email-адресах студентов хранятся в словаре:
emails = {’gryffindor.com’: [’andrei_serov’, ’alexander_pushkin’, ’elena_belova’, ’k_stepanov’],
’hufflepuff.com’: [’alena.semyonova’, ’ivan.polekhin’, ’marina_abrabova’],
’hogwarts.com’: [’sergei.zharkov’, ’julia_lyubimova’, ’vitaliy.smirnoff’],
’slytherin.com’: [’ekaterina_ivanova’, ’glebova_nastya’],
’ravenclaw.com’: [’john.doe’, ’mark.zuckerberg’, ’helen_hunt’]}
Нужно дополнить код таким образом, чтобы он вывел все адреса в формате имя_пользователя@домен.'''

email = {
    'gryffindor.com': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'k_stepanov'],
    'hufflepuff.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
    'hogwarts.com': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
    'slytherin.com': ['ekaterina_ivanova', 'glebova_nastya'],
    'ravenclaw.com': ['john.doe', 'mark.zuckerberg', 'helen_hunt']
}
for dom, users in email.items():
    for u in users:
        email = f"{u}@{dom}"
        print(email)
