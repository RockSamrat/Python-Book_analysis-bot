def count_words(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count

def count_character(text):
    character = text.lower()
    di = {}
    for c in character:
        if c in di:
            di[c] += 1
        else: 
            di[c] = 1
    return di

def sort(dic):
    big_dic = []
    for key in dic:
        big_dic.append({"char": key, "num": dic[key]})
    def sort_on(items):
            return items["num"]
    big_dic.sort(reverse=True, key=sort_on)
    return big_dic

def estimate_reading_time(word_count):
    wpm = 200
    minutes = word_count / wpm
    if minutes < 1:
        return "less than 1 minute"
    hours = int(minutes // 60)
    mins = int(minutes % 60)
    if hours == 0:
        return f"{mins} minute{'s' if mins != 1 else ''}"
    return f"{hours} hour{'s' if hours != 1 else ''} and {mins} minute{'s' if mins != 1 else ''}"

