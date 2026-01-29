
import os

blog_template = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Cali-Bud Delivery News</title>
    <meta name="description" content="{description}">
    <link rel="canonical" href="https://d3jg5wepg4zxcs.cloudfront.net/blog/{slug}/" />
    
    <!-- Open Graph -->
    <meta property="og:type" content="article">
    <meta property="og:url" content="https://d3jg5wepg4zxcs.cloudfront.net/blog/{slug}/">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:image" content="/images/hero-home.webp">

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
            <a href="/" class="logo">Mobile <span>Marijuana Delivery</span></a>
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
                <a href="tel:6614984444" class="phone-link mobile-hide"><i class="fas fa-phone"></i> 661-498-4444</a>
                <a href="/contact/" class="btn btn-primary">Book Repair</a>
                <button class="mobile-menu-btn" aria-label="Toggle navigation"><i class="fas fa-bars"></i></button>
            </div>
        </div>
    </header>

    <!-- Page Hero -->
    <section class="page-hero" style="background-image: linear-gradient(rgba(31, 106, 225, 0.9), rgba(0, 68, 136, 0.9)); padding: 80px 0; background-size: cover; background-position: center;">
        <div class="container" style="text-align: center;">
            <span style="color: #b0e0e6; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; font-size: 0.9rem;">{category}</span>
            <h1 style="color: white; font-size: 3rem; margin-top: 10px; max-width: 900px; margin-left: auto; margin-right: auto;">{title}</h1>
            <p style="color: rgba(255,255,255,0.9); margin-top: 15px;">Published by Cali-Bud Delivery Service</p>
        </div>
    </section>

    <!-- Content Section -->
    <section style="padding: 60px 0; background: #fff;">
        <div class="container" style="max-width: 800px;">
            <div class="blog-content" style="line-height: 1.8; color: #444; font-size: 1.1rem;">
                <p class="lead" style="font-size: 1.3rem; color: #1F6AE1; font-weight: 600; margin-bottom: 30px;">
                    {lead_text}
                </p>
                
                {content_body}

                <div style="background: #f0faff; padding: 30px; border-left: 5px solid #1F6AE1; margin: 40px 0; border-radius: 4px;">
                    <h3 style="margin-top: 0; color: #1F6AE1;">Need Expert Help?</h3>
                    <p style="margin-bottom: 15px;">We serve Palmdale, Lancaster, and Quartz Hill with same-day repairs.</p>
                    <a href="tel:6614984444" class="btn btn-primary">Call 661-498-4444</a>
                </div>

                <hr style="margin: 50px 0; border: 0; border-top: 1px solid #eee;">
                
                <div style="font-size: 0.9rem; color: #666;">
                    <p><strong>Tags:</strong> {tags}</p>
                    <p><a href="/blog/">&larr; Back to All Articles</a></p>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="aw-footer">
        <div class="container aw-footer-inner">
            <div class="aw-footer-brand">
                <h4 style="color: white; margin-bottom: 15px;">Cali-Bud Delivery</h4>
                <p>Your trusted appliance repair provider in the Antelope Valley.</p>
            </div>
            <div class="aw-footer-contact">
                <h4 style="color: white; margin-bottom: 15px; font-size: 1.1rem;">Contact Us</h4>
                <p class="aw-footer-phone"><a href="tel:6614984444">661-498-4444</a></p>
            </div>
        </div>
         <div class="aw-footer-neighborhoods" style="margin-top: 20px; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 20px;">
            <h4 style="font-size: 0.9rem; color: #aaa; margin-bottom: 10px;">Neighborhoods Served</h4>
            <p style="font-size: 0.8rem; color: #888; line-height: 1.6;">
                West Lancaster • East Palmdale • Quartz Hill • Rancho Vista • Anaverde • Sun Village • 
                Littlerock • Pearblossom • Lake Los Angeles • Leona Valley • Rosamond • Antelope Acres • 
                White Fence Farms • Desert View Highlands • Joshua Ranch
            </p>
        </div>
        <div class="aw-footer-bottom">
            <p>© 2026 Cali-Bud Delivery Service. All rights reserved.</p>
        </div>
    </footer>
    <script src="/js/script.js"></script>
