from wordcloud import WordCloud
import jieba
import PIL
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

'''
画词云
'''
def wordcloudplot(txt, maxWords):
    path='c:/Windows/Fonts/simhei.ttf'
    alice_mask = np.array(PIL.Image.open('./data/zhu.png'))
    wordcloud=WordCloud(font_path=path,
                        background_color="white",
                        margin=5, width=1800, height=800, mask=alice_mask,
                        max_words=maxWords,
                        max_font_size=60,
                        random_state=42)
    wordcloud=wordcloud.generate(txt)
    wordcloud.to_file("./picture.jpg")
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


'''
添加停用词
'''
stopwords = pd.read_csv('./data/cn_stopwords.txt', engine='python',
                        encoding='utf-8', names=['stopwords'])['stopwords'].tolist()
book = open('./data/sanguo-utf8.txt', encoding='utf-8').read()

'''
分词
'''
def words_cut(book):
    words=list(jieba.cut(book))
    seg = set(words) - set(stopwords)
    result = [i for i in words if i in seg]
    return result
    


'''
nameList = ['曹操', '玄德', '孔明', '关公', '丞相', '孔明曰', '玄德曰', '云长',
						'张飞', '主公', '吕布', '刘备', '孙权', '赵云', '司马懿',
						'周瑜', '魏延', '袁绍', '马超', '姜维', '黄忠', '诸葛亮',
						'庞德', '张辽', '刘表', '董卓', '孙策', '鲁肃', '邓艾', '大将军',
						'张苞', '袁术', '刘玄德', '玄德大', '子龙', '司马', '孔明笑', '公瑾',
						'操大喜', '翼德', '刘皇叔', '赵子龙', '郭嘉', '仲达', '关云长',
						'操大怒', '玄德问', '阿斗', '刘豫州', '玄德闻', '玄德乃', '曹丞相'
						]  
'''

def main():
    a=[]
    '''
    ## 直接分词,不过滤停用词,并利用nameList直接过滤
    f=open(r'./data/sanguo-utf8.txt', 'rb').read()
    words=list(jieba.cut(f))
    '''
    words = words_cut(book)
    for word in words:
        if len(word)>1:
            a.append(word)

    txt=r' '.join(a)
    wordcloudplot(txt, 2000)

if __name__=='__main__':
    main()
