# shadok

A python library that permit to unleash the full efficiency of shadok's logic.

## Installation

```bash
pip3 install shadok
```

## Usage

### ShadokInteger

You can create a `ShadokInteger` from an int or a string. `ShadokString` are string,
it means you can create a `ShadokInteger` from one.

```
>>> from shadok import ShadokInteger
>>> ShadokInteger("BugaZoMeu")
−𝙾ᒧ◿
>>> ShadokInteger("−𝙾ᒧ◿").pronunciation
'BuGaZoMeu'
>>> ShadokInteger(56)
◿ᒧ𝙾
>>> ShadokInteger(56).pronunciation
'MeuZoGa'
```

You can't create a `ShadokInteger` from a string with multiple word :

```
>>> ShadokInteger("Buga ZoMeu").pronunciation
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/pierre/workspace/shadok/shadok/shadok_integer.py", line 14, in __init__
    % value
shadok.path_to_success.ImproperShadokLogic: Cannot cast string containing multiple words ('Buga ZoMeu') to an int.
``` 

### ShadokString

You can create a `ShadokString` from a shadok sentences with multiple words
separated by spaces. If a word is an shadok integer you can get its value
with `int()`.

```
>>> from shadok import ShadokString
>>> ShadokString("zogabuzomEu")
ZoGaBuZoMeu
>>> int(ShadokString("ZoGabuzoMeu"))
539
>>> ShadokString("Gabu ◿ᒧ𝙾")
GaBu ◿ᒧ𝙾
```

You can't use improper shadok syntax in a `ShadokString` :

```
>>> ShadokString("Gabu Gibi")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/pierre/workspace/shadok/shadok/shadok_string.py", line 42, in __init__
    MagicFaucet.check_syntax(self.raw_string)
  File "/home/pierre/workspace/shadok/shadok/magic_faucet.py", line 42, in check_syntax
    raise ImproperShadokSyntax(word, matches)
shadok.path_to_success.ImproperShadokSyntax:
Incorrect shadok syntax in 'Gibi'
                            ^^^^
Au Goulp !
```

You can't cast a `ShadokString` with multiple word to an `int` :

```
>>> int(ShadokString("Gabu ◿ᒧ𝙾"))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/pierre/workspace/shadok/shadok/shadok_string.py", line 52, in __int__
    number = ShadokInteger(self.raw_string)
  File "/home/pierre/workspace/shadok/shadok/shadok_integer.py", line 14, in __init__
    % value
shadok.path_to_success.ImproperShadokLogic: Cannot cast string containing multiple words ('Gabu ◿ᒧ𝙾') to an int.
```

### MagicFaucet

The `MagicFaucet` permit to check if a string is in proper Shadok syntax :
```
>>> from shadok import MagicFaucet
>>> MagicFaucet.check_syntax("GabuZo")
>>> MagicFaucet.check_syntax("GabuZoMi")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/pierre/workspace/shadok/shadok/magic_faucet.py", line 42, in check_syntax
    raise ImproperShadokSyntax(word, matches)
shadok.path_to_success.ImproperShadokSyntax:
Incorrect shadok syntax in 'GabuZoMi'
                                  ^^
Au Goulp !
```

It also permit to pretty print your shadok without instantiation of a `ShadokString`:

```
>>> MagicFaucet.pretty_print("meumEumUumeu")
'MeuMeuMeuMeu'
```

## FAQ

* I need to perform serious arithmetic operations on large numbers does this library provide that ?

Sadly the highest order of meta-bin yet attainable is only 31. Those are big very meta bins
though.

* Is there any side effect to using this library ?

Yes, sometimes we're not careful and we count to BuGa, so some shadok's eggs
can be created. Please however note that this help with performance because they
can help with parallelism as soon as they hatch.

* Can I run this in parallel ?

See question above, this is the default, but you need to count to **−𝙾** first.
If you count to **◿** or less why do you even want to run in parallel in the first
place ?

* Do you count to **−𝙾** when you pretty print using MagicFaucet ?

No.

* I get a `ColanderIsInFactABusError` when I instantiate my `Colander`...

Your colander seems to be a pot, please make sure your pot has a handle and is
not, in fact, a bus.
