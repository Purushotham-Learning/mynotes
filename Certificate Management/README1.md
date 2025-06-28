# 🔐 SSL, TLS, and OpenSSL – Comparison Table
| **Aspect / Topic**     | **SSL**                                          | **TLS**                                                     | **OpenSSL**                                                             |
| ---------------------- | ------------------------------------------------ | ----------------------------------------------------------- | ----------------------------------------------------------------------- |
| **Full Form**          | Secure Sockets Layer                             | Transport Layer Security                                    | Open Secure Sockets Layer                                               |
| **Type**               | Security Protocol                                | Security Protocol                                           | Tool / Library                                                          |
| **Purpose**            | Secure/encrypt data transmission                 | Secure/encrypt data transmission                            | Generate, manage keys, CSRs, and certificates; test SSL/TLS connections |
| **Status**             | ❌ Obsolete (SSLv2/3 deprecated, insecure)        | ✅ Actively used (TLS 1.2 / 1.3 are current standards)       | ✅ Actively maintained, open-source                                      |
| **Replaced By**        | TLS                                              | Ongoing improvements (e.g., TLS 1.3 is faster, more secure) | Not applicable                                                          |
| **Used In**            | Legacy systems, old HTTPS/FTPS/Email servers     | Modern HTTPS, APIs, SMTP/IMAPS, VPNs, Docker, Kubernetes    | DevOps, CI/CD, Kubernetes, Docker, Linux environments                   |
| **Security Level**     | Weak (vulnerable to attacks like POODLE, BEAST)  | Strong (modern crypto; forward secrecy in TLS 1.3)          | Secure if used properly; supports modern ciphers and protocols          |
| **Handshake Support**  | Yes (legacy handshake methods)                   | Yes (faster, more secure in TLS 1.3)                        | Can simulate or test TLS handshakes (e.g., `openssl s_client`)          |
| **Encryption Type**    | Symmetric + Asymmetric (older standards)         | Symmetric + Asymmetric (modern standards like AES, ECDHE)   | Supports both encryption methods (depends on usage)                     |
| **Certificate Format** | X.509 Certificates                               | X.509 Certificates                                          | Creates, signs, and manages X.509 certificates                          |
| **Common Versions**    | SSL 2.0, SSL 3.0 (both deprecated)               | TLS 1.0, 1.1, 1.2, 1.3 (TLS 1.2/1.3 in use today)           | Supports TLS 1.0 through TLS 1.3                                        |
| **Example Command**    | ❌ Not applicable                                 | ❌ Not applicable                                            | `openssl req -new -x509 -key key.pem -out cert.pem`                     |
| **Common Use Case**    | Deprecated systems, rarely used in modern setups | Secure websites, APIs, email servers, VPN, mobile apps      | Certificate creation, CSR generation, TLS testing, internal dev certs   |
| **Platform Usage**     | Legacy apps, no longer secure                    | Modern apps, browsers, cloud infrastructure                 | Docker TLS certs, Kubernetes secrets, CI/CD scripts, Linux servers      |



# 🛠 Common Use Cases with OpenSSL (Related to TLS)
| Use Case                       | OpenSSL Command Example                                                    |
| ------------------------------ | -------------------------------------------------------------------------- |
| Generate Private Key           | `openssl genrsa -out domain.key 2048`                                      |
| Create CSR                     | `openssl req -new -key domain.key -out domain.csr`                         |
| Self-sign Certificate          | `openssl req -x509 -newkey rsa:2048 -nodes -keyout self.key -out self.crt` |
| Verify Certificate             | `openssl x509 -in cert.pem -text -noout`                                   |
| Check SSL Connection to Server | `openssl s_client -connect example.com:443`                                |
| Convert PEM to PFX             | `openssl pkcs12 -export -out cert.pfx -inkey key.pem -in cert.pem`         |
