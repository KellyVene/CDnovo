func = {'norm': stats.norm, 'expon': stats.expon, 'uniform': stats.uniform, 't': stats.t, 
        'chi2': stats.chi2, 'f': stats.f, 'gamma': stats.gamma, 'beta': stats.beta}

#Se n�o visualizar o pywidgets:
#conda install -c conda-forge ipywidgets

#Fun��o que utiliza o pywidget
@interact(n = (1, 20, 1), distribui��o = sorted(list(func.keys())))
def f(distribui��o = 'norm', n = 1):
    
    size = 1000
    loc = 0
    scale = 1
    
    arg = {'loc': loc, 'scale': scale, 'size': size}
    
    #Cada distribui��o tem seu conjunto de par�metros espec�ficos
    if distribui��o == 't':
        arg['df'] = 5
    elif distribui��o == 'chi2':
        arg['df'] = 5
    elif distribui��o == 'f':
        arg['dfn'] = 5
        arg['dfd'] = 7
    elif distribui��o == 'gamma':
        arg['a'] = 1
    elif distribui��o == 'beta':
        arg['a'] = 0.5
        arg['b'] = 0.5
    
    #Gerar n vetores de 1000 amostras cada
    Xb = func[distribui��o].rvs(**arg)
    for i in range(n-1):
        Xb += func[distribui��o].rvs(**arg)
        
    #Calcular a m�dia
    Xb = Xb / n
    
    #Prints
    fig = plt.figure(figsize=(10,4))
    
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    
    #Histograma
    pd.Series(Xb).hist(normed=True, ax=ax1)
    
    #Fit e print da pdf
    (mu, sigma) = stats.norm.fit(Xb)
    x = np.arange(Xb.min(), Xb.max(), 0.01)
    ax1.plot(x, stats.norm.pdf(x, loc = mu, scale=sigma))
    
    #QQ-Plot
    stats.probplot(Xb, dist=stats.norm, sparams=(mu, sigma), plot=ax2)
    
    return "M�dia Amostral: {0:0.2f}, Desvio Padr�o Amostral: {1:0.2f}\n".format(Xb.mean(),Xb.std())