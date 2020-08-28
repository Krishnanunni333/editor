import os
import subprocess

def prorun(i):
    with open('Code.py','w') as f:
        f.write(i)
    os.chmod('Code.py', 0o777)

    p = subprocess.Popen(["python3", "Code.py"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    output, errors = p.communicate()
    return [output,errors]
    
