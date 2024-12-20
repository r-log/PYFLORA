import winreg
import sys
import os
from urllib.parse import urlparse, parse_qs
import traceback


class URLHandler:
    @staticmethod
    def register_url_scheme():
        """Register the pyflora:// URL scheme."""
        try:
            # Get absolute paths
            python_path = os.path.abspath(sys.executable)
            app_path = os.path.abspath(sys.argv[0])
            script_dir = os.path.dirname(app_path)

            print(f"Registering URL scheme with:")
            print(f"Python path: {python_path}")
            print(f"App path: {app_path}")
            print(f"Script directory: {script_dir}")

            # Create main protocol key
            with winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\Classes\pyflora") as key:
                winreg.SetValue(key, "", winreg.REG_SZ, "URL:PyFlora Protocol")
                winreg.SetValueEx(key, "URL Protocol", 0, winreg.REG_SZ, "")

                # Add default icon
                with winreg.CreateKey(key, "DefaultIcon") as icon_key:
                    winreg.SetValue(icon_key, "", winreg.REG_SZ,
                                    f"{python_path},0")

                # Set command to run without keeping the window open
                with winreg.CreateKey(key, r"shell\open\command") as cmd_key:
                    cmd = f'cmd /c cd /d "{script_dir}" && "{python_path}" "{app_path}" "%1"'
                    print(f"Command registered: {cmd}")
                    winreg.SetValue(cmd_key, "", winreg.REG_SZ, cmd)

            print("URL scheme registered successfully")

            # Verify registration
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\Classes\pyflora\shell\open\command") as key:
                value = winreg.QueryValue(key, "")
                print(f"Verified command: {value}")

        except Exception as e:
            print(f"Error registering URL scheme: {e}")

    @staticmethod
    def parse_reset_url(url):
        """Parse reset URL and extract token."""
        try:
            print(f"\nParsing reset URL: {url}")
            # Replace double slash with single slash after scheme
            normalized_url = url.replace('://', ':/')
            parsed = urlparse(normalized_url)
            print(f"Parsed URL components: {parsed}")

            # Combine netloc and path for checking, remove trailing slash
            full_path = f"/{parsed.netloc}{parsed.path}" if parsed.netloc else parsed.path
            full_path = full_path.rstrip('/')  # Remove trailing slash
            print(f"Full path (normalized): {full_path}")

            if parsed.scheme == 'pyflora' and full_path == '/reset-password':
                query = parse_qs(parsed.query)
                print(f"Parsed query parameters: {query}")

                token = query.get('token', [None])[0]
                print(f"Extracted token: {token}")

                if token:
                    clean_token = token.strip()
                    print(f"Clean token: {clean_token}")
                    return clean_token
                else:
                    print("No token found in query parameters")
                    return None
            else:
                print(
                    f"Invalid URL scheme ({parsed.scheme}) or path ({full_path})")
                return None
        except Exception as e:
            print(f"Error parsing reset URL: {e}")
            traceback.print_exc()
            return None

    @staticmethod
    def show_dialog(main_window, token):
        """Show the password reset dialog."""
        try:
            print("Found main window, showing dialog...")
            print("Processing events and showing dialog...")
            print("Preparing to show dialog...")
            print("Creating controllers...")

            from src.controllers.password_reset_controller import PasswordResetController
            password_reset_controller = PasswordResetController(main_window)

            print("Showing reset dialog...")
            password_reset_controller.show_reset_dialog(token)

        except Exception as e:
            print(f"Error showing dialog: {e}")
            import traceback
            traceback.print_exc()
