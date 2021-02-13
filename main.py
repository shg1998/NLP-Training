
import time
START = '<Start> '

isBackoffMode = False
isBigramMode = False
isUnigramMode = False

unigramDict = dict()
bigramDict = dict()
backoffDict = dict()


def CreateDictionary(fName):
    _dict = dict()
    fAddress = fName+".txt"
    fText = open(fAddress, "r", 1, "Utf-8")

    for fLine in fText:
        fLine = fLine.strip()
        words = fLine.split(" ")

        for w in words:
            if w in _dict:  # check for new word that has same word in dict or not!
                _dict[w] = _dict[w] + 1  # insert new word with its repeation!
            else:
                _dict[w] = 1
        # print(_dict)
    fText.close()

    if "ferdowsi" in fName:
        outF = open("./Dictionaries/ferdowsi.txt", "w", encoding='utf-8')
    elif "hafez" in fName:
        outF = open("./Dictionaries/hafez.txt", "w", encoding='utf-8')
    elif "molavi" in fName:
        outF = open("./Dictionaries/molavi.txt", "w", encoding='utf-8')

    dictt = dict()
    dictt = Cleaner(_dict)

    for value in dictt:
        outF.write(str(value)+" "+str(dictt[value]))
        outF.write("\n")
    outF.close()


def BigramModel(fName):

    fAddress = fName + ".txt"
    fText = open(fAddress, "r", 1, "Utf-8")

    for fLine in fText:
        fLine = fLine.strip()
        fLine = START + fLine  # for hiding spaces!
        words = fLine.split(" ")  # splitting text by Space

        for i in range(len(words)-1):
            w = words[i] + " " + words[i+1]  # dota dota

            if w in bigramDict:
                bigramDict[w] = bigramDict[w] + 1
            else:
                bigramDict[w] = 1

    fText.close()


def UnigramModel(fName):

    fAddress = fName+".txt"
    fText = open(fAddress, "r", 1, "Utf-8")

    for fLine in fText:
        fLine = fLine.strip()  # for hiding spaces!
        fLine = START + fLine
        words = fLine.split(" ")  # splitting text by Space

        for w in words:
            if w in unigramDict:
                unigramDict[w] = unigramDict[w] + 1
            else:
                unigramDict[w] = 1

    fText.close()


def BackoffModel(fileName):

    Landa1 = 0.4
    Landa2 = 0.2
    Landa3 = 0.4
    Epsilon = 0.2

    Uni_dict = unigramDict
    bi_dict = bigramDict
    for key, value in bi_dict.items():
        words = key.split(' ')
        backoffDict[key] = (value * Landa3) + \
            (Uni_dict[words[0]] * Landa2) + (Landa1 * Epsilon)


def Cleaner(dictionary):
    dictt = dict()
    for key, value in dictionary.items():

        if value >= 2:
            dictt[key] = value
    return dictt


def unigram_Accuracy(fLine):
    fLine = fLine.strip()
    fLine = START + fLine
    words = fLine.split(" ")
    unigramACC = 1
    for word in words:
        if(word in unigramDict):
            unigramACC = (unigramDict[word]/sum(unigramDict.values()))
    return unigramACC


def bigram_Accuracy(fLine):
    fLine = fLine.strip()
    fLine = START + fLine
    words = fLine.split(" ")
    bigramACC = 1
    for i in range(len(words)-1):
        word = words[i] + " " + words[i+1]
        if(word in bigramDict):
            bigramACC = (bigramDict[word] /
                         sum(bigramDict.values()))
    return bigramACC


def backoff_Accuracy(fLine):
    fLine = fLine.strip()
    fLine = START + fLine
    words = fLine.split(" ")
    backoffACC = 1
    for i in range(len(words)-1):
        word = words[i] + " " + words[i+1]
        if(word in backoffDict):
            backoffACC = (backoffDict[word]/sum(backoffDict.values()))

    return backoffACC


