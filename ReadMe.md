贝叶斯概率统计之二择一情况.  
贝叶斯一般形式  
1. P(A|B)=P(B|A)*P(A)/P(B)  
二择一形式：  

P(B)=P(A,B)+P(A^{C},B)=P(B|A)P(A)+P(B|A^{C})P(A^{C})，  
其中AC是A的补集（即非A）。故上式亦可写成：
{\displaystyle P(A|B)={\frac {P(B|A)\,P(A)}{P(B|A)P(A)+P(B|A^{C})P(A^{C})}}.,\!} P(A|B)={\frac {P(B|A)\,P(A)}{P(B|A)P(A)+P(B|A^{C})P(A^{C})}}.,\!
在更一般化的情况，假设{Ai}是事件集合里的部分集合，对于任意的Ai，贝叶斯定理可用下式表示：     
{\displaystyle P(A_{i}|B)={\frac {P(B|A_{i})\,P(A_{i})}{\sum _{j}P(B|A_{j})\,P(A_{j})}},\!} P(A_{i}|B)={\frac {P(B|A_{i})\,P(A_{i})}{\sum _{j}P(B|A_{j})\,P(A_{j})}},\!