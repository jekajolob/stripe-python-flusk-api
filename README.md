# Stripe Payment Integration with Flask

A simple and secure payment integration using Stripe Checkout and Flask. This project demonstrates how to implement a payment system with features like success and cancel handling.

## Features

- 💳 Secure payment processing with Stripe Checkout
- 🔒 PCI compliant
- 📱 Responsive design
- 🌐 Support for multiple payment methods
- ✨ Custom success and cancel pages
- 🔄 Webhook integration for order fulfillment

## Prerequisites

- Python 3.x
- Flask
- Stripe account and API keys
- Virtual environment (recommended)

## Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
cd stripe-python-flask-api
```

2. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install flask stripe python-dotenv
```

4. Create a `.env` file in the project root and add your Stripe keys:

```
API_SECRET_KEY=your_stripe_secret_key_here
```

## Project Structure

```
stripe-python-flask-api/
├── app.py                 # Main Flask application
├── static/               # Static files (images, etc.)
│   └── Stripe_Logo.png
├── templates/            # HTML templates
│   ├── index.html       # Main checkout page
│   ├── success.html     # Success page
│   └── cancel.html      # Cancel page
├── .env                 # Environment variables
└── README.md           # This file
```

## Usage

1. Start the Flask server:

```bash
python app.py
```

2. Open your browser and navigate to:

```
http://localhost:4242
```

3. Click the "Buy" button to test the payment flow

## Webhook Setup

For local development:

1. Install the [Stripe CLI](https://stripe.com/docs/stripe-cli)
2. Run webhook forwarding:

```bash
stripe listen --forward-to localhost:4242/webhook
```

## Testing

Use Stripe's test cards to verify the integration:

- Successful payment: 4242 4242 4242 4242
- Failed payment: 4000 0000 0000 0002

## Security Notes

- Never commit your Stripe secret key
- Always use environment variables for sensitive data
- Keep your dependencies updated
- Use HTTPS in production

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please refer to:

- [Stripe Documentation](https://stripe.com/docs)
- [Flask Documentation](https://flask.palletsprojects.com/)
- Create an issue in this repository

## Acknowledgments

- Stripe for their excellent payment processing platform
- Flask team for the web framework
- All contributors to this project
