print(open('/task/workspace/invoice/core.py').read())
import subprocess
print(subprocess.run(['grep','-n','region','/task/fixtures/current-tests/test_invoice.py'],capture_output=True,text=True).stdout[:1500])