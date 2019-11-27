# VALID
# namaUser hanya boleh terdiri atas huruf, angka, dash ('-') dan underscore ('_').
# namaHosting hanya boleh terdiri atas huruf dan angka.
# ekstensi hanya boleh terdiri atas huruf, dengan maksimum 5 karakter.

inputEmail = (input('Masukan alamat email: '))
# print(inputEmail)
angka = ['0','1','2','3','4','5','6','7','8','9']
huruf = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
simbol = ['-','_']
cond1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','-','_']
cond2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']


for i in inputEmail:
    if i == '.':
        iHosting = int(inputEmail.index(i))
    if i == '@':
        iUser = int(inputEmail.index(i))

def namaUser(inputEmail):
    for i in inputEmail[0:iUser]:
        if i in cond1:
            email = True
        else:
            email = False
            break
    return email

def namaHosting(inputEmail):
    for i in inputEmail[iUser+1:iHosting]:
        if i.lower() in cond2:
            email = True
        else:
            email = False
            break
    return email

def namaEkstensi(inputEmail):
    lenEks = len(inputEmail[iHosting+1:])
    for i in inputEmail[iHosting+1:]:
        if i.lower() in huruf and lenEks <=5:
            email = True
        else:
            email = False
    return email

def alamatEmail(inputEmail):
    user = namaUser(inputEmail)
    hosting = namaHosting(inputEmail)
    ekstensi = namaEkstensi(inputEmail)
    if user and hosting and ekstensi == True:
        print('hasil: EMAIL VALID')
    else:
        print('hasil: EMAIL TIDAK VALID ')

alamatEmail(inputEmail)
