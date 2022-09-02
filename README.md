# python_projects

### Cryptography:

- _Caesar Cipher_: Encrypt/Decrypts a string using a character shift as as key. shift = 3: "A" => "D"
  - Caesar cipher is generally weak since it can be easily broken by using frequency analysis to discover the key.
  - Frequency analysis: some letters and letter combinations are more likely than others.
    - If you know that "A" has a relative frequency of 8%, but "K" in the encrypted text has gone from 0.77% => 8%...

NB! Current implementation of the cipher preserves spaces and punctuation which makes it even weaker than necessary
