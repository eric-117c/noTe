# 大模型概述和tokenization

## 课程宗旨
- 观点：understanding via building

## 一些例子
- attn层的FLOPs vs MLP层的FLOPs
  - 小模型时两者数量基本相当
  - 规模扩大后，MLP中的数量占据主导地位
  - 因此，优化中更注重优化MLP层
  - 注释：
    - FLOPs（float point operations）：浮点运算数
    - attn（attention）：注意力
    - MLP(multilayer perception):多层感知器
- 涌现行为（emergence of behavior with scale）[Jason Wei+,2022]
  - 模型在一个规模以下时，各项指标增长极其缓慢
  - 当跨越这个数值后，指标增长及其迅速
  
## 介绍
- 这门课学什么
  - 运作机制
  - 思维方式
  - 直觉
  
## Overview
- 基础原理 (Basics)： 涵盖 Transformer 架构、自注意力机制、词嵌入与分词技术等底层逻辑。

- 系统工程 (Systems)： 探讨分布式训练集群、GPU 算力优化、显存管理以及高性能推理框架。

- 缩放法则 (Scaling Laws)： 研究计算量、模型参数量与数据量之间的定量关系及性能预测。

- 数据工程 (Data)： 涉及海量语料的清洗、去重、质量评估以及指令微调数据的构造。

- 模型对齐 (Alignment)： 聚焦 RLHF（人类反馈强化学习）、安全性护栏以及确保模型输出符合人类价值观。

## Tokenization
- 原始文本通常以Unicode来编码
- 比如，string = "Hello,:earth_africa:!你好!"
<br>

- 语言模型会在一系列分词分布一定的概率，通常用整数表示
- 比如，indices = [15496,11,995,0]
<br>

- 因此,会需要一个程序把 string **编码**（encode）成 token
- 此外,还需要一个程序把 token **解码**（decode）成 string 
<br>

- Tokenizer是一个实现解码和编码的一个class
- 你的**词汇表大小**(vocabulary size)就是token值的上限
<br>

- 尝试一下，看看 tokenizer 是怎么工作的
- https://tiktokenizer.vercel.app/?encoder=gpt2
- 一些观察：
  - 空格也是 token 的一部分，通常出现在token的前面
  - 因此，`hello`和` hello`会被分配到不同的 token 
  - 以 gpt-4o 为例，前者是`24912`,而后者是`40617`
  - 连续的数字不是作为一个整体，而是**从左至右**以三个数字为一个整体分配 token 

### Character-based tokenization
- idea: a unicode string is a sequence of unicode characters
- 所以，根据这个idea，charcter可以通过`ord`转换为integer，integer也可以通过`chr`转换为character

### Byte-based tokenization
- idea: unicode string can also be repesented by integers(from 0 to 255)
- most common one is UTF-8
- 在处理长序列时，会得到很长的token list

### Word-based tokenization
- vocabulary size 可能无穷大

### Byte pair Encoding
- Basic Idea:把数据喂给分词器让分词器自动生成词汇表
- Intuition:常见的字符序列用一个token表示，罕见的序列用多个token表示
- Training Algorithm:
```python
def train_bpe(string: str, num_merges: int) -> BPETokenizerParams:  # @inspect string, @inspect num_merges
    # Start with the list of bytes of string.

    indices = list(map(int, string.encode("utf-8")))  
    # @inspect indices

    merges: dict[tuple[int, int], int] = {}  # index1, index2 => merged index
    vocab: dict[int, bytes] = {x: bytes([x]) for x in range(256)}  # index -> bytes

    for i in range(num_merges):

       # Count the number of occurrences of each pair of tokens
        counts = defaultdict(int)
        for index1, index2 in zip(indices, indices[1:]):  # For each adjacent pair
            counts[(index1, index2)] += 1  # @inspect counts

        # Find the most common pair.
        pair = max(counts, key=counts.get)  # @inspect pair
        index1, index2 = pair

        # Merge that pair.
        new_index = 256 + i  # @inspect new_index
        merges[pair] = new_index  # @inspect merges
        vocab[new_index] = vocab[index1] + vocab[index2]  # @inspect vocab
        indices = merge(indices, pair, new_index)  # @inspect indices
    
    return BPETokenizerParams(vocab=vocab, merges=merges)
```
## Summary
- Tokenizer: strings <-> tokens (indices)
- Character-based, byte-based, word-based tokenization highly suboptimal
- BPE is an effective heuristic that looks at corpus statistics
- Tokenization is a necessary evil, maybe one day we'll just do it from bytes...