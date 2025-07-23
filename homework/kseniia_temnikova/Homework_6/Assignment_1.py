text = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel.' \
       ' Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
updated_text = text.split()
print(updated_text)
final_text = []
for word in updated_text:
    if (',' not in word) and ('.' not in word):
        final_text.append(word + 'ing')
    else:
        word = word[:-1] + 'ing' + word[-1]
        final_text.append(word)
print(' '.join(final_text))
