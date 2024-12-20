import unittest
from src.services.auth.auth_service import AuthService
from src.utils.database.user_data_handler import UserDataHandler
from src.utils.database.schema import Schema
import time


class TestPasswordReset(unittest.TestCase):
    def setUp(self):
        """Set up test environment before each test."""
        self.schema = Schema()
        self.auth_service = AuthService()
        self.auth_service.test_mode = True  # Add test mode flag
        self.user_data = UserDataHandler()

        # Reset database and create fresh tables
        self.schema.reset_database()

        # Test user data
        self.test_username = "testuser"
        self.test_email = "test@example.com"
        self.test_password = "TestPassword123!"

        # Register a test user
        self.auth_service.register(
            self.test_username,
            self.test_password,
            self.test_email
        )

    def test_password_reset_flow(self):
        """Test the complete password reset flow."""
        # 1. Verify email exists
        self.assertTrue(
            self.user_data.email_exists(self.test_email),
            "Test email should exist in database"
        )

        # 2. Send reset email
        result = self.auth_service.send_reset_email(self.test_email)
        self.assertTrue(result, "Should send reset email successfully")

        # 3. Get the token (in real scenario this would be from email)
        token = None
        for t in self.auth_service.reset_tokens:
            if self.auth_service.reset_tokens[t]['email'] == self.test_email:
                token = t
                break

        self.assertIsNotNone(token, "Should have generated a reset token")

        # 4. Verify token
        is_valid, email = self.auth_service.verify_reset_token(token)
        self.assertTrue(is_valid, "Token should be valid")
        self.assertEqual(email, self.test_email,
                         "Token should be associated with correct email")

        # 5. Reset password
        new_password = "NewTestPassword123!"
        reset_success = self.auth_service.reset_password(token, new_password)
        self.assertTrue(reset_success, "Password reset should succeed")

        # 6. Try logging in with new password
        login_success, _ = self.auth_service.login(
            self.test_username, new_password)
        self.assertTrue(
            login_success, "Should be able to login with new password")

        # 7. Verify old token is invalidated
        is_valid, _ = self.auth_service.verify_reset_token(token)
        self.assertFalse(is_valid, "Old token should be invalidated")

    def test_invalid_email(self):
        """Test password reset with invalid email."""
        result = self.auth_service.send_reset_email("nonexistent@example.com")
        self.assertFalse(result, "Should fail for non-existent email")

    def test_token_expiration(self):
        """Test token expiration."""
        # Send reset email
        self.auth_service.send_reset_email(self.test_email)

        # Get the token
        token = next(iter(self.auth_service.reset_tokens))

        # Modify expiration time to be in the past
        self.auth_service.reset_tokens[token]['expiry'] = \
            self.auth_service.reset_tokens[token]['expiry'].replace(year=2000)

        # Verify token
        is_valid, _ = self.auth_service.verify_reset_token(token)
        self.assertFalse(is_valid, "Expired token should be invalid")

    def test_multiple_reset_requests(self):
        """Test handling of multiple reset requests."""
        # Send first reset email
        self.auth_service.send_reset_email(self.test_email)
        first_token = next(iter(self.auth_service.reset_tokens))

        # Wait a moment to ensure different timestamps
        time.sleep(1)

        # Send second reset email
        self.auth_service.send_reset_email(self.test_email)
        second_token = next(iter(self.auth_service.reset_tokens))

        # Verify tokens are different
        self.assertNotEqual(first_token, second_token,
                            "Second token should be different from first")

        # Try to verify first token (should fail as it's invalidated)
        is_valid, _ = self.auth_service.verify_reset_token(first_token)
        self.assertFalse(is_valid, "First token should be invalidated")

        # Verify second token is valid
        is_valid, email = self.auth_service.verify_reset_token(second_token)
        self.assertTrue(is_valid, "Second token should be valid")
        self.assertEqual(email, self.test_email,
                         "Token should be associated with correct email")

    def tearDown(self):
        """Clean up after each test."""
        self.schema.reset_database()


if __name__ == '__main__':
    unittest.main()
