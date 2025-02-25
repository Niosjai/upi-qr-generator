from flask import Flask, render_template, request
import qrcode
from io import BytesIO
import base64
from urllib.parse import quote

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_qr():
    # Get form data
    upi_id = request.form.get('upi_id')
    merchant_name = request.form.get('merchant_name')
    amount = request.form.get('amount')
    note = request.form.get('note', 'Payment')

    # Validate required fields
    if not all([upi_id, merchant_name, amount]):
        return "All fields are required", 400

    # URL encode parameters
    upi_id_encoded = quote(upi_id)
    merchant_name_encoded = quote(merchant_name)
    note_encoded = quote(note)

    # Create UPI payment URI
    upi_uri = f"upi://pay?pa={upi_id_encoded}&pn={merchant_name_encoded}&am={amount}&tn={note_encoded}"

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(upi_uri)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Convert image to base64
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()

    return render_template('result.html', 
                         qr_code=img_str,
                         merchant_name=merchant_name,
                         upi_id=upi_id,
                         amount=amount)

if __name__ == '__main__':
    app.run(debug=True)