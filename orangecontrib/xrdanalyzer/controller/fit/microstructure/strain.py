import numpy

from orangecontrib.xrdanalyzer.controller.fit.fit_parameter import Boundary, FitParameter, FitParametersList

class LaueGroup:

    laue_groups = {}
    laue_groups["-1"] = "1"
    laue_groups["2/m"] = "2"
    laue_groups["2/mmm"] = "3"
    laue_groups["4/m"] = "4"
    laue_groups["4/mmm"] = "5"
    laue_groups["-3R"] = "6"
    laue_groups["-31mR"] = "7"
    laue_groups["-3"] = "8"
    laue_groups["-3m1"] = "9"
    laue_groups["-31m"] = "10"
    laue_groups["6/m"] = "11"
    laue_groups["6/mmm"] = "12"
    laue_groups["m3"] = "13"
    laue_groups["m3m"] = "14"

    @classmethod
    def get_laue_id(cls, laue_group):
        return cls.laue_groups[laue_group]

    @classmethod
    def get_laue_group(cls, laue_id):
        for key, value in cls.laue_groups.items():
            if int(value) == laue_id:
                return key

    @classmethod
    def tuple(cls):
        return ["-1", "2/m", "2/mmm", "4/m", "4/mmm", "-3R", "-31mR", "-3", "-3m1", "-31m", "6/m", "6/mmm", "m3", "m3m"]

class InvariantPAH(FitParametersList):
    aa = None
    bb = None
    laue_id = 1
    e1 = None
    e2 = None
    e3 = None
    e4 = None
    e5 = None
    e6 = None
    e7 = None
    e8 = None
    e9 = None
    e10 = None
    e11 = None
    e12 = None
    e13 = None
    e14 = None
    e15 = None

    @classmethod
    def get_parameters_prefix(cls):
        return "invariant_"

    def __init__(self,
                 aa,
                 bb,
                 laue_id = 1,
                 e1  = None,
                 e2  = None,
                 e3  = None,
                 e4  = None,
                 e5  = None,
                 e6  = None,
                 e7  = None,
                 e8  = None,
                 e9  = None,
                 e10 = None,
                 e11 = None,
                 e12 = None,
                 e13 = None,
                 e14 = None,
                 e15 = None):
        super(InvariantPAH, self).__init__()

        self.aa = aa
        self.bb = bb
        self.laue_id = laue_id

        self.e1  = e1
        self.e2  = e2
        self.e3  = e3
        self.e4  = e4
        self.e5  = e5
        self.e6  = e6
        self.e7  = e7
        self.e8  = e8
        self.e9  = e9
        self.e10 = e10
        self.e11 = e11
        self.e12 = e12
        self.e13 = e13
        self.e14 = e14
        self.e15 = e15

    def get_invariant(self, h, k, l):
        invariant = self.e1.value*(h**4)

        if not self.e2  is None: invariant += self.e2.value*(k**4)
        if not self.e3  is None: invariant += self.e3.value*(l**4)
        if not self.e4  is None: invariant += 2*(self.e4.value*(h**2)*(k**2))
        if not self.e5  is None: invariant += 2*(self.e5.value*(k**2)*(l**2))
        if not self.e6  is None: invariant += 2*(self.e6.value*(h**2)*(l**2))
        if not self.e7  is None: invariant += 4*(self.e7.value*(h**3)*k)
        if not self.e8  is None: invariant += 4*(self.e8.value*(h**3)*l)
        if not self.e9  is None: invariant += 4*(self.e9.value*(k**3)*h)
        if not self.e10 is None: invariant += 4*(self.e10.value*(k**3)*l)
        if not self.e11 is None: invariant += 4*(self.e11.value*(l**3)*h)
        if not self.e12 is None: invariant += 4*(self.e12.value*(l**3)*k)
        if not self.e13 is None: invariant += 4*(self.e13.value*(h**2)*k*l)
        if not self.e14 is None: invariant += 4*(self.e14.value*(k**2)*h*l)
        if not self.e15 is None: invariant += 4*(self.e15.value*(l**2)*h*k)

        return invariant

    def to_text(self):
        text = "STRAIN - INVARIANT PAH\n"
        text += "-----------------------------------\n"

        text += self.aa.to_text() + "\n"
        text += self.bb.to_text() + "\n"

        text += "Laue Group: " + str(self.laue_id) + ", " + LaueGroup.get_laue_group(self.laue_id) + "\n"

        if not self.e1  is None: text += self.e1.to_text() + "\n"
        if not self.e2  is None: text += self.e2.to_text() + "\n"
        if not self.e3  is None: text += self.e3.to_text() + "\n"
        if not self.e4  is None: text += self.e4.to_text() + "\n"
        if not self.e5  is None: text += self.e5.to_text() + "\n"
        if not self.e6  is None: text += self.e6.to_text() + "\n"
        if not self.e7  is None: text += self.e7.to_text() + "\n"
        if not self.e8  is None: text += self.e8.to_text() + "\n"
        if not self.e9  is None: text += self.e9.to_text() + "\n"
        if not self.e10 is None: text += self.e10.to_text() + "\n"
        if not self.e11 is None: text += self.e11.to_text() + "\n"
        if not self.e12 is None: text += self.e12.to_text() + "\n"
        if not self.e13 is None: text += self.e13.to_text() + "\n"
        if not self.e14 is None: text += self.e14.to_text() + "\n"
        if not self.e15 is None: text += self.e15.to_text() + "\n"

        text += "-----------------------------------\n"

        return text

    def duplicate(self):
        return InvariantPAH(aa=None if self.aa is None else self.aa.duplicate(),
                            bb=None if self.bb is None else self.bb.duplicate(),
                            laue_id=self.laue_id,
                            e1 = None if self.e1  is None else self.e1.duplicate(),
                            e2 = None if self.e2  is None else self.e2.duplicate(),
                            e3 = None if self.e3  is None else self.e3.duplicate(),
                            e4 = None if self.e4  is None else self.e4.duplicate(),
                            e5 = None if self.e5  is None else self.e5.duplicate(),
                            e6 = None if self.e6  is None else self.e6.duplicate(),
                            e7 = None if self.e7  is None else self.e7.duplicate(),
                            e8 = None if self.e8  is None else self.e8.duplicate(),
                            e9 = None if self.e9  is None else self.e9.duplicate(),
                            e10= None if self.e10 is None else self.e10.duplicate(),
                            e11= None if self.e11 is None else self.e11.duplicate(),
                            e12= None if self.e12 is None else self.e12.duplicate(),
                            e13= None if self.e13 is None else self.e13.duplicate(),
                            e14= None if self.e14 is None else self.e14.duplicate(),
                            e15= None if self.e15 is None else self.e15.duplicate())



    def get_warren_plot(self, h, k, l, L_max=50):
        step = L_max/100
        L = numpy.arange(start=step, stop=L_max + step, step=step)

        from orangecontrib.xrdanalyzer.controller.fit.wppm_functions import displacement_invariant_pah

        DL = displacement_invariant_pah(L, h, k, l, self.aa.value, self.bb.value, self.get_invariant(h, k, l))

        return L, DL

