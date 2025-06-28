# 🌐🔧 Domain Setup + Browser Request Lifecycle – Full Table
| **Phase**           | **Step**                        | **What Happens**                                            | **Example / Tool**                        |
| ------------------- | ------------------------------- | ----------------------------------------------------------- | ----------------------------------------- |
| 🛒 **Domain Setup** | 1. Buy a domain                 | Register a domain name via a registrar                      | GoDaddy, Namecheap, Google Domains        |
|                     | 2. Choose hosting               | Pick where to host your website or app                      | AWS, Hostinger, DigitalOcean, Azure, etc. |
|                     | 3. Get server IP                | Hosting gives you a public IP address or load balancer DNS  | e.g., `13.234.21.65`                      |
|                     | 4. Point domain to server (DNS) | Add **A record** in DNS settings to map domain to server IP | `@ → 13.234.21.65`, `www → 13.234.21.65`  |
|                     | 5. Enable HTTPS (SSL/TLS)       | Install SSL certificate to support secure HTTPS             | Let’s Encrypt, Certbot, or commercial CA  |
|                     | 6. Deploy website/app           | Set up a web server and serve files or run backend app      | Nginx, Apache, Node.js, Flask, etc.       |
|                     | 7. Verify access                | Open browser and visit your domain                          | `https://yourdomain.com`                  |
