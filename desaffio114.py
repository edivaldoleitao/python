import urllib.request

try:
    site = urllib.request.urlopen('http://www.youtube.com')
except Exception as erro:
    print(f'problema de conexão do tipo :{erro.__class__}')
else:
    print('conexão estabelecida')
    print(site.read())