class InvariantPAHLaueGroup1(InvariantPAH):

    def __init__(self,
                 aa  =FitParameter(parameter_name="aa", value=1e-3),
                 bb  =FitParameter(parameter_name="bb", value=1e-3),
                 e1  = FitParameter(parameter_name="e1" , value=1e-4),
                 e2  = FitParameter(parameter_name="e2" , value=1e-4),
                 e3  = FitParameter(parameter_name="e3" , value=1e-4),
                 e4  = FitParameter(parameter_name="e4" , value=1e-4),
                 e5  = FitParameter(parameter_name="e5" , value=1e-4),
                 e6  = FitParameter(parameter_name="e6" , value=1e-4),
                 e7  = FitParameter(parameter_name="e7" , value=1e-4),
                 e8  = FitParameter(parameter_name="e8" , value=1e-4),
                 e9  = FitParameter(parameter_name="e9" , value=1e-4),
                 e10 = FitParameter(parameter_name="e10", value=1e-4),
                 e11 = FitParameter(parameter_name="e11", value=1e-4),
                 e12 = FitParameter(parameter_name="e12", value=1e-4),
                 e13 = FitParameter(parameter_name="e13", value=1e-4),
                 e14 = FitParameter(parameter_name="e14", value=1e-4),
                 e15 = FitParameter(parameter_name="e15", value=1e-4)):
        super().__init__(aa, bb, 1, e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15)
        raise NotImplementedError("TO BE CHECKED")

class InvariantPAHLaueGroup2(InvariantPAH):

    def __init__(self,
                 aa=FitParameter(parameter_name="aa", value=1e-3),
                 bb=FitParameter(parameter_name="bb", value=1e-3),
                 e1  = FitParameter(parameter_name="e1" , value=1e-4),
                 e2  = FitParameter(parameter_name="e2" , value=1e-4),
                 e3  = FitParameter(parameter_name="e3" , value=1e-4),
                 e4  = FitParameter(parameter_name="e4" , value=1e-4),
                 e5  = FitParameter(parameter_name="e5" , value=1e-4),
                 e6  = FitParameter(parameter_name="e6" , value=1e-4),
                 e7  = FitParameter(parameter_name="e7" , value=1e-4),
                 e9  = FitParameter(parameter_name="e9" , value=1e-4),
                 e15 = FitParameter(parameter_name="e15", value=1e-4)):
        super().__init__(aa, bb, 2, e1, e2, e3, e4, e5, e6, e7, e9=e9, e15=e15)
        raise NotImplementedError("TO BE CHECKED")

