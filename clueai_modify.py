import clueai
# initialize the clueai Client with an API Key
cl = clueai.Client('K3Io6qzMNDreOFr1X2bzG1101110010')
def modify(txt):
    pre = "生成与下列文字相同意思的句子：\n"
    prompt = pre + txt
    # # generate a prediction for input txt
    prediction = cl.generate(
        model_name='clueai-large',
        prompt=prompt)
    print("答案：{}".format(prediction.generations[0].text))

if __name__ == '__main__':
    modify("我觉得洛杉矶湖人这个赛季能夺冠")