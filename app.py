from googletrans import Translator

def translate_text(text, target_language):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

def main():
    print("Welcome to the Translator App!")
    while True:
        text = input("Enter the text to translate (or 'q' to quit): ")
        if text.lower() == "q":
            break
        source_language = input("Enter the source language: ")
        target_language = input("Enter the target language: ")
        translation = translate_text(text, target_language)
        print("Translation:", translation)
        print()

if __name__ == "__main__":
    main()
