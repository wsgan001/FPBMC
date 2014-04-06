# -*- coding: utf-8 -*-
'''
Created on 2014年3月28日

@author: ZhuJiahui506
'''
import os
import time
import numpy as np
from TextToolkit import get_text_to_single_list, quick_write_list_to_text,\
    get_text_to_complex_list


'''
Step 14 - 2
Query evaluation using Precision Recall and F measure.  7 clusters
This is our result.
'''

def classification_evaluate(read_filename1, read_filename2, write_directory):
    
    # string类型二维列表
    classification_result = []
    get_text_to_complex_list(classification_result, read_filename1, 0)
    
    # string类型
    real_tag = []
    get_text_to_single_list(real_tag, read_filename2)
    
    # 需要手动录入
    class_tag = ['2', '3', '6', '1', '5', '7', '4']
    class_tag2 = ['2', '3', '8', '1', '5', '7', '4']
    
    precision_list = []
    recall_list = []
    fmeasure_list = []
    for i in range(len(class_tag)):
        real_classification = []
        for j in range(len(real_tag)):
            # 检索6和8为一类
            if real_tag[j] == class_tag[i] or real_tag[j] == class_tag2[i]:
                real_classification.append(str(j))
        
        correct = len(set(classification_result[i]) & set(real_classification))
        this_precision = np.true_divide(correct, len(set(classification_result[i])))
        this_recall = np.true_divide(correct, len(set(real_classification)))
        this_fmeasure = np.true_divide(2.0 * this_precision * this_recall, (this_precision + this_recall))
        
        print this_precision, this_recall, this_fmeasure

        precision_list.append(str(this_precision))
        recall_list.append(str(this_recall))
        fmeasure_list.append(str(this_fmeasure))
    
    average_precision = np.average([float(x) for x in precision_list])
    average_recall = np.average([float(x) for x in recall_list])
    average_fmeasure = np.average([float(x) for x in fmeasure_list])
    print 'Average:', average_precision, average_recall, average_fmeasure
    quick_write_list_to_text(precision_list, write_directory + u'/precision.txt')
    quick_write_list_to_text(recall_list, write_directory + u'/recall.txt')
    quick_write_list_to_text(fmeasure_list, write_directory + u'/fmeasure.txt')

if __name__ == '__main__':
    start = time.clock()
    now_directory = os.getcwd()
    root_directory = os.path.dirname(now_directory) + '/'
    
    read_filename1 = root_directory + u'dataset/cluster7/classification_result.txt'
    read_filename2 = root_directory + u'dataset/global/weibo_class_tag.txt'
    
    write_directory = root_directory + u'dataset/cluster7'
    
    if (not(os.path.exists(write_directory))):
        os.mkdir(write_directory)

    classification_evaluate(read_filename1, read_filename2, write_directory)
       
    print 'Total time %f seconds' % (time.clock() - start)
    print 'Complete !!!'