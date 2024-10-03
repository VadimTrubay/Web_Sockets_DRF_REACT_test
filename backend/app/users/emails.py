from djoser.email import (
    ActivationEmail,
    PasswordResetEmail,
    PasswordChangedConfirmationEmail,
    UsernameResetEmail,
    UsernameChangedConfirmationEmail,
)


class CustomActivationEmail(ActivationEmail):
    template_name = "email/activation.html"


class CustomPasswordResetEmail(PasswordResetEmail):
    template_name = "email/password_reset.html"


class CustomPasswordChangedConfirmationEmail(PasswordChangedConfirmationEmail):
    template_name = "email/password_reset_confirmation.html"


class CustomUsernameResetEmail(UsernameResetEmail):
    template_name = "email/username_reset.html"


class CustomUsernameChangedConfirmationEmail(UsernameChangedConfirmationEmail):
    template_name = "email/username_reset_confirmation.html"