class InvariantPAHLaueGroup3(InvariantPAH):

    def __init__(self,
                 aa=FitParameter(parameter_name="aa", value=1e-3),
                 bb=FitParameter(parameter_name="bb", value=1e-3),
                 e1  = FitParameter(parameter_name="e1" , value=1e-4),
                 e2  = FitParameter(parameter_name="e2" , value=1e-4),
                 e3  = FitParameter(parameter_name="e3" , value=1e-4),
                 e4  = FitParameter(parameter_name="e4" , value=1e-4),
                 e5  = FitParameter(parameter_name="e5" , value=1e-4),
                 e6  = FitParameter(parameter_name="e6" , value=1e-4),
                 e7  = FitParameter(parameter_name="e7" , value=1e-4)):
        super().__init__(aa, bb, 3, e1, e2, e3, e4, e5, e6, e7)
        raise NotImplementedError("TO BE CHECKED")

class InvariantPAHLaueGroup4(InvariantPAH):

    def __init__(self,
                 aa=FitParameter(parameter_name="aa", value=1e-3),
                 bb=FitParameter(parameter_name="bb", value=1e-3),
                 e1  = FitParameter(parameter_name="e1" , value=1e-4),
                 e3  = FitParameter(parameter_name="e3" , value=1e-4),
                 e4  = FitParameter(parameter_name="e4" , value=1e-4),
                 e6  = FitParameter(parameter_name="e6" , value=1e-4),
                 e7  = FitParameter(parameter_name="e7" , value=1e-4)):
        super().__init__(aa, bb, 4, e1, e3=e3, e4=e4, e6=e6, e7=e7)
        raise NotImplementedError("TO BE CHECKED")

class InvariantPAHLaueGroup5(InvariantPAH):

    def __init__(self,
                 aa=FitParameter(parameter_name="aa", value=1e-3),
                 bb=FitParameter(parameter_name="bb", value=1e-3),
                 e1  = FitParameter(parameter_name="e1" , value=1e-4),
                 e3  = FitParameter(parameter_name="e3" , value=1e-4),
                 e4  = FitParameter(parameter_name="e4" , value=1e-4),
                 e6  = FitParameter(parameter_name="e6" , value=1e-4)):
        super().__init__(aa, bb, 5, e1, e3=e3, e4=e4, e6=e6)
        raise NotImplementedError("TO BE CHECKED")


class InvariantPAHLaueGroup6(InvariantPAH):

    def __init__(self,
                 aa=FitParameter(parameter_name="aa", value=1e-3),
                 bb=FitParameter(parameter_name="bb", value=1e-3),
                 e1  = FitParameter(parameter_name="e1" , value=1e-4),
                 e3  = FitParameter(parameter_name="e3" , value=1e-4),
                 e4  = FitParameter(parameter_name="e4" , value=1e-4),
                 e6  = FitParameter(parameter_name="e6" , value=1e-4),
                 e7  = FitParameter(parameter_name="e7" , value=1e-4),
                 e9  = FitParameter(parameter_name="e9" , value=1e-4),
                 e15 = FitParameter(parameter_name="e15", value=1e-4)):
        super().__init__(aa, bb, 6, e1, e3=e3, e4=e4, e6=e6, e7=e7, e9=e9, e15=e15)
        raise NotImplementedError("TO BE CHECKED")

class InvariantPAHLaueGroup7(InvariantPAH):
    def __init__(self,
                 aa=FitParameter(parameter_name="aa", value=1e-3),
                 bb=FitParameter(parameter_name="bb", value=1e-3),
                 e1  = FitParameter(parameter_name="e1" , value=1e-4),
                 e3  = FitParameter(parameter_name="e3" , value=1e-4),
                 e4  = FitParameter(parameter_name="e4" , value=1e-4),
                 e6  = FitParameter(parameter_name="e6" , value=1e-4),
                 e7  = FitParameter(parameter_name="e7" , value=1e-4),
                 e9  = FitParameter(parameter_name="e9" , value=1e-4),
                 e15 = FitParameter(parameter_name="e15", value=1e-4)):
        super().__init__(aa, bb, 7, e1, e3=e3, e4=e4, e6=e6, e7=e7, e9=e9, e15=e15)
        raise NotImplementedError("TO BE CHECKED")

