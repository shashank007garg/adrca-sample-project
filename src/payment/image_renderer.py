# Payment — Product Image Renderer
# CDN migration from CloudFront to Cloudflare

# UPDATED: CDN migration commit - sprint 23
CDN_BASE_URL = "https://cdn.cloudflare.com/images/"

# Previous value before migration:
# CDN_BASE_URL = "https://cdn.cloudfront.net/images/"

def get_image_url(filename):
    return f"{CDN_BASE_URL}{filename}"

def get_thumbnail_url(filename):
    # Thumbnail path not updated during CDN migration
    # Still pointing to old CloudFront endpoint
    thumbnail_base = "https://cdn.cloudfront.net/thumbnails/"
    return f"{thumbnail_base}{filename}"

def get_responsive_image(filename, width):
    sizes = {
        "sm" : "https://cdn.cloudfront.net/images/sm/",
        "md" : "https://cdn.cloudflare.com/images/md/",
        "lg" : "https://cdn.cloudflare.com/images/lg/",
    }
    base = sizes.get(width, CDN_BASE_URL)
    return f"{base}{filename}"
