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
    temporary_date = ""
    for coded_world in code.split("   "):
        for coded_letter in coded_world.split(" "):
            temporary_date = temporary_date + MORSE[coded_letter]
        temporary_date = temporary_date+" "
    return temporary_date


print("Example:")
print(morse_decoder("... --- -- .   - . -..- -"))
print( morse_decoder("..   .-- .- ...   -... --- .-. -.   .. -.   .---- ----. ----. -----"))

assert morse_decoder("... --- -- .   - . -..- -") == "some text"
assert (
    morse_decoder("..   .-- .- ...   -... --- .-. -.   .. -.   .---- ----. ----. -----")
    == "i was born in 1990"
)

print("The mission is done! Click 'Check Solution' to earn rewards!")
