# shadok

A python library that permit to unleash the full efficiency of shadok's logic.

* [Installation](https://github.com/Pierre-Sassoulas/shadok#installation)
* [Usage](https://github.com/Pierre-Sassoulas/shadok#usage)
* [FAQ](https://github.com/Pierre-Sassoulas/shadok#faq)

## Installation

```bash
pip3 install shadok
```

## Usage

### ShadokInteger

You can create a `ShadokInteger` from an int or a string.

```python
from shadok import ShadokInteger
i = ShadokInteger("BugaZoMeu")
j = ShadokInteger(56)
k = ShadokInteger("◿")
print(i,j,k)
# −𝙾ᒧ◿ ◿ᒧ𝙾 ◿
print(int(i), int(j), int(k))
# 75 56 3
print(i.pronunciation, j.pronunciation, k.pronunciation)
# BuGaZoMeu MeuZoGa Meu
```

You can't create a `ShadokInteger` from a string with multiple word. The following
code will raise an error. But the more you fail the closer you are to success :

```python
from shadok import ShadokInteger
ShadokInteger("Buga ZoMeu")
```

Will get you the following error :

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/shadok/shadok/shadok_integer.py", line 14, in __init__
    % value
shadok.path_to_success.ImproperShadokLogic: Cannot cast string containing
multiple words ('Buga ZoMeu') to an int.
``` 

### ShadokString

You can create a `ShadokString` from a shadok sentences with multiple words
separated by spaces. If a word is an shadok integer you can get its value
with `int()`. `ShadokString` are string, it means you can create a
`ShadokInteger` from one.

```python
from shadok import ShadokString
a = ShadokString("zogabuzomEu")
b = ShadokString("ZoGabuzoMeu")
c = ShadokString("Gabu")
c += "◿ᒧ𝙾 ZoMEU"  # Mutlitple words
print(a,b,c)
# ZoGaBuZoMeu ZoGaBuZoMeu GaBu ◿ᒧ𝙾 ZoMeu
print(int(a), int(b)) # c cannot be casted to int
# 539 539
```

You can't use improper shadok syntax in a `ShadokString` :

```python
from shadok import ShadokString
ShadokString("Gabu Gibi")
```

Will get you the following error :

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/shadok/shadok/shadok_string.py", line 42, in __init__
    MagicFaucet.check_syntax(self.raw_string)
  File "/home/shadok/shadok/magic_faucet.py", line 42, in check_syntax
    raise ImproperShadokSyntax(word, matches)
shadok.path_to_success.ImproperShadokSyntax:
Incorrect shadok syntax in 'Gibi'
                            ^^^^
Au Goulp !
```

### MagicFaucet

The `MagicFaucet` permit to check if a string is in proper Shadok syntax :

```python
from shadok import MagicFaucet
# Proper syntax, nothing will happen
MagicFaucet.check_syntax("GabuZo")
# Will raise an ImproperShadokSyntax exception
MagicFaucet.check_syntax("GabuZoMi")
```

Will get you the following error :

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/shadok/shadok/magic_faucet.py", line 42, in check_syntax
    raise ImproperShadokSyntax(word, matches)
shadok.path_to_success.ImproperShadokSyntax:
Incorrect shadok syntax in 'GabuZoMi'
                                  ^^
Au Goulp !
```

The `MagicFaucet` also permit to pretty print your shadok without instantiation of a `ShadokString`:

```
>>> MagicFaucet.pretty_print("meumEumUumeu")
'MeuMeuMeuMeu'
```

## FAQ

* I need to perform serious arithmetic operations on large numbers does this library provide that ?

Sadly the highest order of meta-bin yet attainable is only 31. Those are big very meta bins
though.

* My empty meta bins are disappearing when I create a `ShadokInteger` ?!
But I need them if my number get bigger !

Stop reporting this issue. This is a feature not a bug ! You should create meta bins
only when you need them for efficiency. I don't care about your use case.

* Why is `GaGaGaGaGaBu` becoming `Bu` when I cast it to `int` ?

See "*My empty meta bins are disappearing*".

* My string was `Gagaga` and was casted to a boolean. It returned `False`, shouldn't it means
`You fool !` and be `True` instead ?

When evaluating a string containing only `Ga` you must ask yourself :
why make a simple test when a complicated one will do ? The shadok logic tell us
that we need to cast to an int when evaluating a boolean value.
We must also get rid of the empty meta bins in integer. So `Gagaga` equals 0,
equals `[False, "You fool !"]`. So when casted into a boolean you have 1 in 33
chance that its equals to `False` and 1 in 2 chance that its equal to `"You fool !"`.
It could also be `True` but that would really be by chance and maybe by mistake.


* Is there any side effect to using this library ?

Yes, we're trying to rely on the new threshold required to be parent (`BuBu`).
If you're using the program before it was created and if the new reform
is not yet effective, we can count to the old limit (`BuGa`) and create one or a
few millions of eggs. Also sometime we're not very careful.
Please however note that this help with performance because they can help with
parallelism as soon as they hatch.

* Can I run this in parallel ?

See question above, this is the default, but you need to count to **−−** first.
If you count to **−𝙾** or less why do you even want to run in parallel in the first
place ?

* Do you count to **−𝙾** when you pretty print using MagicFaucet ?

No.

* I get a `ColanderIsInFactABusError` when I instantiate my `Colander`...

Your colander seems to be a pot, please make sure your pot has a handle and is
not, in fact, a bus.
