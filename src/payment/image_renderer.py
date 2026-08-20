Content:
# Payment — Product Image Renderer
# CDN migration from CloudFront to Cloudflare

# OLD URL — hardcoded, not updated after migration
CDN_BASE_URL = "https://cdn.cloudfront.net/images/"

# Should be: https://cdn.cloudflare.com/images/
# This caused KAN-6 after CDN migration

def get_image_url(filename):
    return f"{CDN_BASE_URL}{filename}"
