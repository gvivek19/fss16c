from __future__ import division
import math
import Sym

def max(x,y) : return x if x>y else y
def min(x,y) : return x if x<y else y

class Num:
    def __init__(i):
        i.mu,i.n,i.m2,i.up,i.lo = 0,0,0,-10e32,10e32
        i.binned = False
        i.symClass = Sym.Sym()
        i.values = []
        i.binMaps = {}
  
    def add(i,x):
        i.n += 1
        x = float(x)
        i.values.append(x)
        if x > i.up: i.up=x
        if x < i.lo: i.lo=x
        delta = x - i.mu
        i.mu += delta/i.n
        i.m2 += delta*(x - i.mu)
        return x 
    
    def sub(i,x):
        i.n   = max(0,i.n - 1)
        delta = x - i.mu
        i.mu  = max(0,i.mu - delta/i.n)
        i.m2  = max(0,i.m2 - delta*(x - i.mu))
        i.values.remove(x)
    
    def sd(i):
        return 0 if i.n < 2 else (i.m2/(i.n - 1))**0.5
    
    def show(i):
        if i.binned:
            i.symClass.show()
            return
        print "Mean : " + str(i.mu) + "\tStandard Deviation : " + str(i.sd())
        
    def norm(i, x):
        tmp= (x - i.lo) / (i.up - i.lo + 10**-32)
        if tmp > 1: return 1
        elif tmp < 0: return 0
        else: return tmp
        
    def dist(i,x,y):
        if i.binned:
            return i.symClass.dist(x, y)
        return i.norm(x) - i.norm(y)
  
    def furthest(i,x) :
        if i.binned:
            return i.symClass.furthest(x)
        return i.up if x <(i.up-i.lo)/2 else i.lo
        
    def like(i,x, prior):
        if i.binned:
            return i.symClass.like(x, prior)
        var   = i.sd()**2
        result = 1 if x == i.mu else 0.001
        if var != 0:
            denom = (2*math.pi*var)**.5
            num   = math.exp(-(x-i.mu)**2/(2*var))
            result = num / denom
            result = result if result < 1 else 1
        return result if result > 0 else 10**-32

    def discretize(self, policy, nbins):
        if policy == 'width':
            self.equalwidth(nbins)
        elif policy == 'frequency':
            self.equalfrequency(nbins)
        self.binned = True

    def equalwidth(self, nbins):
        binrange = (self.up - self.lo) / nbins
        for i in range(1, nbins + 1) :
            self.binMaps["bin" + str(i + 1)] =(i * binrange, (i + 1) * binrange - 1)
        print self.binMaps
        for val in self.values:
            binid = val // binrange + 1
            self.symClass.add("bin" + str(int(binid)))

    def equalfrequency(i, nbins):
        i.values = sorted(i.values)
        binn = i.n // nbins
        if binn * nbins != i.n :
            binn += 1

        binvalues = {}
        prev_val = i.values[0]
        cur_bin_freq = 0
        curBinId = 1
        i.symClass.add("bin" + str(curBinId))
        binvalues[curBinId] = [prev_val]
        for ind in range(1, i.n):
            current_val = i.values[ind]

            if ((current_val != prev_val) and (cur_bin_freq >= binn)):
                curBinId += 1
                cur_bin_freq = 0
                binvalues[curBinId] = []

            binvalues[curBinId].append(current_val)

            cur_bin_freq += 1
            i.symClass.add("bin" + str(curBinId))
            prev_val = current_val

        for k in range(0, curBinId):
            values = binvalues[k + 1]
            maxval = values[0]

            for l in values[1:]:
                if l > maxval :
                    maxval = l
            print k+1, maxval

            lowrange = 0 if k == 0 else i.binMaps["bin" + str(k)][1] + 1
            i.binMaps["bin" + str(k + 1)] = (lowrange, maxval)
        print i.binMaps