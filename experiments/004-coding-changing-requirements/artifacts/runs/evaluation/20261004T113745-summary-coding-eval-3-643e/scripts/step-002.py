import subprocess
print(open('/task/workspace/invoice/core.py').read());print(open('/task/workspace/invoice/__init__.py').read())
print(subprocess.run(['grep','-n','format_money\|assert','/task/fixtures/current-tests/test_invoice.py'],capture_output=True,text=True).stdout[:2500])