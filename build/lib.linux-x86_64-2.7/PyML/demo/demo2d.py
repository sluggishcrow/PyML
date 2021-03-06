import numpy
from numpy import arange

import matplotlib
from matplotlib import pylab


pylab.rcParams['contour.negative_linestyle'] = 'solid'
from PyML.containers.vectorDatasets import VectorDataSet, PyVectorDataSet
from PyML.containers.labels import Labels

"""
demo2d:  display decision boundaries and contours of the decision function
of a classifier on two dimensional data.
it usually works with the latest version of matplotlib.

USAGE::

  first you need to generate some data; you need to call
  demo2d.getData() 
  data is generated by clicking '1' or '2' at positions on the figure
  where you want your data points to be.
  click 'q' when you're done.
  demo2d.decisionSurface(classifier) then plots the decision boundary and
  contours of the decision function of the given classifier on the data
  that was generated.
  demo2d.decisionSurface can be called several times using different classifiers.
"""

X = []
Y = []
# plotStr = ['or', 'ob']
plotStr = ['or', '+b']
xmin = -1
xmax = 1
ymin = -1
ymax = 1
numpy_container = False


def pick(event):
    global data
    global X
    global Y
    global numpy_container
    if event.key == 'q':
        if len(X) == 0: return
        if not numpy_container:
            data = VectorDataSet(X)
        else:
            data = PyVectorDataSet(numpy.array(X))
        data.attachLabels(Labels(Y))
        X = []
        Y = []
        print 'done creating data.  close this window and use the decisionSurface function'
        pylab.disconnect(binding_id)
    if event.key == '1' or event.key == '2':
        if event.inaxes is not None:
            print 'data coords', event.xdata, event.ydata
            X.append([event.xdata, event.ydata])
            Y.append(event.key)
            pylab.plot([event.xdata], [event.ydata],
                       plotStr[int(event.key) - 1])
            pylab.draw()


def getData(**args):
    global numpy_container
    numpy_container = False
    if 'numpy_container' in args:
        numpy_container = args['numpy_container']
    pylab.subplot(111)
    pylab.plot([xmin, xmin, xmax, xmax], [ymin, ymax, ymin, ymax], '.k')
    pylab.title("press the numbers 1 or 2 to generate data points and 'q' to quit")
    global binding_id
    binding_id = pylab.connect('key_press_event', pick)
    pylab.show()


def setData(data_):
    global data

    data = data_


def scatter(data, **args):
    markersize = 5
    if 'markersize' in args:
        markersize = args['markersize']
    features = [0, 1]
    if 'features' in args:
        features = args['features']
    for c in range(data.labels.numClasses):
        x1 = []
        x2 = []
        for p in data.labels.classes[c]:
            x = data.getPattern(p)
            x1.append(x[features[0]])
            x2.append(x[features[1]])
        pylab.plot(x1, x2, plotStr[c], markersize=markersize)


def decisionSurface(classifier, fileName=None, **args):
    global data
    global numpy_container
    classifier.train(data)

    numContours = 3
    if 'numContours' in args:
        numContours = args['numContours']
    title = None
    if 'title' in args:
        title = args['title']
    markersize = 5
    fontsize = 'medium'
    if 'markersize' in args:
        markersize = args['markersize']
    if 'fontsize' in args:
        fontsize = args['fontsize']
    contourFontsize = 10
    if 'contourFontsize' in args:
        contourFontsize = args['contourFontsize']
    showColorbar = False
    if 'showColorbar' in args:
        showColorbar = args['showColorbar']
    show = True
    if fileName is not None:
        show = False
    if 'show' in args:
        show = args['show']

    # setting up the grid
    delta = 0.01
    if 'delta' in args:
        delta = args['delta']

    x = arange(xmin, xmax, delta)
    y = arange(ymin, ymax, delta)

    Z = numpy.zeros((len(x), len(y)), numpy.float)
    gridX = numpy.zeros((len(x) * len(y), 2), numpy.float)
    n = 0
    for i in range(len(x)):
        for j in range(len(y)):
            gridX[n][0] = x[i]
            gridX[n][1] = y[j]
            n += 1

    if not numpy_container:
        gridData = VectorDataSet(gridX)
        gridData.attachKernel(data.kernel)
    else:
        gridData = PyVectorDataSet(gridX)
    results = classifier.test(gridData)

    n = 0
    for i in range(len(x)):
        for j in range(len(y)):
            Z[i][j] = results.decisionFunc[n]
            n += 1

    #pylab.figure()
    im = pylab.imshow(numpy.transpose(Z),
                      interpolation='bilinear', origin='lower',
                      cmap=pylab.cm.gray, extent=(xmin, xmax, ymin, ymax))

    if numContours == 1:
        C = pylab.contour(numpy.transpose(Z),
                          [0],
                          origin='lower',
                          linewidths=(3),
                          colors='black',
                          extent=(xmin, xmax, ymin, ymax))
    elif numContours == 3:
        C = pylab.contour(numpy.transpose(Z),
                          [-1, 0, 1],
                          origin='lower',
                          linewidths=(1, 3, 1),
                          colors='black',
                          extent=(xmin, xmax, ymin, ymax))
    else:
        C = pylab.contour(numpy.transpose(Z),
                          numContours,
                          origin='lower',
                          linewidths=2,
                          extent=(xmin, xmax, ymin, ymax))

    pylab.clabel(C,
                 inline=1,
                 fmt='%1.1f',
                 fontsize=contourFontsize)

    # plot the data
    scatter(data, markersize=markersize)
    xticklabels = pylab.getp(pylab.gca(), 'xticklabels')
    yticklabels = pylab.getp(pylab.gca(), 'yticklabels')
    pylab.setp(xticklabels, fontsize=fontsize)
    pylab.setp(yticklabels, fontsize=fontsize)

    if title is not None:
        pylab.title(title, fontsize=fontsize)
    if showColorbar:
        pylab.colorbar(im)

    # colormap:
    pylab.hot()
    if fileName is not None:
        pylab.savefig(fileName)
    if show:
        pylab.show()

    
