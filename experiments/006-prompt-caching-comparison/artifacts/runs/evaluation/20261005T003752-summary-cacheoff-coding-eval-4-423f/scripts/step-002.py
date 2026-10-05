print(open('/task/workspace/invoice/core.py').read()[:2000])
import subprocess
print(subprocess.run(['grep','-n','def test\\|format_money','/task/fixtures/current-tests/test_invoice.py'],capture_output=True,text=True).stdout[:2000])