import re
import nltk as tk
tk.download('punkt')

with open (r'data\0_9.txt','r') as file:
    data=file.read()
    print(data)
    
# 更新你的data，把大写转为小写
data = data.lower()
# 将所有非数字字符的符号转化为空
data = re.sub(r'[^a-z0-9\s]', '', data)  
print(data)  

# 获得你的tokens #
tk.data.path.append('F:/anaconda/envs/skim/lib/nltk_data')
tokens = tk.wordpunct_tokenize(data)
tokens2 = tk.word_tokenize(data)
print(tokens2)
print(tokens)

import nltk.stem as ns
from nltk.corpus import wordnet
from nltk import pos_tag

# 定义要进行词形还原的单词
token = "running"

result = []
lemmatizer = ns.WordNetLemmatizer()

# 获取单词的词性标记，使用pos_tag函数
pos = pos_tag([token])[0][1]
# pos = pos_tag([token]) 会打印出什么？尝试一下
print(pos)

# 将词性标记转换为WordNet词性标记
wn_pos = wordnet.VERB if pos.startswith('V') else wordnet.NOUN

print(wn_pos)
# 现在可以使用lemmatizer.lemmatize()还原词性并且打印结果