</body>
</html>
"""

articles = [
    {
        "slug": "hard-water-effects-palmdale-dishwashers",
        "title": "Hard Water in Palmdale: Is It Killing Your Dishwasher?",
        "category": "Local Guide",
        "description": "The Antelope Valley has hard water. Learn how mineral buildup affects your dishwasher and how to prevent costly breakdowns.",
        "lead_text": "Palmdale residents know that hard water is a fact of life here. But did you know those mineral deposits are silently damaging your dishwasher's pump and spray arms?",
        "tags": "Dishwasher Repair, Hard Water, Palmdale, Maintenance",
        "content_body": '''
            <h2 style="color: #1F6AE1; margin-top: 40px; margin-bottom: 20px;">The White Film Problem</h2>
            <p>If your glasses are coming out cloudy, it's not soap scum—it's limescale. In Palmdale, calcium and magnesium levels in the water are high. Over time, this builds up inside the heating element and water inlet valve.</p>
            
            <h2 style="color: #1F6AE1; margin-top: 40px; margin-bottom: 20px;">Preventing Damage</h2>
            <p>We recommend running a citric acid-based dishwasher cleaner once a month. This dissolves the minerals before they turn into rock-hard deposits that block water flow.</p>

            <h2 style="color: #1F6AE1; margin-top: 40px; margin-bottom: 20px;">When to Call a Pro</h2>
            <p>If your dishwasher is making a grinding noise or not draining, the buildup may have already damaged the impeller. Our technicians in Palmdale carry specialized tools to descale and repair these components.</p>
        '''
    },
    {
        "slug": "power-surges-lancaster-refrigerators",
        "title": "Protecting Your Fridge from Power Surges in Lancaster",
        "category": "Technical Advice",
        "description": "Lancaster experiences frequent wind-driven power fluctuations. Learn how to protect your refrigerator's control board.",
        "lead_text": "High winds in Lancaster often lead to flickering lights and power surges. For modern refrigerators with sensitive digital control boards, these surges can be fatal.",
        "tags": "Refrigerator Repair, Power Surge, Lancaster, Prevention",
        "content_body": '''
            <h2 style="color: #1F6AE1; margin-top: 40px; margin-bottom: 20px;">The Silent Killer of Control Boards</h2>
            <p>Modern Samsung, LG, and Whirlpool fridges are essentially computers that keep your food cold. A sudden spike in voltage can fry the motherboard, leading to a 'dead' fridge or error codes.</p>
            
            <h2 style="color: #1F6AE1; margin-top: 40px; margin-bottom: 20px;">Surge Protector Solutions</h2>
            <p>We highly recommend installing a specialized appliance surge protector behind your refrigerator. Unlike standard power strips, these are designed to handle the high amperage of a compressor startup while clamping down on voltage spikes.</p>

            <h2 style="color: #1F6AE1; margin-top: 40px; margin-bottom: 20px;">Did Your Power Just Go Out?</h2>
            <p>If your power returned but your fridge didn't, don't panic. Unplug it for 5 minutes to reset the internal computer. If it still doesn't start, the relay or board may be damaged. Call us for a diagnostic.</p>
        '''
    },
    {
        "slug": "why-quartz-hill-chooses-mobile-repair",
        "title": "Why Quartz Hill Residents Trust Us for Repairs",
        "category": "Community Spotlight",
        "description": "From 60th West to the Hill, we provide fast, neighborhood-focused appliance repair services for Quartz Hill families.",
        "lead_text": "Quartz Hill is a unique community with a mix of ranch properties and modern homes. We understand the specific needs of our neighbors on the Hill.",
        "tags": "Quartz Hill, Local Business, Marijuana Delivery, Community",
        "content_body": '''
            <h2 style="color: #1F6AE1; margin-top: 40px; margin-bottom: 20px;">We Know the Area</h2>
            <p>We don't need GPS to find 60th Street West. Being local means we don't charge excessive travel fees just to get to your house. We are your neighbors.</p>
            
            <h2 style="color: #1F6AE1; margin-top: 40px; margin-bottom: 20px;">Ranch Properties & Second Fridges</h2>
            <p>Many homes in Quartz Hill have a second fridge or freezer in the garage. These units work harder in the summer heat and require specific maintenance checks. We specialize in garage-ready refrigerator repair.</p>

            <h2 style="color: #1F6AE1; margin-top: 40px; margin-bottom: 20px;">Same-Day Availability</h2>
            <p>Because our trucks are already in the area, we can often fit you in on the same day you call. Don't wait three days for a technician driving up from LA.</p>
        '''
    }
]

def generate_articles():
    base_dir = "blog"
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
        
    for article in articles:
        # Create directory
        article_dir = os.path.join(base_dir, article['slug'])
        if not os.path.exists(article_dir):
            os.makedirs(article_dir)
            
        # Create HTML
        html_content = blog_template.format(
            title=article['title'],
            description=article['description'],
            slug=article['slug'],
            category=article['category'],
            lead_text=article['lead_text'],
            content_body=article['content_body'],
            tags=article['tags']
        )
        
        # Write file
        file_path = os.path.join(article_dir, "index.html")
        with open(file_path, "w") as f:
            f.write(html_content)
        
        print(f"Generated: {file_path}")

if __name__ == "__main__":
    generate_articles()
