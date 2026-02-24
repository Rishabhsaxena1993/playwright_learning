#!/usr/bin/env python
import subprocess
import sys

result = subprocess.run(
    [sys.executable, '-m', 'pytest',
     'test_login_account_transfer.py::test_complete_login_account_transfer_flow',
     '-v', '-s', '--tb=short'],
    cwd='C:\\Users\\visha\\PycharmProjects\\playwright_learning',
    capture_output=True,
    text=True
)

print("STDOUT:")
print(result.stdout)
print("\nSTDERR:")
print(result.stderr)
print(f"\nReturn code: {result.returncode}")

