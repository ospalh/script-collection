## Scripts for this and that

This is a collection of different scripts and short programs i found
useful. The are roughly organized by usage. Some of them are a little
bit cumbersome to use, and closely tailored to my use. Take it or,
leave it, or take it and modify it.

Categories:
* file system: for use when looking at files
* scanning: useful when scanning and post-processing books
* text: text processing

### days

Print the age of one or more files in days, using a special formatting
that i like. It repeats the file names when more than one is given, or
just prints the age for one.

Use `days -h` to see more options.


### un-one-two

When scanning two pages at once with [xsane](http://xsane.org/)’s `+2`
file numbering, the [scantailor](http://scantailor.org/) output file
names may look like this:

* `Frankenstein_001.tif`
* `Frankenstein_002_1L.tif`
* `Frankenstein_002_2R.tif`
* `Frankenstein_004_1L.tif`
* `Frankenstein_004_2R.tif`
* `Frankenstein_006_1L.tif`
* `Frankenstein_006_2R.tif`

and so on.

This script renames files with a  `n_[12][LR]`  pattern so that you end up with nicer file names:

* `Frankenstein_001.tif`
* `Frankenstein_002.tif`
* `Frankenstein_003.tif`
* `Frankenstein_004.tif`
* `Frankenstein_005.tif`
* `Frankenstein_006.tif`
* `Frankenstein_007.tif`

and so on.

You have to give the prefix and suffix explicitly, for example, you have to run it as `un-one-two --prefix Frankenstein_ --suffix .tif`. When you don’t use three digit page numbers, you have to change the script.


### shift-by

Fixes errors when you skipped a (double) page during scans, or scanned one twice. Say, you accidentally scanned the double page 8, 9 twice, and notices this only much later:

* …
* `Sherlock Holmes 006.png` contains pages 6, 7, OK
* `Sherlock Holmes 008.png` contains pages 8, 9, OK
* `Sherlock Holmes 010.png` contains pages 8, 9 again. Can be deleted
* `Sherlock Holmes 012.png` contains pages 10, 11, but looks like pages 12, 13
* `Sherlock Holmes 014.png` contains pages 12, 13, but looks like pages 14, 15
* `Sherlock Holmes 016.png` contains pages 14, 15, but looks like pages 16, 17
* `Sherlock Holmes 018.png` contains pages 16, 17, but looks like pages 18, 19
* …

Then you would run `shift-by --prefix "Sherlock Holmes " --suffix .png --by 2 --min 12` and end up with one fewer file:

* …
* `Sherlock Holmes 006.png` stayed the same
* `Sherlock Holmes 008.png` stayed the same
* `Sherlock Holmes 010.png` old file `Sherlock Holmes 012.png`, original got clobbered
* `Sherlock Holmes 012.png` old file `Sherlock Holmes 014.png`, original was moved before this move
* `Sherlock Holmes 014.png` old file `Sherlock Holmes 016.png`, original was moved before this move
* `Sherlock Holmes 016.png` old file `Sherlock Holmes 018.png`, original was moved before this move
* `Sherlock Holmes 018.png` old file `Sherlock Holmes 020.png`, original was moved before this move
* …

and each file now contains the page from its name.

### de-utf-mojibake

This fixes one common case of mojibake
([文字化け](https://en.wikipedia.org/wiki/Mojibake)): Text that was
UTF-8 encoded, has been opened as plain 8-bit encoding (specifically
[Code page 1252](https://en.wikipedia.org/wiki/Windows-1252)), and
saved as UTF-8.

When you see a text that is Unicode, but where non-ASCII characters
are messed up, you can try this. For example, i came along a “MÃ¶bius”
once, with the *two* Unicode characters »LATIN CAPITAL LETTER A WITH
TILDE« and »PILCROW SIGN«. With a
[bit of](http://www.fileformat.info/info/unicode/char/search.htm?preview=entity&q=%C3%83)
[resarch](http://www.fileformat.info/info/unicode/char/search.htm?preview=entity&q=%C2%B6)
you find out that those are the Unicode characters (code points)
U+00C3 and U+00B6, encoded as two eight-bit octets each. On the other hand,
the two octets 0xc3 + 0xb6 together are the Unicode character
[ö](http://www.fileformat.info/info/unicode/char/00f6/index.htm).

To save all this look up, just run this script on the file with the dubious characters, `de-utf-mojibake mojibake-file fixed-file`, and voilà, “MÃ¶bius” is turned into “Möbius”.


### unicode-names

Show the names of unicode characters given as argument, together with the code point. For example `unicode-names "Aß☭🚴🏼"` prints out
```
» A «: LATIN CAPITAL LETTER A 0x41
» ß «: LATIN SMALL LETTER SHARP S 0xdf
» ☭ «: HAMMER AND SICKLE 0x262d
» 🚴 «: BICYCLIST 0x1f6b4
» 🏼 «: EMOJI MODIFIER FITZPATRICK TYPE-3 0x1f3fc
```
