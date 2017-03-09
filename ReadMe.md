关于贝叶斯二择一形式公式的几点说明:      
1.普通的贝叶斯公式：     
<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/71d8066a406fb22ce08eec25dd04870779345cd3" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -2.671ex; width:25.215ex; height:6.509ex;" alt="P(A|B)={\frac {P(B|A)\,P(A)}{P(B)}}">   
2.二择一形式:   
<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/4da5a989fc6ee3c6ece9478f476af4a1e98db269" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; width:64.285ex; height:3.176ex;" alt="P(B)=P(A,B)+P(A^{C},B)=P(B|A)P(A)+P(B|A^{C})P(A^{C})">  
其中Ａ^C为Ａ的补集,也可以这样理解成(1-A),结合以上1,2两个式子，我们可以得到下面这个式子３  
3. 二分类中的式子：   
<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/03c8d4c9b009705e33ae35317f3c7ae6e1d03485" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -2.671ex; margin-right: -0.229ex; width:45.31ex; height:6.509ex;" alt="P(A|B)={\frac {P(B|A)\,P(A)}{P(B|A)P(A)+P(B|A^{C})P(A^{C})}}.,\!">    
但是上面这个式子明显是在两个条件的一个贝叶斯概率计算情况,但是在一般情况下,都不是两个,这个可以扩展到N个条件下,预测贝叶斯概率事件,推倒一般公式，我们可以先从三个条件的开始.:   
4 推倒过程:   
  P(C|AB)=P(AB|C)*P(C)/P(AB)   (4.1)  
  P(AB|C) = P(A|C)*P(B|C)      (4.2)  
  P(AB) = P(A)*P(B)            (4.3)  
  从上面4.1,4.2,4.3三个式子中,我们就可以将一个三个条件的降为多个两个条件的贝叶斯概率事件了.  
  P(C|AB) = {P(C)P(A|C)*P(B|C)}/{P(A)*P(B)}  
,我们在将其写成一般式子   
P(C|ＥAi) = {P(C)P(ＥAi|C)}/{P(ＥAi)},然后我们将这个式子代入到我们的计算中,就可以用来简单的预测短信是否是垃圾信息啦～     
  5.　关于数据集合,从这个地址地方下载的http://archive.ics.uci.edu/ml/  
  6.　结果展示:     
Rofl. Its true to its name>>>>>>|| result( prob spam ): --> 0.15844183241   
Free Msg: Ringtone!From: http://tms. widelive.com/index. wml?id=1b6a5ecef91ff9*37819&first=true18:0430-JUL-05>>>>>>|| result( prob spam ): --> 1.0   
龚细军>>>>>>|| result( prob spam ): --> 0.5  
speak haha>>>>>>|| result( prob spam ): --> 0.00302526687657   
helo,there is a ads>>>>>>|| result( prob spam ): --> 0.997563452806    
