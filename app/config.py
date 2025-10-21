class Config:
    SECRET_KEY = 'secretkey'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///shop.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # PayNet FPX sandbox
    PAYNET_FPX_MERCHANT_ID = 'sandbox_merchant'
    PAYNET_FPX_API_URL = 'https://sandbox.fpx.paynet.com.my/payment'
    PAYNET_FPX_RETURN_URL = 'http://127.0.0.1:5000/success'
