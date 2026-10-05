print(open('/task/workspace/invoice/core.py').read())
import subprocess
print(subprocess.run(['grep','-n','format_money\|bulk\|qty','/task/fixtures/current-tests/test_invoice.py'],capture_output=True,text=True).stdout)