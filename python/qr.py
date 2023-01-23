from flask import Flask, request, make_response
from io import BytesIO
import qrcode

app = Flask(__name__)

@app.route('/qr-code', methods=['GET'])
def qr_code():
    url = request.args.get('url')
    if not url:
        return make_response('Missing "url" parameter', 400)
    img = qrcode.make(url)
    # Save image data to a BytesIO object
    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)

    response = make_response(img_io.read())
    response.content_type = 'image/png'
    return response

if __name__ == '__main__':
    app.run(debug=True)
