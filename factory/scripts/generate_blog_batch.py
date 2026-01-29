import os
import json
import sys

def load_config():
    """Load configuration from factory_config.json"""
    config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "factory_config.json"))
    if not os.path.exists(config_path):
        print(f"ERROR: Configuration file not found at {config_path}")
        sys.exit(1)
    
    with open(config_path, 'r') as f:
        return json.load(f)

config = load_config()
client = config.get("client", {})
brand = config.get("brand", {})

BUSINESS_NAME = client.get("name", "[BUSINESS_NAME]")
DOMAIN = client.get("domain", "[DOMAIN_NAME]")
PHONE = client.get("phone", "[PHONE_NUMBER]")
CLEAN_PHONE = "".join(filter(str.isdigit, PHONE))
PRIMARY_COLOR = brand.get("primary_color", "#0077be")

blog_template = f"""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{title}} | {BUSINESS_NAME}</title>
    <meta name="description" content="{{description}}">
    
    <!-- Open Graph -->
    <meta property="og:type" content="article">
    <meta property="og:url" content="https://{DOMAIN}/blog/{{slug}}/">
    <meta property="og:title" content="{{title}}">
    <meta property="og:description" content="{{description}}">
    <meta property="og:image" content="/images/hero-home.webp">

    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600&family=Poppins:wght@600;700;800&display=swap" rel="stylesheet">
    
    <!-- Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    
    <link rel="stylesheet" href="/css/styles.css?v=2.2">
    <link rel="icon" type="image/x-icon" href="/images/favicon.ico">
</head>

<body>

    <!-- Header -->
    <header>
        <div class="container">
            <a href="/" class="logo">{BUSINESS_NAME.split(' ')[0]} <span>{' '.join(BUSINESS_NAME.split(' ')[1:])}</span></a>
            <nav class="nav-menu">
                <ul>
                    <li><a href="/">Home</a></li>
                    <li><a href="/menu/">Menu</a></li>
                    <li><a href="/about/">About Us</a></li>
                    <li><a href="/blog/" class="active">Blog</a></li>
                    <li><a href="/news/">News</a></li>
                    <li><a href="/contact/">Contact</a></li>
                </ul>
            </nav>
            <div class="header-actions">
                <a href="tel:{CLEAN_PHONE}" class="phone-link mobile-hide"><i class="fas fa-phone"></i> {PHONE}</a>
                <a href="/contact/" class="btn btn-primary">Order Now</a>
                <button class="mobile-menu-btn" aria-label="Toggle navigation"><i class="fas fa-bars"></i></button>
            </div>
        </div>
    </header>

    <!-- Page Hero -->
    <section class="page-hero" style="background-image: linear-gradient(rgba(30, 127, 67, 0.9), rgba(20, 89, 45, 0.9)), url('/images/hero-home.webp'); padding: 80px 0; background-size: cover; background-position: center;">
        <div class="container" style="text-align: center;">
            <span style="color: #F7C948; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; font-size: 0.9rem;">{{category}}</span>
            <h1 style="color: white; font-size: 3rem; margin-top: 10px; max-width: 900px; margin-left: auto; margin-right: auto;">{{title}}</h1>
            <p style="color: rgba(255,255,255,0.9); margin-top: 15px;">Official Guide by {BUSINESS_NAME}</p>
        </div>
    </section>

    <!-- Content Section -->
    <section style="padding: 60px 0; background: #fdfdf5;">
        <div class="container" style="max-width: 800px;">
            <div class="blog-content" style="line-height: 1.8; color: #444; font-size: 1.1rem; background: #fff; padding: 40px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
                <p class="lead" style="font-size: 1.3rem; color: #1E7F43; font-weight: 600; margin-bottom: 30px;">
                    {{lead_text}}
                </p>
                
                {{content_body}}

                <div style="background: #f0faf4; padding: 30px; border-left: 5px solid #1E7F43; margin: 40px 0; border-radius: 4px;">
                    <h3 style="margin-top: 0; color: #1E7F43;">Ready to Order?</h3>
                    <p style="margin-bottom: 15px;">Skip the line and experience the fastest delivery in the Antelope Valley.</p>
                    <a href="tel:{CLEAN_PHONE}" class="btn btn-primary">Call {PHONE}</a>
                </div>

                <hr style="margin: 50px 0; border: 0; border-top: 1px solid #eee;">
                
                <div style="font-size: 0.9rem; color: #666;">
                    <p><strong>Tags:</strong> {{tags}}</p>
                    <p><a href="/blog/">&larr; Back to All Articles</a></p>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="aw-footer">
        <div class="container aw-footer-inner">
            <div class="aw-footer-brand">
                <h4 style="color: white; margin-bottom: 10px;">{BUSINESS_NAME}</h4>
                <p style="font-size: 0.9rem; opacity: 0.8; line-height: 1.6;">Your premier licensed mobile cannabis delivery service in the Antelope Valley. Fast, discreet, and reliable.</p>
            </div>
            <div class="aw-footer-locations">
                <h4 style="color: white; margin-bottom: 15px;">Products</h4>
                <ul style="list-style: none; padding: 0;">
                    <li><a href="/menu/cannabis/" style="color: #ccc; text-decoration: none;">Cannabis</a></li>
                    <li><a href="/menu/edibles/" style="color: #ccc; text-decoration: none;">Edibles</a></li>
                    <li><a href="/menu/vapes/" style="color: #ccc; text-decoration: none;">Vapes</a></li>
                    <li><a href="/menu/concentrates/" style="color: #ccc; text-decoration: none;">Concentrates</a></li>
                </ul>
            </div>
            <div class="aw-footer-locations">
                <h4 style="color: white; margin-bottom: 15px;">Resources</h4>
                <ul style="list-style: none; padding: 0;">
                    <li><a href="/blog/" style="color: #ccc; text-decoration: none;">Blog</a></li>
                    <li><a href="/news/" style="color: #ccc; text-decoration: none;">News Hub</a></li>
                    <li><a href="/about/" style="color: #ccc; text-decoration: none;">About Us</a></li>
                    <li><a href="/contact/" style="color: #ccc; text-decoration: none;">Support</a></li>
                    <li><a href="/delivery/" style="color: #ccc; text-decoration: none;">Delivery Areas</a></li>
                </ul>
            </div>
            <div class="aw-footer-contact">
                <h4 style="color: white; margin-bottom: 15px;">Contact</h4>
                <p class="aw-footer-phone"><a href="tel:{CLEAN_PHONE}" style="color: #F7C948; text-decoration: none; font-weight: 700;">{PHONE}</a></p>
                <p style="font-size: 0.9rem; color: #ccc; margin-top: 10px;">Daily: 10am – 10pm</p>
            </div>
        </div>
        <div class="aw-footer-bottom">
            <p>© 2026 {BUSINESS_NAME}. All rights reserved.</p>
        </div>
    </footer>
    <script src="/js/script.js"></script>
</body>
</html>
"""

