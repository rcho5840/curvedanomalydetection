import matplotlib.pyplot as plt

def cnnvisualization(hist, param1, title1, param2, title2, maintitle):
      
    
    fig = plt.figure()
    plt.plot(hist.history[param1], color = 'blue', label = title1)
    plt.plot(hist.history[param2], color = 'teal', label = title2)
    fig.suptitle(maintitle, fontsize = 20)
    plt.legend(loc = "upper left")
    plt.show()
