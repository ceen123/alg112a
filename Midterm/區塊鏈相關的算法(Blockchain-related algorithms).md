
**

## Blockchain

**

Blockchain technology relies on several algorithms and data structures to achieve its goals of decentralization, security, and immutability. Here are some key algorithms and data structures associated with blockchain:

**Hash Function:**
The most commonly used Hashing algorithm are:

 - MD5 (Message-Digest Algorithm 5)
 - SHA256
 - SHA384
 - SHA224
 - SHA512
 - SHA-1

SHA-256(Secure Hash Algorithm 256-bit), This cryptographuc hash function is widely used in blockchain to produce a fixed-size output that uniquely represent input data. It plays a crucial role in creating blocks and securing the integrity of data. 

![enter image description here](https://www.simplilearn.com/ice9/free_resources_article_thumb/hashing1.PNG)

The hash function is responsible for converting the plaintext to its respective hash digest. They are designed to be irreversible, which means your hash value should not provide you with the original plain text. Hash function also provide the same output value if the input remains unchanged.
The primary application of hashing:

 - *Password Hashes*
![enter image description here](https://www.simplilearn.com/ice9/free_resources_article_thumb/passwords.PNG)
 - Integrity Verification
![enter image description here](https://www.simplilearn.com/ice9/free_resources_article_thumb/integrity1.PNG)

These are the python code comparison of using Hashing algorithm of md5 andsha 256

    import hashlib
    result = hashlib.md5(b"Password123$%").hexdigest()
    print(result)
> 01670e8205dc727ce0af1cd4b429a321

    import hashlib
    test_str = "Password123$%"
    result = hashlib.sha256(test_str.encode())
    print(result.hexdigest()) 
> 9e2c546ac62f635d12742532b4dee9bfd670fba23aca6bd8cccc2ca87a59cfe4

The proccess inside a Blockchain are simply these four steps
![enter image description here](https://www.simplilearn.com/ice9/free_resources_article_thumb/apps_Sha.PNG)


