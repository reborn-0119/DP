import hashlib
import requests

def checkPwdLeak(pwd):
    sha1pwd = hashlib.sha1(pwd.encode('utf-8')).hexdigest().upper()
    
    prefix, suffix = sha1pwd[:5], sha1pwd[5:]
    
    url = f'https://api.pwnedpasswords.com/range/{prefix}'
    
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f'Error fetching : {response.status_code}, check the API and try again')
    
    hashes = (line.split(':') for line in response.text.splitlines())
    for h, count in hashes:
        if h == suffix:
            return int(count)
    return 0
    
    
    
    
    
def checkPwdFile(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            try:
                username,password = line.strip().split(',')
                leak_count = checkPwdLeak(password)
                if leak_count:
                    print(f'Password for {username} was found {leak_count} times in data breaches.')
                    
                else:
                    print(f'Password for {username} was not found in data breaches.')
                    
            except ValueError:
                print(f'Error reading line: {line.strip()}')
    
    
    
file_name='prog4.txt'
checkPwdFile(file_name)