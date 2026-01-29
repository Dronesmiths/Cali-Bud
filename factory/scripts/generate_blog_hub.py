
import os
import re

def get_article_meta(filepath):
    """Extracts title and description from an HTML file."""
    try:
        with open(filepath, 'r') as f:
            content = f.read()
            
        title_match = re.search(r'<title>(.*?) \|', content)
        desc_match = re.search(r'<meta name="description" content="(.*?)">', content)
        
        title = title_match.group(1) if title_match else "Untitled Article"
        description = desc_match.group(1) if desc_match else "No description available."
        
        return title, description
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return None, None

def generate_hub():
    base_dir = "blog"
    articles = []
    
    # Scan for articles
    if os.path.exists(base_dir):
        for item in os.listdir(base_dir):
            article_dir = os.path.join(base_dir, item)
            index_path = os.path.join(article_dir, "index.html")
            
            if os.path.isdir(article_dir) and os.path.exists(index_path):
                title, description = get_article_meta(index_path)
                if title:
                    articles.append({
                        "slug": item,
                        "title": title,
                        "description": description
                    })
    
    # HTML Template
    html_start = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cannabis Culture & News | Cali-Bud Delivery</title>
    <meta name="description" content="Stay informed with the latest cannabis news, product guides, and delivery tips for the Antelope Valley.">
    <link rel="canonical" href="https://calibud.club/blog/" />
    
    <!-- Open Graph -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://calibud.club/blog/">
    <meta property="og:title" content="Cannabis Culture & News | Cali-Bud Delivery">
    <meta property="og:description" content="Stay informed with the latest cannabis news, product guides, and delivery tips.">
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
            <a href="/" class="logo">Cali-Bud <span>Delivery</span></a>
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
                <a href="tel:6615472422" class="phone-link mobile-hide"><i class="fas fa-phone"></i> 661-547-2422</a>
                <a href="/contact/" class="btn btn-primary">Order Now</a>
                <button class="mobile-menu-btn" aria-label="Toggle navigation"><i class="fas fa-bars"></i></button>
            </div>
        </div>
    </header>

    <!-- Page Hero -->
    <section class="page-hero" style="background-image: linear-gradient(rgba(30, 127, 67, 0.9), rgba(20, 89, 45, 0.9)); padding: 80px 0; background-size: cover; background-position: center;">
        <div class="container" style="text-align: center;">
            <span style="color: #F7C948; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; font-size: 0.9rem;">The Green Room</span>
            <h1 style="color: white; font-size: 3rem; margin-top: 10px; max-width: 900px; margin-left: auto; margin-right: auto;">Cannabis Tips & News</h1>
            <p style="color: rgba(255,255,255,0.9); margin-top: 15px;">Education, strain reviews, and industry updates.</p>
        </div>
    </section>

    <!-- Blog Grid -->
    <section style="padding: 60px 0; background: #fdfdf5;">
        <div class="container">
            <div class="features-grid grid-balance-3">
"""

    html_end = """
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="aw-footer">
        <div class="container aw-footer-inner">
            <div class="aw-footer-brand">
                <h4 style="color: white; margin-bottom: 10px;">Cali-Bud Delivery</h4>
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
                <p class="aw-footer-phone"><a href="tel:6615472422" style="color: #F7C948; text-decoration: none; font-weight: 700;">661-547-2422</a></p>
                <p style="font-size: 0.9rem; color: #ccc; margin-top: 10px;">Daily: 10am – 10pm</p>
            </div>
        </div>
        <div class="aw-footer-bottom">
            <p>© 2026 Cali-Bud Delivery. All rights reserved.</p>
        </div>
    </footer>
    <script src="/js/script.js"></script>
</body>
</html>
"""

    # Generate Cards
    cards_html = ""
    for article in articles:
        card = f"""
                <div class="feature-card" style="text-align: left; padding: 0; overflow: hidden; display: flex; flex-direction: column;">
                    <div style="padding: 30px; flex-grow: 1; display: flex; flex-direction: column;">
                        <span style="color: #1E7F43; font-size: 0.8rem; text-transform: uppercase; font-weight: 700; margin-bottom: 10px; display: block;">Article</span>
                        <h3 style="margin-top: 0; margin-bottom: 15px; font-size: 1.3rem;">{article['title']}</h3>
                        <p style="color: #666; font-size: 0.95rem; margin-bottom: 20px; line-height: 1.6;">{article['description']}</p>
                        <div style="margin-top: auto;">
                            <a href="/blog/{article['slug']}/" style="color: #1E7F43; font-weight: 600; text-decoration: none;">Read More &rarr;</a>
                        </div>
                    </div>
                </div>
        """
        cards_html += card

    # Write Content
    full_html = html_start + cards_html + html_end
    
    with open(os.path.join(base_dir, "index.html"), "w") as f:
        f.write(full_html)
    
    print(f"Generated Blog Hub with {len(articles)} articles.")

if __name__ == "__main__":
    generate_hub()
