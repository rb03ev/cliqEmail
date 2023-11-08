import click
from account import register_user, login_user
from send_grid import send_email
from authenticate import authenticate_email


@click.group()
def cli():
    pass

# USAGE: python3 app.py --help
# USAGE: python3 app.py user --help
# USAGE: python3 app.py user --register || python3 app.py user --login


@cli.command()
@click.option("--register", is_flag=True, help="Enter username, password and email")
@click.option("--login", is_flag=True, help="Enter username and password")
def user(register, login):

    # -- Register User -- #
    if register_user:
        # Prompt user to enter details for registration
        click.confirm("Would you like to register?")

        username = click.prompt("Enter your username")
        email = click.prompt("Enter your email address")
        password = click.prompt(
            "Enter your password", hide_input=True, confirmation_prompt=True)

        # Authenticate the email
        auth_email = authenticate_email(email)

        # --- Confirm if registration is successful -- #
        success = register_user(username, auth_email, password)

        if success:
            click.echo("You have successfully registered")
        else:
            click.echo(
                "Registration failed. The username or email might already be in use.")

        # Store user data
        data = [{username, email, password}]
        user_data = [datum for datum in data if not None]
        print(user_data)

    # -- Login User -- #
    elif login:
        click.confirm("Would you like to login?")
        # Prompt the user for login credentials
        username = click.prompt("Enter your username")
        password = click.prompt("Enter your password", hide_input=True)

        # Log in the user
        login_success = login_user(username, password)

        if login_success:
            click.echo(f"Welcome {username}.")
            send()
        else:
            click.echo("Login failed. Please check your credentials")


# Define command to send emails via SendGrid
# USAGE: python3 app.py send --send_mail
@cli.command()
@click.option("--send_mail", is_flag=True, help="Send an email")
@click.option("--email_address", is_flag=True, help="Enter email address.")
@click.option("--subject", is_flag=True, help="Enter content subject")
@click.option("--content", is_flag=True, help="Enter message to send")
def send(send_mail, email_address, subject, content):

    # Ask if user wants to send an email
    send_mail = click.confirm("Would you like to send an email?")
    if send_mail:
        click.prompt("Enter recipient's email address")
        click.prompt("Enter the subject for this email")
        click.prompt("Enter the content or message you would like to send")

        if email_address is not None:
            if authenticate_email(email_address):
                # Send message via SendGrid
                send_email(email_address, subject, content)
                click.echo("Email sent successfully.")
            else:
                click.echo("Invalid email address: {email_address}")
        else:
            click.echo("Please provide an email address")


r = cli()
if __name__ == "__main__":
    print(r)
