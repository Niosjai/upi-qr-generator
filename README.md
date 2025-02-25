# UPI QR Code Generator

This project provides a Python-based solution to generate QR codes for UPI payments. Users can input their UPI ID, recipient name, amount, and a transaction note to create a scannable QR code for seamless payments.

## Features

- Generate UPI payment QR codes with customizable parameters.
- Save the generated QR code as an image file.
- Compatible with all UPI-supported applications.

## Requirements

Ensure you have the following installed:

- Python 3.x
- Required Python packages listed in `requirements.txt`

Install the necessary packages using:

```bash
pip install -r requirements.txt
```

## Usage

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Niosjai/upi-qr-generator.git
   cd upi-qr-generator
   ```

2. **Run the Application**:

   Execute the following command to start the application:

   ```bash
   python app.py
   ```

3. **Generate a QR Code**:

   - Input your UPI ID, recipient name, amount, and transaction note as prompted.
   - The application will generate and save a QR code image in the project directory.

## How It Works

The application constructs a UPI payment URL with the provided parameters:

```
upi://pay?pa=UPI_ID&pn=Recipient_Name&am=Amount&tn=Transaction_Note
```

This URL is then encoded into a QR code using the `qrcode` library. Scanning this QR code with any UPI-compatible app will initiate the payment with the specified details.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
