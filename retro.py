import winreg
import sys

key_path = "SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize"
app_theme = 'AppsUseLightTheme'
sys_theme = 'SystemUsesLightTheme'

def set_theme(value):
    try:
        winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path)
        reg_handle = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_WRITE
        )
        winreg.SetValueEx(reg_handle, app_theme, 0, winreg.REG_DWORD, value)
        winreg.SetValueEx(reg_handle, sys_theme, 0, winreg.REG_DWORD, value)
        winreg.CloseKey(reg_handle)
        return True
    except:
        return False

def main():
    if len(sys.argv) == 2:
        setting = sys.argv[1]
        if setting == '1':
            set_theme(0)
        elif setting == '0':
            set_theme(1)
        else:
            print('[R] Value must be either 0 or 1')
    else:
        print('[R] Usage: python retro.py 0-1 (0: white ; 1: dark)')

if __name__ == "__main__":
    main()