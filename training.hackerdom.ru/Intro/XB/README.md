Task is:
BBBBX B XBBBB XBB BBBBX B XBBBB XBBB BBBBX XBB XXBBB BX BBBBB BBBBB BBBXX BXXXX BBBBX B XBBBB XBB BBBBB
BBXXX XBBBB XBXB BBBBB XXXXB XBBBB BX BBBBX BBXXX XBBBB XBBB BBBBB XXXXB BBBBB BBBBX BBBBB BBBBB BBBXX
XXXXX BBBBB XXXXB XBBBB XBB BBBBX B XBBBB XXXBB BBBBX XBB BBBBX BBBBX BBBBB XXXXB XXBBB XXBBB BBBBB
XXXXB XBBBB BX BBBBB BBXXX XBBBB BX BBBBX XBB XXBBB BX XBBBB XBBB BBBXX XXXXX BBBBX B XXBBB BX XBBBB
XBBB BBBXX BBBBX BBBBX XBB XXBBB BX XBBBB XBBB BBBXX XBB

let's guess that B is dot and X is "-":

....- . -.... -.. ....- . -.... -... ....- -.. --... .- ..... ..... ...-- .---- ....- . -.... -.. .....
..--- -.... -.-. ..... ----. -.... .- ....- ..--- -.... -... ..... ----. ..... ....- ..... ..... ...--
----- ..... ----. -.... -.. ....- . -.... ---.. ....- -.. ....- ....- ..... ----. --... --... .....
----. -.... .- ..... ..--- -.... .- ....- -.. --... .- -.... -... ...-- ----- ....- . --... .- -....
-... ...-- ....- ....- -.. --... .- -.... -... ...-- -..

Decoding via http://www.unit-conversion.info/texttools/morse-code/

4e6d4e6b4d7a55314e6d526c596a426b59545530596d4e684d445977596a526a4d7a6b304e7a6b344d7a6b3d

Seems like HEX.
========================================================================================================
on another hand, when B is "-" and X is dot:
----. - .---- .-- ----. - .---- .--- ----. .-- ..--- -. ----- ----- ---.. -.... ----. - .---- .-- -----
--... .---- .-.- ----- ....- .---- -. ----. --... .---- .--- ----- ....- ----- ----. ----- ----- ---..
..... ----- ....- .---- .-- ----. - .---- ...-- ----. .-- ----. ----. ----- ....- ..--- ..--- -----
....- .---- -. ----- --... .---- -. ----. .-- ..--- -. .---- .--- ---.. ..... ----. - ..--- -. .----
.--- ---.. ----. ----. .-- ..--- -. .---- .--- ---.. .--

9t1w9t1j9w2n00869t1w0
71?041n971j0409008
5041w9t139w9904220
41n071n9w2n1j859t2n1
j899w2n1j8?

Creepy thing.

Let's stay with first choice.
========================================================================================================

Convert HEX to ASCII (via http://www.rapidtables.com/convert/number/hex-to-ascii.htm):

NmNkMzU1NmRlYjBkYTU0YmNhMDYwYjRjMzk0Nzk4Mzk=

This is a Base64 code (look at "=" on the end)

which becomes to (https://www.base64decode.org/):
6cd3556deb0da54bca060b4c39479839

Looks like a md5. Use http://www.md5online.org/ to decrypt:

And value (flag) is: Hello, world!


