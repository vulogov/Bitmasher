# Bitmasher - private key crypto algorithm based on bit buffer rotation and steganography

## Algorithm.
  Bitmasher is based on three encryption ideas combined in three passes of  encryption.

  - XOR encryption of the data with rotational key
  - Mixing XOR encrypted block of data with a random data
  - Bit-rotation ROR/ROL (ROR/ROL for decryption), based on two random keys: one defining the depth of the rotation, other - directionality of the rotation.

  So, in order to break encrypted block of data, you actually need to figure out two keys, and second stage mixing preventing statistical analysis. If you are interested to learn more about algorithm itself, please take a look at this slides. [Buffer bit-rotating cryptography with steganography](https://www.slideshare.net/VladimirUlogov1/short-presentation-of-the-bitmasher-privatekey-encryption)

## "Hello World" of the Bitmasher

```
>>> from Bitmasher import *
>>> n = init()
>>> d = encrypt(n, "This is a BIG secret")
>>> print(decrypt(n, *d))
b'This is a BIG secret'
>>>
```
 - First, we have to import Bitmasher functions. Python 3.6 or newer is required.
 - Next, we initializing namespace for a crypto operations.
 - We are encrypting. Note, first parameter to a `encrypt` function is a reference to a namespace. You can pass any Python values, supported by `msgpack` serializing library.
 - Next, we decrypting. Please note, you have to pass namespace as first parameter.

 This is all very simple

## Where is my keys !!!!
  Bitmasher does not trust you with keys generation. It maintain a "codebook" internally by generating keys on demand. First 1024 keys are generating while calling init(). Each block of data encrypting with uniq key. Key consisting of two parts:
  - Private key. serves as modulo for the XOR operation during the first pass and number of rotation at third pass.
  - Masher. Dataset defining directionality of the rotations at third pass.

  Function `encrypt` returning the list of the tuples, where first element of the tuple is key ID and second element is encrypted data. In order to decrypt, you are expecting to load a "used pages" from codebook, that you received by secure means inside Bitmasher namespace.

### How to export pages from a codebook which were used during encryption ?

```
>>> from Bitmasher import *
>>> n = init()
>>> d = encrypt(n, "This is a BIG secret")
>>> book = cryptobook_save(n)
>>> len(book)
21085
>>> book[:32]
b'\x82\xda\x00$1ba990f9-6b43-4a9d-9bc1-a820'
```
  Yep, it is a msgpack data. And it is contains all your keys.

### How to load pages from a codebook to use for decryption

```
>>> from Bitmasher import *
>>> n = init()
>>> d = encrypt(n, "This is a BIG secret")
.... saving and transferring cryptobook image
>>> n = cryptobook_load(n, book)
>>> print(decrypt(n, *d))
b'This is a BIG secret'
```
