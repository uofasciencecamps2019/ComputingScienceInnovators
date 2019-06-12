# Cryptography Scavenger Hunt

### Rules
1. Asking your peers for help is okay, but try not to copy and paste their code
2. If you get any code from peers or online sources, cite your sources
3. Make sure your code is compatible with Python3 (some things you look up will work for Python2 but not Python3)

#### When you are done
1. Save all of your answers in a file called firstname_lastname_scavenger.txt
2. Call one of the camp leaders over to check your answers

```text
Tem Tamre
Scavenger hunt answers

Puzzle 1: answer1, answer2

Puzzle 2: answer1, answer2, answer3

Puzzle 3: answer1, answer2

Puzzle 4: answer

Puzzle 5: answer

Puzzle 6: answer

Puzzle 7: answer
```

*Hint: Make full use of Github's website functions to find hidden clues*

### Puzzle 1: Caesar Cipher Decryption
You will be given 2 sentences that has been encrypted using a caesar cipher. The first one will be accompanied by the shift number, which should make decryption a lot easier. The second, however, will not come with a key.

```python
ciphertext1 = "nvctfdv kf tfdglkzex jtzvetv zeefmrkfij"  # Key = 17
ciphertext2 = "kd dro exsfobcsdi yp kvlobdk mywzedsxq cmsoxmo moxdob"
```

<!-- Hint: ciphertext1 is something that we did earlier, ciphertext2 can be solved with a for loop and some printing-->

### Puzzle 2: Substitution Cipher Encryption
You will be given 3 words or phrases that need to be encrypted using the substitution cipher. Come up with a key for each plaintext that will convert them to the expected ciphertext

```python
plaintext1 = "We will stirke Venice"    # Expected ciphertext: xf xjmm tujslf wfojdf
plaintext2 = "Server shutdown"          # Expected ciphertext: ugtxgt ujwvfqyp
plaintext3 = "Build the fort"           # Expected ciphertext: niozf yjr gpty
```

<!-- Hint: the first two plaintext strings should be encrypted using keys that are in-order -->

### Puzzle 3: Decode the ASCII characters
Decode the two codes below

```python
109 105 99 114 111 115 111 102 116
103 111 108 100 101 110 32 98 101 97 114 115
```

<!-- Hint: You can use the same method you used to solve puzzle 1 -->

### Puzzle 4: Three-Rail Cipher
Your job is to learn about the three-rail cipher, explain it in your own words, and use it to encrypt the following plaintext

```python
plaintext = "We should invade the North"
```

<!-- Hint: You don't need to write any code to solve this -->

### Puzzle 5: Vignere Cipher
Your job is to learn about the vignere cipher and explain it in your own words

<!-- Hint: Just like in puzzle 4, you don't need to write any code to solve this -->
<!-- Answer:
Each character is encrypred according to multiple substitution ciphers -->

### Puzzle 6: Hidden Message
Decipher the code in the following message:

```text
115516 25152118 41201 19165
```

<!-- Hint: Letters can be numbers too -->

### Puzzle 7: Quantum Cryptography (very hard)
Explain (in a few sentences) what quantum cryptography is, in your own words.

<!-- Hint: First, try to figure out what quantum bits are. Then, figure out what quantum computing is. -->
