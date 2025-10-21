from app import create_app, db
from app.models import Product

app = create_app()
with app.app_context():
    db.create_all()
    p1 = Product(name="Durian Premium", price=25.0, description="Fresh durian")
    p2 = Product(name="Dragonfruit", price=15.0, description="Organic dragonfruit")
    db.session.add_all([p1, p2])
    db.session.commit()
    print("Sample products added!")
