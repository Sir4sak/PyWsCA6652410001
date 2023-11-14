def word (sentence):
    words = sentence.split()
    xwords = len(words)
    
    uniqueWords = set(words)
    totalUnique = len(uniqueWords)
    
    duplicatewords = [word for word in uniqueWords if words.count(word) > 1]
    
    print(f"มีคำรวมทั้งหมด {xwords} คำ")
    print(f"มีคำที่ซ้ำกันรวม {len(duplicatewords)} คำ คือ {' '.join(duplicatewords)}")
    
    for word in duplicatewords:
        count = words.count(word)
        print(f"คำว่า {word} ซ้ำกัน {count} ครั้ง")

try:
    inputSentence = input("ป้อนข้อความ: ")
    word (inputSentence)
except Exception as e:
    print(f"เกิดข้อผิดพลาด: {e}")