class InvariantPAHLaueGroup8(InvariantPAH):
    def __init__(self,
                 aa=FitParameter(parameter_name="aa", value=1e-3),
                 bb=FitParameter(parameter_name="bb", value=1e-3),
                 e1  = FitParameter(parameter_name="e1" , value=1e-4),
                 e3  = FitParameter(parameter_name="e3" , value=1e-4),
                 e4  = FitParameter(parameter_name="e4" , value=1e-4),
                 e6  = FitParameter(parameter_name="e6" , value=1e-4),
                 e7  = FitParameter(parameter_name="e7" , value=1e-4),
                 e9  = FitParameter(parameter_name="e9" , value=1e-4),
                 e15 = FitParameter(parameter_name="e15", value=1e-4)):
        super().__init__(aa, bb, 8, e1, e3=e3, e4=e4, e6=e6, e7=e7, e9=e9, e15=e15)
        raise NotImplementedError("TO BE CHECKED")

class InvariantPAHLaueGroup9(InvariantPAH):
    def __init__(self,
                 aa=FitParameter(parameter_name="aa", value=1e-3),
                 bb=FitParameter(parameter_name="bb", value=1e-3),
                 e1  = FitParameter(parameter_name="e1" , value=1e-4),
                 e3  = FitParameter(parameter_name="e3" , value=1e-4),
                 e6  = FitParameter(parameter_name="e6" , value=1e-4),
                 e13 = FitParameter(parameter_name="e13", value=1e-4)):
        super().__init__(aa, bb, 9, e1, e3=e3, e6=e6, e13=e13)
        raise NotImplementedError("TO BE CHECKED")

class InvariantPAHLaueGroup10(InvariantPAH):
    def __init__(self,
                 aa=FitParameter(parameter_name="aa", value=1e-3),
                 bb=FitParameter(parameter_name="bb", value=1e-3),
                 e1  = FitParameter(parameter_name="e1" , value=1e-4),
                 e3  = FitParameter(parameter_name="e3" , value=1e-4),
                 e6  = FitParameter(parameter_name="e6" , value=1e-4),
                 e13 = FitParameter(parameter_name="e13", value=1e-4)):
        super().__init__(aa, bb, 10, e1, e3=e3, e6=e6, e13=e13)
        raise NotImplementedError("TO BE CHECKED")

class InvariantPAHLaueGroup11(InvariantPAH):
    def __init__(self,
                 aa=FitParameter(parameter_name="aa", value=1e-3),
                 bb=FitParameter(parameter_name="bb", value=1e-3),
                 e1  = FitParameter(parameter_name="e1" , value=1e-4),
                 e3  = FitParameter(parameter_name="e3" , value=1e-4),
                 e6  = FitParameter(parameter_name="e6" , value=1e-4)):
        super().__init__(aa, bb, 11, e1, e3=e3, e6=e6)
        raise NotImplementedError("TO BE CHECKED")


class InvariantPAHLaueGroup12(InvariantPAH):
    def __init__(self,
                 aa=FitParameter(parameter_name="aa", value=1e-3),
                 bb=FitParameter(parameter_name="bb", value=1e-3),
                 e1  = FitParameter(parameter_name="e1" , value=1e-4),
                 e3  = FitParameter(parameter_name="e3" , value=1e-4),
                 e6  = FitParameter(parameter_name="e6" , value=1e-4)):
        super().__init__(aa, bb, 12, e1, e3=e3, e6=e6)


class InvariantPAHCubic(InvariantPAH):
    def __init__(self,
                 aa=FitParameter(parameter_name="aa", value=1e-3),
                 bb=FitParameter(parameter_name="bb", value=1e-3),
                 laue_id = 13,
                 e1 = FitParameter(parameter_name="e1" , value=1e-4),
                 e4 = FitParameter(parameter_name="e4" , value=1e-4)):
        super(InvariantPAHCubic, self).__init__(aa, bb, laue_id,
                                                e1=e1,
                                                e2=FitParameter(parameter_name=self.get_parameters_prefix() + "e2",
                                                                value=e1.value,
                                                                function=True,
                                                                function_value=e1.parameter_name),
                                                e3=FitParameter(parameter_name=self.get_parameters_prefix() + "e3",
                                                                value=e1.value,
                                                                function=True,
                                                                function_value=e1.parameter_name),
                                                e4=e4,
                                                e5=FitParameter(parameter_name=self.get_parameters_prefix() + "e5",
                                                                value=e4.value,
                                                                function=True,
                                                                function_value=e4.parameter_name),
                                                e6=FitParameter(parameter_name=self.get_parameters_prefix() + "e6",
                                                                value=e4.value,
                                                                function=True,
                                                                function_value=e4.parameter_name))

