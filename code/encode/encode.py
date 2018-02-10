# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
from datetime import datetime
from scipy.sparse import csc_matrix
from scipy.sparse import save_npz

from scipy.sparse import load_npz
startTime = datetime.now()


string1 = """SGSWLRDVWDWICTVLTDFKTWLQSKLLPRLPGVPFLSCQRGYKGVWRGDGIMQTTCPCGAQIAGHVKNGSMRIVGPKTC
SNTWHGTFPINAYTTGPCVPSPAPNYSKALWRVAAEEYVEVTRVGDFHYVTGMTTDNIKCPCQVPAPEFFTEVDGVRLHR
YAPACKPLLREEVTFQVGLNQYLVGSQLPCEPEPDVTVLTSMLSDPSHITAETAKRRLARGSPPSLASSSASQLSAPSLK
ATCTTHHDSPDADLIEANLLWRQEMGGNITRVESENKVVILDSFDPLRAEEGEREISVPAEILRKTRKFPPAMPIWARPD
YNPPLIESWKHPDYVPPVVHGCPLPATKAPPIPPPRRKRTVVLTESTVSSALAELATKTFGSSESSAVDSGTATAPLDQP
SDAGDTGSDVESYSSMPPLEGEPGDPDLSDGSWSTVSEEASEDVVCC"""

string2 = """SGSWLRDVWDWICTVLTDFKTWLQSKLLPRLPGVPFLSCQRGYKGVWRGDGIMQTTCPCGAQIAGHVKNGSMRIVGPKTC
SNTWHGTFPINAYTTGPCVPSPAPNYSKALWRVAAEEYVEVTRVGDFHYVTGMTTDNIKCPCQVPAPEFFTEVDGVRLHR
YAPACKPLLREEVTFQVGLNQYLVGSQLPCEPEPDVTVLTSMLSDPSHITAETAKRRLARGSPPSLASSSASQLSAPSLK
ATCTTHHDSPDADLIEANLLWRQEMGGNITRVESENKVVILDSFDPLRAEEGEREISVPAEILRKTRKFPPAMPIWARPD
YNPPLIESWKHPDYVPPVVHGCPLPATKAPPIPPPRRKRTVVLTESTVSSALAELATKTFGSSESSAVDSGTATAPLDQP
PDAGDTGSDVESYSSMPPLEGEPGDPDLSDGSWSTVSEEASEDVVCC"""

string4 = "1234512"
string3 = "abcdeab"

string5 = "abcdeabc"
seqList = [string1, string2, string3, string4, string5]


sizeOfSubstr = (1,2,3)
numOfSeq = len(seqList)
listSubString = [] #list of substrings or list of feature
encodingMat= np.zeros((0,numOfSeq), dtype = 'uint8') #dòng là feature(substr), cột là seq

for sizeOfSub in sizeOfSubstr: #số lượng kí tự của substr
    curNumOfFeature = len(listSubString)
    startIndexOfCurSize = curNumOfFeature
    
    for indexOfCurSeq in xrange(0,numOfSeq): #duyệt từng sequence
        seq = seqList[indexOfCurSeq]
        sizeOfSeq = len(seq)

        for index in xrange(0,sizeOfSeq-sizeOfSub+1): # duyệt substr
            curSubStr = seq[index: index+sizeOfSub]
            try:
                #chỉ tìm trong các sub string có cùng số lượng kí tự nên có startIndexOfCurSize
                foundIndexOfFeature = listSubString.index(curSubStr, startIndexOfCurSize)
                #nếu có cho thêm sửa value trong matrix
                encodingMat[foundIndexOfFeature][indexOfCurSeq] += 1
            except ValueError:
                #nếu không tìm được
                #thêm feature vào list
                listSubString.append(curSubStr)
                #tạo thêm dòng feature trong matrix
                #tạo row
                newRowFeature = np.zeros((numOfSeq), dtype='uint8')
                #sửa gtri feature trong dòng của seq tạo ra feature mới này
                newRowFeature[indexOfCurSeq] += 1 
                #add row vào trong matrix
                encodingMat = np.vstack([encodingMat, newRowFeature])
                
#save mat by numpy
np.save('output1',encodingMat)
readMat1 = np.load('output1.npy')


#save sparse Mat to .npz file by scipy.sparse lib
sparseMat = csc_matrix(encodingMat)
save_npz('output', sparseMat)


readMat = load_npz('output.npz')
readMat = readMat.todense()



print datetime.now() - startTime