def getAccuracy(fName, Mode):

    file = fName + ".txt"
    text = open(file, "r", 1, "Utf-8")
    filename = fName+"Accuracy" + ".txt"
    fWrite = open(filename, "w", 1, "Utf-8")
    AccList = list()
    unigram_Accuracy_1 = float()
    for l in text:
        words = l.split('\t')
        if Mode == 1:
            unigram_Accuracy_1 = unigram_Accuracy(words[1])
            AccList.append((unigram_Accuracy_1 * 100))
            # fWrite.write(str(unigram_Accuracy_1)+" %" +
            #            "   =================>   "+l)

        elif Mode == 2:
            bigram_Accuracy_1 = bigram_Accuracy(words[1])
            AccList.append((bigram_Accuracy_1 * 100))
            # fWrite.write(str(bigram_Accuracy_1)+" %" +
            #            "   =================>   "+l)
        elif Mode == 3:
            backoff_Accuracy_1 = backoff_Accuracy(words[1]) * 100
            AccList.append((backoff_Accuracy_1 * 100))
            # print(backoff_Accuracy_1)  # for test! :)
            # fWrite.write(str(backoff_Accuracy_1)+" %" +
            #            "   =================>   "+l)

    fWrite.close()  # close File
    return AccList


def Menu1():
    print("choose Shaer: ")
    print("1- ferdowsi")
    print("2- hafez")
    print("3- molavi")


def Menu2():
    print("choose Accuracy Type: ")
    print("1- Unigram")
    print("2- Bigram")
    print("3- Backoff")


def Static4Ferdowsi():
    CreateDictionary("./train_set/ferdowsi_train")
    UnigramModel("./train_set/ferdowsi_train")
    BigramModel("./train_set/ferdowsi_train")
    BackoffModel("./train_set/ferdowsi_train")


def Static4Hafez():
    CreateDictionary("./train_set/hafez_train")
    UnigramModel("./train_set/hafez_train")
    BigramModel("./train_set/hafez_train")
    BackoffModel("./train_set/hafez_train")


def Static4Molavi():
    CreateDictionary("./train_set/molavi_train")
    UnigramModel("./train_set/molavi_train")
    BigramModel("./train_set/molavi_train")
    BackoffModel("./train_set/molavi_train")


def main():

    start_time = time.time()
    print("running ... ")

    ferdowsiAccuracyList = list()
    hafezAccuracyList = list()
    molaviAccuracyList = list()
    ConcreteAccuracy = list()
    ShaerList = list()

    Menu2()
    AccuracyMode = int(input())

    print("Calculating Accuracy of each Shaer ... ")

    Static4Ferdowsi()
    ferdowsiAccuracyList = getAccuracy("./test_set/test_file", AccuracyMode)

    Static4Hafez()
    hafezAccuracyList = getAccuracy("./test_set/test_file", AccuracyMode)

    Static4Molavi()
    molaviAccuracyList = getAccuracy("./test_set/test_file", AccuracyMode)

    # print(ferdowsiAccuracyList)
    # print(hafezAccuracyList)
    # print(molaviAccuracyList)

    print("Calculating total Accuracy  ... ")
    for i in range(len(ferdowsiAccuracyList)):
        dummy = [ferdowsiAccuracyList[i],
                 hafezAccuracyList[i], molaviAccuracyList[i]]
        ConcreteAccuracy.append(max(dummy))
        if ConcreteAccuracy[i] == ferdowsiAccuracyList[i]:
            ShaerList.append("ferdowsi")
        elif ConcreteAccuracy[i] == hafezAccuracyList[i]:
            ShaerList.append("hafez")
        elif ConcreteAccuracy[i] == molaviAccuracyList[i]:
            ShaerList.append("molavi")

    file = "./test_set/test_file" + ".txt"
    text = open(file, "r", 1, "Utf-8")
    filename = "./test_set/test_file"+"Accuracy" + ".txt"
    fWrite = open(filename, "w", 1, "Utf-8")
    i = 0
    lineCounter = 0
    TrueResult = 0
    for l in text:
        if i < len(ConcreteAccuracy):
            if l[0] == "1":
                if ShaerList[i] == "ferdowsi":
                    TrueResult += 1
            if l[0] == "2":
                if ShaerList[i] == "hafez":
                    TrueResult += 1
            if l[0] == "3":
                if ShaerList[i] == "molavi":
                    TrueResult += 1
            fWrite.write(str(ConcreteAccuracy[i])+" %     &    " + ShaerList[i] +
                         "   =================>   "+l)
            i += 1
        lineCounter += 1
    print(str(TrueResult) + " s s "+str(lineCounter))
    totalACC = TrueResult/lineCounter
    elapsed_time = time.time() - start_time
    print("totla Accuracy is : "+str(totalACC))
    print("operations done in "+str(elapsed_time) + " s")
    print("result is in test_fileAccuracy file :)")

if __name__ == "__main__":
    main()
