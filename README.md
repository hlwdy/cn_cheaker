# cn_cheaker

A simple Chinese text error corrector.
一个简易中文文本纠错器

## Main component 主要组成部分
+ spell_checker.py --单个词语纠错(Single word corrector)
+ cn_cheaker.py --句子纠错(Sentence corrector)
+ radical.py --汉字部首拆分(Chinese character radical splitter)
+ zi_data.txt --汉字字库(Chinese character dictionary)
+ cn_texts --汉语词语字典目录(Chinese word dictionary directory)

## How does it work 它是如何运作的
+ 1.分词(jieba)，寻找单个字，极有可能为错误部分(Separate words, look for single words, they are most likely to be the wrong part.)
+ 2.分成单个词语进行纠错(Split into single words for error correction.)
+ 3.最终输出结果(Print the result.)

## How to run it 如何运行此程序
运行 "cn_cheaker.py"，这是主程序。
Run "cn_cheaker.py", this is the main program.
