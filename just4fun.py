"""
https://py.checkio.org/en/mission/morse-decoder/
"""

MORSE = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
}

# print(MORSE["----."], MORSE[".---"])


def morse_decoder(code: str) -> str:
    wc = 0
    temporary_date = ""
    for coded_world in code.split("   "):
        lc = 0
        for coded_letter in coded_world.split(" "):
            if (wc == 0 and lc == 0):
                temporary_date = temporary_date + MORSE[coded_letter].upper()
            else:
                temporary_date = temporary_date + MORSE[coded_letter]
            lc += 1
        temporary_date = temporary_date+" "
        wc += 1

    return "".join(temporary_date.strip())


print("Example:")
print(morse_decoder("... --- -- .   - . -..- -"))
print( morse_decoder("..   .-- .- ...   -... --- .-. -.   .. -.   .---- ----. ----. -----"))
print(morse_decoder('...- ...-- .-. -.--   .---- ----- -. --.   ... - .-. .---- -. --.   .-- .---- - ....   ... ----- -- ...--   -. ..- -- -... ...-- .-. .....'))
assert morse_decoder("... --- -- .   - . -..- -") == "Some text"
assert (
    morse_decoder("..   .-- .- ...   -... --- .-. -.   .. -.   .---- ----. ----. -----")
    == "I was born in 1990"
)
assert morse_decoder('... --- -- .   - . -..- -') == 'Some text'
assert morse_decoder('..   .-- .- ...   -... --- .-. -.   .. -.   .---- ----. ----. -----') == 'I was born in 1990'
assert morse_decoder('.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..') == 'Abcdefghijklmnopqrstuvwxyz'
assert morse_decoder('----- .---- ..--- ...-- ....- ..... -.... --... ---.. ----.   .- .-. .   -.. .. --. .. - ...') == '0123456789 are digits'
assert morse_decoder('...- ...-- .-. -.--   .---- ----- -. --.   ... - .-. .---- -. --.   .-- .---- - ....   ... ----- -- ...--   -. ..- -- -... ...-- .-. .....') == 'V3ry 10ng str1ng w1th s0m3 numb3r5'

print("The mission is done! Click 'Check Solution' to earn rewards!")
