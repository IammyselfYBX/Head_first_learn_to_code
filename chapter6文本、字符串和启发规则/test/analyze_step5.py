#建立启发规则
import ch1text

def count_syllables(words): #这是新的函数,接受一个单词列表
    count = 0

    for word in words:
        word_count = count_syllables_in_word(word)
        count = count + word_count

    return count

def count_syllables_in_word(word):  #这个是启发式计算音节数的
    count = 0

    if len(word) <= 3:
        return 1   
 
    vowels = "aeiouAEIOU"
    prev_char_was_vowel = False

    for char in word:
        if char in vowels:
            if not prev_char_was_vowel: #如果处理当前字符是一个元音,而前一个不是,音节数+1
                count = count + 1
            prev_char_was_vowel = True  #处理下一个音节前,清为True
        else:                           #这个else是和 if char in vowels: 匹配的
            prev_char_was_vowel = False

    return count

def count_sentences(text):
    count = 0

    terminals = '.;?!'
    for char in text:
        if char in terminals:
            count = count + 1
    return count

def compute_readability(text):
    total_words = 0
    total_sentences = 0
    total_syllables = 0
    score = 0

    words = text.split()
    total_words = len(words)
    total_sentences = count_sentences(text)
    total_syllables = count_syllables(words)

    print(total_words, 'words')
    print(total_sentences, 'sentences')
    print(total_syllables, 'syllables')

compute_readability(ch1text.text)
