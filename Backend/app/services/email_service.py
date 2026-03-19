import aiosmtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.config import get_settings

settings = get_settings()

async def send_email(to_email: str, subject: str, html_body: str):
    message = MIMEMultipart("alternative")
    message["From"] = settings.SMTP_USER
    message["To"] = to_email
    message["Subject"] = subject

    message.attach(MIMEText(html_body, "html"))

    await aiosmtplib.send(
        message,
        hostname=settings.SMTP_HOST,
        port=settings.SMTP_PORT,
        username=settings.SMTP_USER,
        password=settings.SMTP_PASSWORD,
        start_tls=True
    )


async def notify_owner(contact):
    subject = f"New Contact Form Submission from {contact.name}"

    html_body = f"""
    <h2>New Contact Form Submission</h2>
    <p><strong>Name:</strong> {contact.name}</p>
    <p><strong>Email:</strong> {contact.email}</p>
    <p><strong>Phone:</strong> {contact.phone}</p>
    <p><strong>Service:</strong> {contact.service}</p>
    <p><strong>Message:</strong><br>{contact.message}</p>
    """
    await send_email(settings.OWNER_EMAIL, subject, html_body)


async def send_confirmation(contact):
    subject = "Thank you for contacting us!"
    html_body = f"""
    <h2>Thank you for reaching out, {contact.name}!</h2>
    <p>We have received your message regarding "{contact.service}" and will get back to you shortly.</p>
    <p>Best regards,<br>The Cabnet Team</p>
    """
    await send_email(contact.email, subject, html_body)
