# cn_cheaker

A simple Chinese text error corrector.

一个简易中文文本纠错器

## Main component 主要组成部分
+ spell_checker.py --单个词语纠错(Single word corrector)
+ cn_cheaker.py --句子纠错(Sentence corrector)
+ radical.py --汉字部首拆分(Chinese character radical splitter)
+ ci_maker.py --词库整理(Chinese word dictionary organizer)(已经经过整理，暂不需要-It has been sorted and is not needed temporarily)
+ zi_data.txt --汉字字库(Chinese character dictionary)
+ cn_texts --汉语词语字典目录(Chinese word dictionary directory)
+ radical_data.csv --汉字部首数据(Chinese character radical data)

## How does it work 它是如何运作的
+ 1.分词(jieba)，寻找单个字，极有可能为错误部分(Separate words, look for single words, they are most likely to be the wrong part.)
+ 2.分成单个词语进行纠错(Split into single words for error correction.)
     - 从词库中选择候选字(Select candidate words from the dictionary.)
	 - 判断词库中是否存在这个词，存在则无需纠错(Judge whether the word exists in the dictionary. If it exists, there is no need to correct it.)
	 - 逐个匹配，取相似度最高的结果(Match one by one, take the result with the highest similarity.)
+ 3.最终输出结果(Print the result.)

## How to run it 如何运行此程序
运行 "cn_cheaker.py"，这是主程序。

Run "cn_cheaker.py", this is the main program.

## For example 运行示例
```
input: 你是以个学声.学系成绩不撮
你是一个学生.学习成绩不错
input: 这场体育竟赛能够充分展限同学们的风彩
这场体育竞赛能够充分展现同学们的风采
input: 济南的东天是没有风生的
济南的冬天是没有风声的
input: 仅天的天器怎么样
今天的天气怎么样
input: 我们虚要自觉的遵守规锭
我们需要自觉地遵守规定
```
