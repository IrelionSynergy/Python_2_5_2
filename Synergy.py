# Гласные буквы английского алфавита - «a», «e», «i», «o», «u», «y»

vowels = ['a', 'e', 'i', 'o', 'u', 'y']
countVowel = 0
countSingleChar = 0

print('Введите слово на английском языке:')
stringList = list(input().lower());

for vowel in vowels:
    for char in stringList:
        if vowel == char:
            countVowel += 1
            countSingleChar += 1

    if countSingleChar == 0:
        countSingleChar = False

    print('{vowel} = {cSC}'.format(vowel = vowel, cSC = countSingleChar))
    countSingleChar = 0

countConsonant  = len(stringList) - countVowel

print('Общее количество гласных букв в слове = {countVowel}'.format(countVowel = countVowel))
print('Общее количество согласных букв в слове = {countConsonant}'.format(countConsonant = countConsonant))