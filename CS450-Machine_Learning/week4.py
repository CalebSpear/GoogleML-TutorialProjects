import numpy as np

def calc_entropy(p):
    
    if p != 0:
        return -p * np.log2(p)
    else:
        return 0
        
def info_gain(data,classes,feature):
    gain = 0 
    nData = len(data)
    
    values = []
    for datapoint in data:
        if datapoint[feature] not in values:
            values.append(datapoint[feature])
    
    featureCounts = np.zeros(len(values))
    entropy = np.zeros(len(values)) 
    valueIndex = 0
    
    for value in values:
        dataIndex = 0
        newClasses = []
        for datapoint in data:
            if datapoint[feature] == value:
                featureCounts[valueIndex] += 1
                newClasses.append(classes[dataIndex])
            dataIndex += 1
            
        classValues = []
        for aclass in newClasses:
            if classValues.count(aclass) == 0:
                classValues.append(aclass)
                
        classCounts = np.zeros(len(classValues))
        classIndex = 0
        for classValue in classValues:
            for aclass in newClasses:
                if aclass == classValue:
                    classCounts[classIndex] += 1
            classIndex += 1
        
        for classIndex in range(len(classValues)):
            entropy[valueIndex] += calc_entropy(float(classCounts[classIndex])/sum(classCounts))
        gain += float(featureCounts[valueIndex])/nData * entropy[valueIndex]
        valueIndex += 1
    return gain
    
def make_tree(data,classes,featureNames):
    default = classes[np.argmax(frequency)]
    if nData == 0 or nFeatures == 0:
        return default
    elif classes.count(classes[0]) == nData:
        return classes[0]
    else:
        gain = np.zeros(nFeatures)
        for feature in range(nFeatures):
            g = info_gain(data,classes,feature)
            gain[feature] = totalEntropy - g
        bestFeature = np.argmax(gain)
        tree = {featureNames[bestFeature]:{}}
        
        for value in values:
            for datapoint in data:
                if datapoint[bestFeature] == value:
                    if bestFeature == 0:
                        datapoint = datapoint[1:]
                        newNames = featureNames[1:]
                    elif bestFeature == nFeatures:
                        datapoint = datapoint[:-1]
                        newNames = featureNames[:-1]
                    else:
                        datapoint = datapoint[:bestFeature]
                        datapoint.extend(datapoint[bestFeature+1:])
                        newNames = featureNames[:bestFeature]
                        newNames.extend(featureNames[bestFeature+1:])
                    newData.append(datapoint)
                    newClasses.append(classes[index])
                index += 1
            
            subtree = make_tree(newData,newClasses,newNames)
            
            tree[featureNames[bestFeature]][value] = subtree
        return tree