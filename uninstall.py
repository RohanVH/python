import subprocess

def get_installed_app_ids():
    ps_command = "winget list | ForEach-Object { ($_ -split '\\s{2,}')[1] }"
    result = subprocess.run(["powershell", "-Command", ps_command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    if result.returncode != 0:
        print("Failed to retrieve the installed application IDs.")
        print(result.stderr)
        return []
    
    # Split the output into lines and return the list of app IDs
    app_ids = result.stdout.splitlines()
    return app_ids

def uninstall_app(app_id):
    uninstall_command = ['winget', 'uninstall', '--id', f'{app_id}']
    result = subprocess.run(uninstall_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    if result.returncode != 0:
        print(f"Failed to uninstall {app_id}.")
        print(result.stderr)
    else:
        print(f"Successfully uninstalled {app_id}.")
        print(result.stdout)

if __name__ == "__main__":
    app_ids = get_installed_app_ids()
    
    if app_ids:
        print("Application IDs found:")
        for app_id in app_ids:
            print(app_id)
            # Uninstall each app
            uninstall_app(app_id)