articles = [
    {
        "slug": "ultimate-guide-to-cannabis-delivery-antelope-valley",
        "title": "The Ultimate Guide to Cannabis Delivery in Antelope Valley",
        "category": "Cornerstone Guide",
        "description": "Everything you need to know about legal marijuana delivery in Palmdale, Lancaster, and Rosamond. Learn about limits, ETAs, and top products.",
        "lead_text": "Navigating the world of cannabis delivery in the High Desert doesn't have to be complicated. Whether you're in Palmdale or Quartz Hill, here is your definitive guide to a seamless experience.",
        "tags": "Cannabis Delivery, Antelope Valley, Legal Weed, Guide",
        "content_body": '''
            <h2>Legality and Compliance</h2>
            <p>In California, cannabis delivery is fully legal for adults aged 21+ (or 18+ with a medical recommendation). Prop 64 paved the way for services like Cali-Bud Delivery to bring the dispensary directly to your door.</p>
            <h2>How It Works</h2>
            <p>1. Browse our real-time menu. 2. Place your order via phone or online. 3. Receive a discreet delivery at your residential address.</p>
            <h2>Service Areas</h2>
            <p>We proudly serve the entire Antelope Valley, including West Lancaster, East Palmdale, and the surrounding desert communities.</p>
        '''
    },
    {
        "slug": "palmdale-fastest-delivery-service",
        "title": "Why Cali-Bud is Palmdale's Fastest Delivery Service",
        "category": "Locality Anchor",
        "description": "Looking for weed delivery in Palmdale? Discover why our localized dispatch system ensures the fastest ETAs in the city.",
        "lead_text": "When you want your favorite strains, you shouldn't have to wait hours. Cali-Bud has optimized its Palmdale routes to ensure record-breaking delivery times.",
        "tags": "Palmdale Delivery, Fast Weed, Local Dispatch",
        "content_body": '''
            <h2>Localized Dispatch Tech</h2>
            <p>Unlike massive statewide corporations, we focus on the AV. Our drivers are already in Palmdale, meaning we don't have to fight freeway traffic to get to you.</p>
            <h2>Discreet and Professional</h2>
            <p>Our drivers prioritize your privacy. Unmarked vehicles and professional handlers ensure you get your delivery without drawing unwanted attention from the neighbors.</p>
        '''
    },
     {
        "slug": "is-weed-delivery-legal-palmdale",
        "title": "Is Weed Delivery Legal in Palmdale? (Compliance Guide)",
        "category": "Compliance Guide",
        "description": "Stay informed on the rules and regulations for cannabis delivery in Palmdale, CA. What you need to know about limits and ID requirements.",
        "lead_text": "Compliance is our priority. If you're wondering about the specific rules for ordering cannabis in Palmdale, this guide covers the essentials.",
        "tags": "Legal Updates, Palmdale Rules, Compliance",
        "content_body": '''
            <h2>Daily Purchase Limits</h2>
            <p>Under CA law, recreational users can purchase up to 28.5 grams of flower and 8 grams of concentrated cannabis per day.</p>
            <h2>Identification Requirements</h2>
            <p>A valid government-issued ID is required for every delivery. We cannot leave products without a physical verification of the recipient's age and identity.</p>
        '''
    }
]

def generate_articles():
    base_dir = "blog"
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
        
    for article in articles:
        article_dir = os.path.join(base_dir, article['slug'])
        if not os.path.exists(article_dir):
            os.makedirs(article_dir)
            
        html_content = blog_template.format(
            title=article['title'],
            description=article['description'],
            slug=article['slug'],
            category=article['category'],
            lead_text=article['lead_text'],
            content_body=article['content_body'],
            tags=article['tags']
        )
        
        file_path = os.path.join(article_dir, "index.html")
        with open(file_path, "w") as f:
            f.write(html_content)
        
        print(f"Generated: {file_path}")

if __name__ == "__main__":
    generate_articles()
