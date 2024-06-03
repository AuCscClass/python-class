import subprocess


# This function is used to get windows difficult apps
def get_default_apps():
    try:
        # Run the Windows PowerShell command to get the default apps
        result = subprocess.run(['powershell',
                                 'Get-AppxPackage | Where-Object {($_.Publisher -like "*Microsoft Corporation*") '
                                 '-and (-not $_.IsFramework)}'],
                                capture_output=True, text=True)

        # Split the output by newlines to get individual app information
        app_lines = result.stdout.strip().split('\n')
        print(app_lines)
        # Extract the name of each app
        defaults = [line.split(':')[1].strip() for line in app_lines if line.startswith('Name')]


        return defaults
    except subprocess.CalledProcessError:
        return []


# Test the function
print(get_default_apps())
