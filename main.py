from PyQt6 import QtWidgets, QtNetwork, QtCore
from src.controllers.auth_controller import LoginRegistrationController
from src.controllers.password_reset_controller import PasswordResetController
from src.services.auth.auth_service import AuthService
import sys
import threading
import queue
from urllib.parse import urlparse, parse_qs
from src.utils.url_handler import URLHandler
import os
import traceback
from src.utils.database.schema import Schema

sys.path.append('src')


def debug_monitor(debug_queue):
    """Monitor thread for debug messages"""
    while True:
        try:
            message = debug_queue.get(timeout=0.1)  # 100ms timeout
            print(f"DEBUG: {message}", file=sys.stderr, flush=True)
        except queue.Empty:
            continue
        except Exception as e:
            print(f"Monitor error: {e}", file=sys.stderr, flush=True)
            break


def handle_url_args():
    """Handle URL arguments for password reset"""
    print(f"Checking URL args: {sys.argv}")  # Debug print
    if len(sys.argv) > 1 and sys.argv[1].startswith('pyflora://'):
        url = urlparse(sys.argv[1])
        print(f"Parsed URL: {url}")  # Debug print
        if url.path == '/reset-password':
            query = parse_qs(url.query)
            token = query.get('token', [None])[0]
            print(f"Found reset token: {token}")  # Debug print
            return token
    return None


class SingleApplication(QtWidgets.QApplication):
    # Add signal for URL handling
    url_received = QtCore.pyqtSignal(str)

    def __init__(self, argv):
        super().__init__(argv)
        print("\n=== Initializing SingleApplication ===")
        self._server = QtNetwork.QLocalServer()
        self._socket = QtNetwork.QLocalSocket()
        self._main_window = None  # Store reference to main window

        # Define a fixed server name
        self.server_name = "PyFloraAppServer"

        # Remove any existing server
        print("Removing existing server...")
        QtNetwork.QLocalServer.removeServer(self.server_name)

        print(
            f"Attempting to connect to existing instance: {self.server_name}")
        self._socket.connectToServer(self.server_name)

        if self._socket.waitForConnected(500):
            print("Connected to existing instance")
            if len(sys.argv) > 1:
                print(f"Sending URL to existing instance: {sys.argv[1]}")
                self._socket.write(sys.argv[1].encode())
                self._socket.flush()
                self._socket.waitForBytesWritten(1000)
                print("Data sent to existing instance")
            sys.exit(0)
        else:
            print(f"\n=== Starting new instance ===")
            self._server.setSocketOptions(
                QtNetwork.QLocalServer.SocketOption.WorldAccessOption)
            if not self._server.listen(self.server_name):
                print(f"Server listen failed: {self._server.errorString()}")
            else:
                print(f"Server listening on: {self._server.serverName()}")
                self._server.newConnection.connect(self._handle_new_connection)

        # Connect URL signal to handler
        self.url_received.connect(self._handle_url_signal)

    def set_main_window(self, window):
        """Store reference to main window"""
        print(f"Setting main window reference: {window}")
        print(f"Window type: {type(window)}")
        print(f"Window is visible: {window.isVisible()}")
        self._main_window = window
        sys.stdout.flush()

    def _handle_new_connection(self):
        """Handle new connection in event loop"""
        print("\n" + "="*50)
        print("NEW CONNECTION RECEIVED")
        print("="*50)
        sys.stdout.flush()

        socket = self._server.nextPendingConnection()
        if socket.waitForReadyRead(1000):
            try:
                data = socket.readAll().data().decode()
                print(f"Received data in first instance: {data}")
                sys.stdout.flush()

                if data.startswith('pyflora://'):
                    print("Processing URL directly...")
                    sys.stdout.flush()

                    # Process URL directly in this method
                    token = URLHandler.parse_reset_url(data)
                    print(f"Parsed token result: {token}")

                    if token:
                        print(f"Found valid token: {token}")

                        if self._main_window:
                            print("Found main window, showing dialog...")

                            def show_dialog():
                                try:
                                    print("Preparing to show dialog...")
                                    self._main_window.show()
                                    self._main_window.raise_()
                                    self._main_window.activateWindow()

                                    print("Creating controllers...")
                                    password_reset_controller = PasswordResetController(
                                        self._main_window)

                                    print("Showing reset dialog...")
                                    password_reset_controller.show_reset_dialog(
                                        token)
                                    print("Dialog shown successfully")
                                except Exception as e:
                                    print(f"Error showing dialog: {e}")
                                    traceback.print_exc()
                                sys.stdout.flush()

                            # Execute in the main thread
                            print("Processing events and showing dialog...")
                            self.processEvents()  # Process any pending events
                            show_dialog()
                        else:
                            print("No main window found!")
                    else:
                        print("Token parsing failed")
                else:
                    print("Not a valid pyflora URL")
                sys.stdout.flush()
            except Exception as e:
                print(f"Error processing connection: {e}")
                traceback.print_exc()
                sys.stdout.flush()

    def _handle_url_signal(self, url):
        """Handle URL via signal"""
        print("\n" + "="*50)
        print(f"HANDLING URL SIGNAL: {url}")
        print("="*50)
        sys.stdout.flush()

        token = URLHandler.parse_reset_url(url)
        if not token:
            print("No valid token found")
            return

        print(f"Found token: {token}")
        sys.stdout.flush()

        try:
            print("\nAttempting to show dialog...")
            print(f"Main window: {self._main_window}")
            print(f"Is window visible: {self._main_window.isVisible()}")
            sys.stdout.flush()

            # Force window to be visible and active
            self._main_window.show()
            self._main_window.raise_()
            self._main_window.activateWindow()

            # Create controllers
            password_reset_controller = PasswordResetController(
                self._main_window)

            # Show dialog directly
            print("Showing reset dialog...")
            password_reset_controller.show_reset_dialog(token)
            print("Dialog shown successfully")
            sys.stdout.flush()
        except Exception as e:
            print(f"Error showing dialog: {str(e)}")
            import traceback
            traceback.print_exc()
            sys.stdout.flush()


def main():
    """Initialize and run the application."""
    try:
        # Initialize database schema first
        print("\nInitializing database schema...")
        schema = Schema()
        if not schema.create_tables():
            print("Failed to create database tables!")
            return
        print("Database schema initialized successfully")

        # Register URL scheme at startup
        URLHandler.register_url_scheme()

        app = SingleApplication(sys.argv)

        # Create and show the main window
        main_window = LoginRegistrationController()
        app.set_main_window(main_window)

        # Show the window
        main_window.show()
        main_window.raise_()
        main_window.activateWindow()

        # Process command line arguments
        if len(sys.argv) > 1:
            print(f"Checking URL args: {sys.argv[1:]}")
            token = URLHandler.parse_reset_url(sys.argv[1])
            print(f"Main: Got reset token: {token}")
            if token:
                app.handle_reset_token(token)

        sys.exit(app.exec())

    except Exception as e:
        print(f"Error in main: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
