thresholds = np.arange(70)

def heavyside(actual):
    return thresholds > actual

def is_cdf_valid(case):
    if case[0] < 0 or case[0] > 1:
        return False
    for i in xrange(1, len(case)):
        if case[i] > 1 or case[i] < case[i-1]:
            return False
    return True

def calc_crps(predictions, actuals):
    #some vector algebra for speed
    obscdf = np.array([heavyside(i) for i in actuals])
    crps = mean(mean((predictions - obscdf) ** 2))
    return crps

def CRPS(predictions, actuals):
    
    check = True
    '''
    for p in predictions :
        if is_cdf_valid(p) == False : 
            print 'something wrong with your prediction'
            check = False
            break
    '''
    if check == True : 
         return calc_crps(predictions, actuals)
         
###example of usage
predictions = np.ones((train.shape[0],70))
print CRPS(predictions, train.Expected)
