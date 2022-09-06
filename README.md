# python_projects

### Misc

- Use Ephem library to calculate the distance between a given planet and the sun on a given date.

  - Needed to use the python inbuilt function getattr() to dynamically select the method.
  - Ephem has a separate method for each planet. Example: ephem.Jupiter(), Ephem.Pluto()
    - ephem[selected_planet]() results in a type error, need to use getattr() to circumvent.

- Use screeninfo library to get screen resolution for single and multi monitor setups.

### Cryptography:

- _Caesar Cipher_: Encrypt/Decrypts a string using a character shift as as key. shift = 3: "A" => "D"
  - Caesar cipher is generally weak since it can be easily broken by using frequency analysis to discover the key.
  - Frequency analysis: some letters and letter combinations are more likely than others.
    - If you know that "A" has a relative frequency of 8%, but "K" in the encrypted text has gone from 0.77% => 8%...

NB! Current implementation of the cipher preserves spaces and punctuation which makes it even weaker than necessary
Example: - "Here is an example of the weakness" => - "EBOB FP XK BUXJMIB LC QEB TBXHKBPP" vs. "EBOB FPXK BUXJ MIBL CQEBT BXHKB PP"
