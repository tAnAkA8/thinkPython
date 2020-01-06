fin = open('ba1d_file')
#[Errno 2] No such file or directory: 'ba1d_file'

fout = open('/etc/passwd', 'w')
#[Errno 2] No such file or directory: '/etc/passwd'

fin = open('home')
#[Errno 21] Is a directory

try:
    fin = open('bad_file')
except:
    print('Something went wrong')