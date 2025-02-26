import numpy

from orangecontrib.xrdanalyzer.controller.fit.fit_parameter import Boundary, FitParameter, FitParametersList

class Shape:
    NONE = "none"
    SPHERE = "sphere"
    CUBE = "cube"
    TETRAHEDRON = "tetrahedron"
    OCTAHEDRON = "octahedron"
    CYLINDER = "cylinder"

    @classmethod
    def tuple(cls):
        return [cls.NONE, cls.SPHERE, cls.CUBE, cls.TETRAHEDRON, cls.OCTAHEDRON, cls.CYLINDER]


class Distribution:
    DELTA = "delta"
    LOGNORMAL = "lognormal"
    GAMMA = "gamma"
    YORK = "york"

    @classmethod
    def tuple(cls):
        return [cls.DELTA, cls.LOGNORMAL, cls.GAMMA, cls.YORK]

class Normalization:
    NORMALIZE_TO_N = 0
    NORMALIZE_TO_N2 = 1

    @classmethod
    def tuple(cls):
        return ["to N", "to N\u00b2"]

from orangecontrib.xrdanalyzer.controller.fit.wppm_functions import lognormal_distribution

class SizeParameters(FitParametersList):

    shape = Shape.SPHERE
    distribution = Distribution.LOGNORMAL
    mu = None
    sigma = None
    add_saxs = False
    normalize_to = Normalization.NORMALIZE_TO_N

    @classmethod
    def get_parameters_prefix(cls):
        return "size_"

    def __init__(self, shape, distribution, mu, sigma, add_saxs=False, normalize_to=Normalization.NORMALIZE_TO_N):
        super(SizeParameters, self).__init__()

        self.shape = shape
        self.distribution = distribution
        self.mu = mu
        self.sigma = sigma
        self.add_saxs = add_saxs
        self.normalize_to = normalize_to

    def to_text(self):
        text = "SIZE\n"
        text += "-----------------------------------\n"

        text += "Shape: " + self.shape + "\n"
        text += "Distribution: " + self.distribution + "\n"

        text += self.mu.to_text() + "\n"
        if not self.sigma is None: text += self.sigma.to_text() + "\n"

        if self.distribution == Distribution.DELTA:
            text += "Add SAXS: " + str(self.add_saxs) + "\n"
            text += "Normalize to: " + Normalization.tuple()[self.normalize_to] + "\n"

        text += "-----------------------------------\n"

        return text


    def duplicate(self):
        return SizeParameters(shape=self.shape,
                              distribution=self.distribution,
                              mu=None if self.mu is None else self.mu.duplicate(),
                              sigma=None if self.sigma is None else self.sigma.duplicate(),
                              add_saxs=self.add_saxs,
                              normalize_to=self.normalize_to)


    def get_distribution(self, auto=True, D_min=None, D_max=None):
        if auto:
            D_min = 0
            D_max = 1000

        step = (D_max-D_min)/1000

        x = numpy.arange(start=D_min, stop=D_max, step=step)

        try:
            if self.distribution == Distribution.LOGNORMAL:
                y = lognormal_distribution(self.mu.value, self.sigma.value, x)
            else:
                y = numpy.zeros(len(x))

            if auto:
                D_min = 0.0
                D_max = x[numpy.where(y > 1e-5)][-1]
                if D_min == D_max: D_min==x[0]

                x, y, D_min, D_max = self.get_distribution(auto=False, D_min=D_min, D_max=D_max)
        except:
            pass

        return x, y, D_min, D_max


if __name__=="__main__":
    fpl = SizeParameters(shape=Shape.SPHERE,
                         distribution=Distribution.DELTA,
                         mu=FitParameter(value=10, parameter_name="mu"),
                         sigma=None, add_saxs=True)

    print(fpl.get_parameters())
