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
    <title>{{title}} | {BUSINESS_NAME} News</title>
    <meta name="description" content="{{description}}">
    
    <!-- Open Graph -->
    <meta property="og:type" content="article">
    <meta property="og:url" content="https://{DOMAIN}/blog/{{slug}}/">
    <meta property="og:title" content="{{title}}">
    <meta property="og:description" content="{{description}}">
    <meta property="og:image" content="/images/logo-og.png">

    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600&family=Poppins:wght@600;700;800&display=swap" rel="stylesheet">
    
    <!-- Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    
    <link rel="stylesheet" href="/css/styles.css?v=1.0">
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
                    <li><a href="/services/">Services</a></li>
                    <li><a href="/about/">About Us</a></li>
                    <li><a href="/blog/" class="active">Blog</a></li>
                    <li><a href="/contact/">Contact</a></li>
                </ul>
            </nav>
            <div class="header-actions">
                <a href="tel:{CLEAN_PHONE}" class="phone-link mobile-hide"><i class="fas fa-phone"></i> {PHONE}</a>
                <a href="/contact/" class="btn btn-primary">Get Free Quote</a>
                <button class="mobile-menu-btn" aria-label="Toggle navigation"><i class="fas fa-bars"></i></button>
            </div>
        </div>
    </header>

    <!-- Page Hero -->
    <section class="page-hero" style="background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('/images/hero-bg.jpg'); padding: 80px 0; background-size: cover; background-position: center;">
        <div class="container" style="text-align: center;">
            <span style="color: #fff; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; font-size: 0.9rem;">{{category}}</span>
            <h1 style="color: white; font-size: 3rem; margin-top: 10px; max-width: 900px; margin-left: auto; margin-right: auto;">{{title}}</h1>
            <p style="color: rgba(255,255,255,0.9); margin-top: 15px;">Published by {BUSINESS_NAME}</p>
        </div>
    </section>

    <!-- Content Section -->
    <section style="padding: 60px 0; background: #fff;">
        <div class="container" style="max-width: 800px;">
            <div class="blog-content" style="line-height: 1.8; color: #444; font-size: 1.1rem;">
                <p class="lead" style="font-size: 1.3rem; color: {PRIMARY_COLOR}; font-weight: 600; margin-bottom: 30px;">
                    {{lead_text}}
                </p>
                
                {{content_body}}

                <div style="background: #f8f9fa; padding: 30px; border-left: 5px solid {PRIMARY_COLOR}; margin: 40px 0; border-radius: 4px;">
                    <h3 style="margin-top: 0; color: {PRIMARY_COLOR};">Ready to Get Started?</h3>
                    <p style="margin-bottom: 15px;">Contact us today for a free professional consultation.</p>
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
            <div class="aw-footer-brand" style="margin-bottom: 30px;">
                <h4 style="color: white;">{BUSINESS_NAME}</h4>
                <p style="opacity: 0.8; line-height: 1.6;">Your trusted professional service provider. Quality craftsmanship, reliable service.</p>
            </div>
            <div class="aw-footer-contact">
                <h4 style="color: white; margin-bottom: 15px;">Contact Us</h4>
                <p class="aw-footer-phone"><a href="tel:{CLEAN_PHONE}">{PHONE}</a></p>
            </div>
        </div>
        <div class="aw-footer-bottom">
            <p>© {BUSINESS_NAME}. All rights reserved. | <a href="/privacy/">Privacy Policy</a></p>
        </div>
    </footer>
    <script src="/js/script.js"></script>
</body>
</html>
"""

articles = [
    {
        "slug": "5-signs-your-refrigerator-needs-repair",
        "title": "5 Signs Your Refrigerator Needs Repair immediately",
        "category": "Refrigerator Repair",
        "description": "Is your fridge making noise or not cooling? Learn the 5 warning signs that indicate you need professional refrigerator repair in the Antelope Valley.",
        "lead_text": "A broken refrigerator can lead to spoiled food and costly waste. Recognizing the early signs of failure can save you hundreds of dollars.",
        "tags": "Refrigerator Repair, Troubleshooting, Maintenance",
        "content_body": '''
            <h2>1. Food Spoilage</h2>
            <p>If you notice your milk is going bad before its expiration date, or your veggies are wilting quickly, your fridge might struggle to maintain the correct temperature.</p>
            <h2>2. Excessive Condensation</h2>
            <p>Water pooling at the bottom of your fridge or droplets on the shelves indicates a cooling system failure or a worn door seal.</p>
            <h2>3. Motor running Constantly</h2>
            <p>Your refrigerator motor shouldn't run 24/7. If it is high-speed cycling or never shutting off, it's overworked and near failure.</p>
            <h2>4. Strange Noises</h2>
            <p>Buzzing, humming, or clicking sounds are often signs of a failing compressor or condenser fan.</p>
            <h2>5. Freezer is Icing Over</h2>
            <p>If your freezer looks like a winter wonderland, the defrost heater or timer might be broken.</p>
        '''
    },
    {
        "slug": "why-is-my-washer-not-spinning",
        "title": "Why Is My Washer Not Spinning? Common Causes",
        "category": "Washer Repair",
        "description": "Washer filling with water but not spinning? Discover the common causes behind this issue and when to call a pro.",
        "lead_text": "There's nothing worse than opening your washer to find a soaking wet pile of laundry. Here is why your machine might be refusing to spin.",
        "tags": "Washer Repair, DIY Tips, Laundry Appliances",
        "content_body": '''
            <h2>Lid Switch Assembly</h2>
            <p>The most common culprit is a broken lid switch. If the machine thinks the lid is open, it won't spin for safety reasons.</p>
            <h2>Drive Belt</h2>
            <p>On top-loaders, a loose or broken drive belt will prevent the drum from turning, even if the motor is running.</p>
            <h2>Worn Clutch</h2>
            <p>Just like a car, your washer has a clutch. If it wears out, the tub won't get up to speed.</p>
            <h2>Drain Pump Blockage</h2>
            <p>If the water can't drain, the safety cycle will prevent the spin. Check your filter for coins or socks!</p>
        '''
    },
     {
        "slug": "dryer-not-heating-troubleshooting",
        "title": "Dryer Running But Not Heating? Here's Why",
        "category": "Dryer Repair",
        "description": "Is your dryer tumbling but leaving clothes damp? It could be a thermal fuse, heating element, or vent issue.",
        "lead_text": "A dryer that doesn't heat is just a large, expensive fan. Before you buy a new one, check these common failure points.",
        "tags": "Dryer Repair, Heating Issues, Fire Safety",
        "content_body": '''
            <h2>1. Clogged Vent Line</h2>
            <p><strong>Safety Warning:</strong> A clogged dryer vent is a major fire hazard. It also causes the thermal fuse to blow, cutting off heat.</p>
            <h2>2. Broken Heating Element</h2>
            <p>Over time, the heating coil can burn out. This is a routine repair for our technicians.</p>
            <h2>3. Thermal Fuse</h2>
            <p>This safety device cuts power to the heater if the dryer gets too hot. If it blows, it needs to be replaced (and the blockage cleared!).</p>
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
