import lang
_ = lang.get

lang.add('locales/pl.xml')
lang.add('locales/de.xml')

print("Available languages:")
print(lang.all(), "\n")

print("Text:", _("Hello World"))
lang.select('de')
print("Actually selected:", lang.selected)
print("German:", _("Hello World"))
lang.select('pl')
print("Actually selected:", lang.selected)
print("Polish:", _("Hello World"))
lang.select()
print("Original:", _("Hello World"))