class InvariantPAHLaueGroup13(InvariantPAHCubic):
    def __init__(self,
                 aa=FitParameter(parameter_name="aa", value=1e-3),
                 bb=FitParameter(parameter_name="bb", value=1e-3),
                 e1  = FitParameter(parameter_name="e1" , value=1e-4),
                 e4  = FitParameter(parameter_name="e4" , value=1e-4)):
        super(InvariantPAHLaueGroup13, self).__init__(aa, bb, 13, e1, e4)

class InvariantPAHLaueGroup14(InvariantPAHCubic):
    def __init__(self,
                 aa=FitParameter(parameter_name="aa", value=1e-3),
                 bb=FitParameter(parameter_name="bb", value=1e-3),
                 e1  = FitParameter(parameter_name="e1" , value=1e-4),
                 e4  = FitParameter(parameter_name="e4" , value=1e-4)):
        super(InvariantPAHLaueGroup14, self).__init__(aa, bb, 14, e1, e4)

class KrivoglazWilkensModel(FitParametersList):
    rho = None
    Re  = None
    Ae  = None
    Be  = None
    As  = None
    Bs  = None
    mix = None
    b   = None

    @classmethod
    def get_parameters_prefix(cls):
        return "kw_"

    def __init__(self,
                 rho= None,
                 Re = None,
                 Ae = None,
                 Be = None,
                 As = None,
                 Bs = None,
                 mix= None,
                 b  = None,
                 ):
        super(FitParametersList, self).__init__()

        self.rho = rho
        self.Re  = Re
        self.Ae  = Ae
        self.Be  = Be
        self.As  = As
        self.Bs  = Bs
        self.mix = mix
        self.b   = b

    def to_text(self):
        text = "STRAIN - KRIVOGLAZ-WILKENS MODEL\n"
        text += "-----------------------------------\n"

        text += "" if self.rho is None else self.rho.to_text() + "\n"
        text += "" if self.Re  is None else self.Re .to_text() + "\n"
        text += "" if self.Ae  is None else self.Ae .to_text() + "\n"
        text += "" if self.Be  is None else self.Be .to_text() + "\n"
        text += "" if self.As  is None else self.As .to_text() + "\n"
        text += "" if self.Bs  is None else self.Bs .to_text() + "\n"
        text += "" if self.mix is None else self.mix.to_text() + "\n"
        text += "" if self.b   is None else self.b  .to_text() + "\n"

        text += "-----------------------------------\n"

        return text


    def duplicate(self):
        return KrivoglazWilkensModel(rho = None if self.rho is None else self.rho.duplicate(),
                                     Re  = None if self.Re  is None else self.Re.duplicate(),
                                     Ae  = None if self.Ae  is None else self.Ae.duplicate(),
                                     Be  = None if self.Be  is None else self.Be.duplicate(),
                                     As  = None if self.As  is None else self.As.duplicate(),
                                     Bs  = None if self.Bs  is None else self.Bs.duplicate(),
                                     mix = None if self.mix is None else self.mix.duplicate(),
                                     b   = None if self.b   is None else self.b.duplicate())


    def get_warren_plot(self, h, k, l, L_max=50):
        step = L_max/100
        L = numpy.arange(start=step, stop=L_max + step, step=step)

        from orangecontrib.xrdanalyzer.controller.fit.wppm_functions import displacement_krivoglaz_wilkens

        DL = displacement_krivoglaz_wilkens(L, h, k, l,
                                            self.rho.value,
                                            self.Re.value,
                                            self.Ae.value,
                                            self.Be.value,
                                            self.As.value,
                                            self.Bs.value,
                                            self.mix.value,
                                            self.b.value)
        return L, DL


class WarrenModel(FitParametersList):
    average_cell_parameter = None

    @classmethod
    def get_parameters_prefix(cls):
        return "warren_"

    def __init__(self,
                 average_cell_parameter=None):
        super(FitParametersList, self).__init__()

        self.average_cell_parameter = average_cell_parameter


    def to_text(self):
        text = "STRAIN - WARREN MODEL\n"
        text += "-----------------------------------\n"

        text += self.average_cell_parameter.to_text() + "\n"

        text += "-----------------------------------\n"

        return text

    def duplicate(self):
        return WarrenModel(average_cell_parameter=None if self.average_cell_parameter is None else self.average_cell_parameter.duplicate())


