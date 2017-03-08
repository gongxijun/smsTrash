# !/usr/bin/env python
# coding:utf-8
import mmseg
import codecs


class Bayes:
    def __init__(self):
        self.sms_count = [0, 0];  # [spam.ham]
        self.sms_value = {};

    def input_raw(self, sentence, is_spam):
        """
        训练数据
        :param sentence: 训练的句子
        :param is_spam: 是否时垃圾短信
        :return:
        """
        sms = mmseg.seg_txt(sentence)
        sms = list(sms)
        for flag, word in enumerate(sms):
            offset = 0 if is_spam else 1;
            if word not in self.sms_value:
                self.sms_value[word] = [1 - offset, offset]
            else:
                self.sms_value[word][offset] += 1;
            self.sms_count[offset] += 1

    def predict(self, sentence):
        def is_zero(value):
            return value if value > 0 else 0.01;

        sms = mmseg.seg_txt(sentence)
        sms = set(sms)
        sms_prob_ham = sms_prob_spam = 1
        for flag, word in enumerate(sms):
            word_prob_spam = word_prob_ham = 0;
            if word in self.sms_value:
                value = self.sms_value[word]
                word_prob_spam = float(value[0]) / self.sms_count[0]  # 这个词为spam的概率
                word_prob_ham = float(value[1]) / self.sms_count[1]  # 这个词为healthy的概率
            word_prob_spam = is_zero(word_prob_spam);
            word_prob_ham = is_zero(word_prob_ham);
            ##计算
            prob_is_spam = word_prob_spam / (word_prob_spam + word_prob_ham)  # 其中word_prob_ham为补集
            sms_prob_spam *= prob_is_spam
            sms_prob_ham *= (1 - prob_is_spam)
        return sms_prob_spam / (sms_prob_spam + sms_prob_ham)

    def train(self, path):
        for sms_line in codecs.open(path, 'r'):
            smdet = sms_line.split("\t");
            text_sms = smdet[-1].strip("\n");
            sms_type = smdet[0].strip("\n");
            self.input_raw(text_sms, False if sms_type == "spam" else True)
        return;


if __name__ == "__main__":
    test_sms = ['Rofl. Its true to its name',
                'Free Msg: Ringtone!From: http://tms. widelive.com/index. wml?id=1b6a5ecef91ff9*37819&first=true18:0430-JUL-05',
                '龚细军', 'speak haha', 'helo,there is a ads']
    badfile = "sms.txt"
    bayes = Bayes()
    bayes.train(badfile)
    for w in test_sms:
        pct = bayes.predict(w)
        print w + ">>>>>>|| result( prob spam ): --> " + str(pct)
