from PyQt6 import QtWidgets
from src.views.ui.account_page_ui import Ui_AccountPage
from src.services.auth.auth_service import AuthService
from .change_password_dialog import ChangePasswordDialog


class AccountController(QtWidgets.QWidget):
    def __init__(self, auth_service, parent=None):
        super().__init__(parent)
        self.auth_service = auth_service
        self.ui = Ui_AccountPage()
        self.ui.setupUi(self)

        # Connect signals
        self.ui.change_pic_btn.clicked.connect(self._change_profile_picture)
        self.ui.delete_account_btn.clicked.connect(self._delete_account)
        self.ui.export_data_btn.clicked.connect(self._export_data)

        # Connect settings buttons - store references to buttons
        self.settings_buttons = {}
        for button in self.ui.settings_group.findChildren(QtWidgets.QPushButton):
            self.settings_buttons[button.text()] = button
            if button.text() == "Change Password":
                button.clicked.connect(self._show_change_password_dialog)

        # Initialize user data
        self._load_user_data()

    def _load_user_data(self):
        """Load user data into the UI"""
        try:
            user_data = self.auth_service.get_current_user_data()
            if user_data:
                self.ui.info_fields["Username:"].setText(
                    user_data.get("username", "N/A"))
                self.ui.info_fields["Email:"].setText(
                    user_data.get("email", "N/A"))
                self.ui.info_fields["Member Since:"].setText(
                    user_data.get("created_at", "N/A"))
                self.ui.info_fields["Last Login:"].setText(
                    user_data.get("last_login", "N/A"))
        except Exception as e:
            print(f"Error loading user data: {e}")

    def _change_profile_picture(self):
        """Handle profile picture change"""
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Select Profile Picture",
            "",
            "Image Files (*.png *.jpg *.jpeg)"
        )
        if file_name:
            # TODO: Implement profile picture update
            print(f"Selected file: {file_name}")

    def _delete_account(self):
        """Handle account deletion"""
        reply = QtWidgets.QMessageBox.question(
            self,
            'Delete Account',
            'Are you sure you want to delete your account? This action cannot be undone.',
            QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No,
            QtWidgets.QMessageBox.StandardButton.No
        )

        if reply == QtWidgets.QMessageBox.StandardButton.Yes:
            # TODO: Implement account deletion
            print("Account deletion requested")

    def _export_data(self):
        """Handle data export"""
        save_path, _ = QtWidgets.QFileDialog.getSaveFileName(
            self,
            "Export Data",
            "",
            "JSON Files (*.json)"
        )
        if save_path:
            # TODO: Implement data export
            print(f"Export data to: {save_path}")

    def _show_change_password_dialog(self):
        """Show the change password dialog."""
        print("Opening change password dialog...")  # Debug print
        dialog = ChangePasswordDialog(self.auth_service, self)
        dialog.exec()
