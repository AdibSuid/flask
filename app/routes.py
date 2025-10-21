from flask import Blueprint, render_template, request, jsonify

main = Blueprint('main', __name__)

# Dynamic content
services = [
    {"title": "AI Development", "desc": "Custom AI solutions including NLP, Computer Vision, and ML models."},
    {"title": "Software Development", "desc": "Web, Mobile, and Desktop applications tailored to your business needs."},
    {"title": "Cloud & DevOps", "desc": "Scalable cloud infrastructure and DevOps pipelines for rapid deployment."},
    {"title": "Data Analytics", "desc": "Data-driven insights to optimize decision-making and efficiency."}
]

portfolio = [
    {"title": "AI Chatbot", "category": "ai", "image": "images/portfolio1.jpg", "desc": "Smart AI chatbot for customer support."},
    {"title": "E-commerce Platform", "category": "software", "image": "images/portfolio2.jpg", "desc": "Full-featured online store."},
    {"title": "IoT Analytics Dashboard", "category": "ai", "image": "images/portfolio3.jpg", "desc": "Real-time IoT data visualization."},
    {"title": "Automation App", "category": "software", "image": "images/portfolio4.jpg", "desc": "Custom automation software for businesses."}
]

team = [
        {"name": "Meow", "role": "CEO & Founder", "image": "images/team1.jpg",
         "bio": "Visionary leader driving innovation and growth."},
        {"name": "Ashraf Zulhelmi", "role": "Chief Technology Officer", "image": "images/team2.jpg",
         "bio": "Expert in AI and scalable cloud solutions."},
        {"name": "Afiq Zawawi", "role": "Chief Finance Officer", "image": "images/team3.jpg",
         "bio": "Overseeing accounting, managing cash flow, and analyzing financial data."},
        {"name": "Fadhlul Wafi", "role": "Lead Software Engineer", "image": "images/team4.jpg",
         "bio": "Crafts impactful brand narratives and campaigns."},
        {"name": "Eiman Azzam", "role": "Software Engineer", "image": "images/team5.jpg",
         "bio": "Architect of robust backend and microservices."},
        {"name": "Hanis Izani", "role": "Project Engineer", "image": "images/team6.jpg",
         "bio": "Transforms data into actionable business insights."},
        {"name": "Naufal Bakri", "role": "AI Research Engineer", "image": "images/team7.jpg",
         "bio": "Develops machine learning and NLP solutions."},
        {"name": "Zulhilmi", "role": "Robotics Engineer", "image": "images/team8.jpg",
         "bio": "Designs intuitive and delightful digital interfaces."},
        {"name": "Hamzah Faisal", "role": "DevOps Engineer", "image": "images/team9.jpg",
         "bio": "Ensures smooth deployment and reliable infrastructure."},
    ]

@main.route('/')
def index():
    return render_template('index.html', services=services, portfolio=portfolio, team=team)

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/services')
def services_page():
    return render_template('services.html', services=services)

@main.route('/portfolio')
def portfolio_page():
    return render_template('portfolio.html', portfolio=portfolio)

@main.route('/team')
def team_page():
    return render_template('team.html', team=team)

@main.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.form
        # Here you can integrate an email API (SendGrid, SMTP, etc.)
        print(f"New message from {data['name']} ({data['email']}): {data['message']}")
        return jsonify({"status": "success", "message": "Your message has been sent!"})
    return render_template('contact.html')

@main.route('/api/services')
def api_services():
    return jsonify(services)
