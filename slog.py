import matplotlib.pyplot as plt 

def symp(data,x_scale,y_scale):
    plt.plot(data[0],data[1])
    plt.xscale(x_scale)
    plt.yscale(y_scale)
    plt.show()

def main():
    # symp(data,'symlog','symlog')
    pass

if __name__ == '__main__':
    main()
