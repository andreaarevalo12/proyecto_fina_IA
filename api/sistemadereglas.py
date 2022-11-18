from reglas import *

class sistemadereglas(KnowledgeEngine):
    
    diagnostico = ''
        
    @Rule(AND(reglas(abdominal="no"))
    ,(reglas(fiebre="no"))
    ,(reglas(deposiciones=P(lambda dep: dep>=0)& P(lambda dep: dep<=2)))
    ,(reglas(vomito="no"))
    ,(reglas(apetito="no")))
    def m1(self):  
        self.diagnostico="Usted no presenta sintomas de una enfermedad del sistema digestivo"       
        print("Usted no presenta sintomas de una enfermedad del sistema digestivo")

#@Rule(Fact(x=P(lambda x: x >= 0) & P(lambda x: x <= 2))) 
    

    @Rule(AND(reglas(abdominal="no"))
    ,(reglas(fiebre="no"))
    ,(reglas(deposiciones=P(lambda dep: dep>=0)& P(lambda dep: dep<=2)))
    ,(reglas(vomito="no"))
    ,(reglas(apetito="si"))) 
    def m2(self):
        self.diagnostico="Usted no presenta sintomas de una enfermedad del sistema digestivo. Se recomienda valoracion por nutricion"
        print("Usted no presenta sintomas de una enfermedad del sistema digestivo. Se recomienda valoracion por nutricion")
        
        
    @Rule(AND(reglas(abdominal="no"))
    ,(reglas(fiebre="no"))
    ,(reglas(deposiciones=P(lambda dep: dep>=0)& P(lambda dep: dep<=2)))
    ,(reglas(vomito="si"))
    ,(reglas(apetito="no"))) 
    def m3(self):
        self.diagnostico="Los sintomas no son concluyentes, se necesita mas informacion para realizar un diagnostico certero. "
        print("Los sintomas no son concluyentes, se necesita mas informacion para realizar un diagnostico certero. ")
        
    @Rule(AND(reglas(abdominal="no"))
    ,(reglas(fiebre="no"))
    ,(reglas(deposiciones=P(lambda dep: dep>=0)& P(lambda dep: dep<=2)))
    ,(reglas(vomito="si"))
    ,(reglas(apetito="si"))) 
    def m4(self):
        self.diagnostico="Los sintomas no son concluyentes, se necesita mas informacion para realizar un diagnostico certero. "
        print("Los sintomas no son concluyentes, se necesita mas informacion para realizar un diagnostico certero. ")


    @Rule(AND(reglas(abdominal="no"))
    ,(reglas(fiebre="no"))
    ,(reglas(deposiciones=P(lambda dep: dep>=3)& P(lambda dep: dep<=8)))
    ,(reglas(vomito="no"))
    ,(reglas(apetito="no"))) 
    def m5(self):
        self.diagnostico="Los sintomas no son concluyentes, se necesita mas informacion para realizar un diagnostico certero. Se recomienda hidratarse bien"
        print("Los sintomas no son concluyentes, se necesita mas informacion para realizar un diagnostico certero. Se recomienda hidratarse bien")
        
        
    @Rule(AND(reglas(abdominal="no"))
    ,(reglas(fiebre="no"))
    ,(reglas(deposiciones=P(lambda dep: dep>=3)& P(lambda dep: dep<=8)))
    ,(reglas(vomito="no"))
    ,(reglas(apetito="si"))) 
    def m6(self):
        self.diagnostico="Los sintomas no son concluyentes, se necesita mas informacion para realizar un diagnostico certero. Se recomienda hidratarse bien"
        print("Los sintomas no son concluyentes, se necesita mas informacion para realizar un diagnostico certero. Se recomienda hidratarse bien")
            
           
    @Rule(AND(reglas(abdominal="no"))
    ,(reglas(fiebre="no"))
    ,(reglas(deposiciones=P(lambda dep: dep>=3)& P(lambda dep: dep<=8)))
    ,(reglas(vomito="si"))
    ,(reglas(apetito="no"))) 
    def m7(self):
        self.diagnostico="Usted tiene ENFERMEDAD DIARREICA AGUDA, favor hidratarse bien"
        print("Usted tiene ENFERMEDAD DIARREICA AGUDA, favor hidratarse bien")


    @Rule(AND(reglas(abdominal="no"))
    ,(reglas(fiebre="no"))
    ,(reglas(deposiciones=P(lambda dep: dep>=3)& P(lambda dep: dep<=8)))
    ,(reglas(vomito="si"))
    ,(reglas(apetito="si")))
    def m8(self):
        self.diagnostico="Usted tiene ENFERMEDAD DIARREICA AGUDA, favor hidratarse bien"
        print("Usted tiene ENFERMEDAD DIARREICA AGUDA, favor hidratarse bien")
        
        
    @Rule(AND(reglas(abdominal="no"))
    ,(reglas(fiebre="si"))
    ,(reglas(deposiciones=P(lambda dep: dep>=0)& P(lambda dep: dep<=2)))
    ,(reglas(vomito="no"))
    ,(reglas(apetito="no"))) 
    def m9(self):
        self.diagnostico="Los sintomas no son concluyentes, se necesita mas informacion para realizar un diagnostico certero. Se recomienda valoracion medica"
        print("Los sintomas no son concluyentes, se necesita mas informacion para realizar un diagnostico certero. Se recomienda valoracion medica")
        
        
    @Rule(AND(reglas(abdominal="no"))
    ,(reglas(fiebre="si"))
    ,(reglas(deposiciones=P(lambda dep: dep>=0)& P(lambda dep: dep<=2)))
    ,(reglas(vomito="no"))
    ,(reglas(apetito="si"))) 
    def m10(self):
        self.diagnostico="Los sintomas no son concluyentes, se necesita mas informacion para realizar un diagnostico certero. Se recomienda valoracion medica"
        print("Los sintomas no son concluyentes, se necesita mas informacion para realizar un diagnostico certero. Se recomienda valoracion medica")


    @Rule(AND(reglas(abdominal="no"))
    ,(reglas(fiebre="si"))
    ,(reglas(deposiciones=P(lambda dep: dep>=0)& P(lambda dep: dep<=2)))
    ,(reglas(vomito="si"))
    ,(reglas(apetito="no")))  
    def m11(self):
        self.diagnostico="Los sintomas no son concluyentes, se necesita mas informacion para realizar un diagnostico certero. Se recomienda valoracion medica"
        print("Los sintomas no son concluyentes, se necesita mas informacion para realizar un diagnostico certero. Se recomienda valoracion medica")
        
        
    @Rule(AND(reglas(abdominal="no"))
    ,(reglas(fiebre="si"))
    ,(reglas(deposiciones=P(lambda dep: dep>=0)& P(lambda dep: dep<=2)))
    ,(reglas(vomito="si"))
    ,(reglas(apetito="si")))
    def m12(self):
        self.diagnostico="Los sintomas presentados son asociados a PANCREATITIS, se recomienda valoracion medica"
        print("Los sintomas presentados son asociados a PANCREATITIS, se recomienda valoracion medica")
                              
                              
    @Rule(AND(reglas(abdominal="no"))
    ,(reglas(fiebre="si"))
    ,(reglas(deposiciones=P(lambda dep: dep>=3)& P(lambda dep: dep<=8)))
    ,(reglas(vomito="no"))
    ,(reglas(apetito="no")))
    def m13(self):
        self.diagnostico="Usted tiene ENFERMEDAD DIARREICA AGUDA, favor hidratarse bien"
        print("Usted tiene ENFERMEDAD DIARREICA AGUDA, favor hidratarse bien")


    @Rule(AND(reglas(abdominal="no"))
    ,(reglas(fiebre="si"))
    ,(reglas(deposiciones=P(lambda dep: dep>=3)& P(lambda dep: dep<=8)))
    ,(reglas(vomito="no"))
    ,(reglas(apetito="si")))
    def m14(self):
        self.diagnostico="Usted tiene ENFERMEDAD DIARREICA AGUDA, favor hidratarse bien"
        print("Usted tiene ENFERMEDAD DIARREICA AGUDA, favor hidratarse bien")
        
        
    @Rule(AND(reglas(abdominal="no"))
    ,(reglas(fiebre="si"))
    ,(reglas(deposiciones=P(lambda dep: dep>=3)& P(lambda dep: dep<=8)))
    ,(reglas(vomito="si"))
    ,(reglas(apetito="no"))) 
    def m15(self):
        self.diagnostico="Usted tiene ENFERMEDAD DIARREICA AGUDA, favor hidratarse bien"
        print("Usted tiene ENFERMEDAD DIARREICA AGUDA, favor hidratarse bien")
        
        
    @Rule(AND(reglas(abdominal="no"))
    ,(reglas(fiebre="si"))
    ,(reglas(deposiciones=P(lambda dep: dep>=3)& P(lambda dep: dep<=8)))
    ,(reglas(vomito="si"))
    ,(reglas(apetito="si")))
    def m16(self):
        self.diagnostico="Usted tiene ENFERMEDAD DIARREICA AGUDA, favor hidratarse bien"
        print("Usted tiene ENFERMEDAD DIARREICA AGUDA, favor hidratarse bien")


    @Rule(AND(reglas(abdominal="si"))
    ,(reglas(fiebre="no"))
    ,(reglas(deposiciones=P(lambda dep: dep>=0)& P(lambda dep: dep<=2)))
    ,(reglas(vomito="no"))
    ,(reglas(apetito="no"))) 
    def m17(self):
        self.diagnostico="Los sintomas no son concluyentes, se necesita mas informacion para realizar un diagnostico certero."
        print("Los sintomas no son concluyentes, se necesita mas informacion para realizar un diagnostico certero.")
        
        
    @Rule(AND(reglas(abdominal="si"))
    ,(reglas(fiebre="no"))
    ,(reglas(deposiciones=P(lambda dep: dep>=0)& P(lambda dep: dep<=2)))
    ,(reglas(vomito="no"))
    ,(reglas(apetito="si"))) 
    def m18(self):
        self.diagnostico="Los sintomas no son concluyentes, se necesita mas informacion para realizar un diagnostico certero."
        print("Los sintomas no son concluyentes, se necesita mas informacion para realizar un diagnostico certero.")
            
           
    @Rule(AND(reglas(abdominal="si"))
    ,(reglas(fiebre="no"))
    ,(reglas(deposiciones=P(lambda dep: dep>=0)& P(lambda dep: dep<=2)))
    ,(reglas(vomito="si"))
    ,(reglas(apetito="no")))
    def m19(self):
        self.diagnostico="Los sintomas presentados son asociados a GASTRITIS, se recomienda valoracion medica"
        print("Los sintomas presentados son asociados a GASTRITIS, se recomienda valoracion medica")


    @Rule(AND(reglas(abdominal="si"))
    ,(reglas(fiebre="no"))
    ,(reglas(deposiciones=P(lambda dep: dep>=0)& P(lambda dep: dep<=2)))
    ,(reglas(vomito="si"))
    ,(reglas(apetito="si")))
    def m20(self):
        self.diagnostico="Los sintomas presentados son asociados a ENFERMEDAD DE CROHN, se recomienda valoracion medica"
        print("Los sintomas presentados son asociados a ENFERMEDAD DE CROHN, se recomienda valoracion medica")
        
        
    @Rule(AND(reglas(abdominal="si"))
    ,(reglas(fiebre="no"))
    ,(reglas(deposiciones=P(lambda dep: dep>=3)& P(lambda dep: dep<=8)))
    ,(reglas(vomito="no"))
    ,(reglas(apetito="no")))
    def m21(self):
        self.diagnostico="Los sintomas presentados son asociados a SINDROME DE INTESTINO IRRITABLE, se recomienda valoracion medica"
        print("Los sintomas presentados son asociados a SINDROME DE INTESTINO IRRITABLE, se recomienda valoracion medica")
        
    @Rule(AND(reglas(abdominal="si"))
    ,(reglas(fiebre="no"))
    ,(reglas(deposiciones=P(lambda dep: dep>=3)& P(lambda dep: dep<=8)))
    ,(reglas(vomito="no"))
    ,(reglas(apetito="si")))
    def m22(self):
        self.diagnostico="Los sintomas presentados son asociados a ENFERMEDAD DE CROHN, se recomienda valoracion medica"
        print("Los sintomas presentados son asociados a ENFERMEDAD DE CROHN, se recomienda valoracion medica")


    @Rule(AND(reglas(abdominal="si"))
    ,(reglas(fiebre="no"))
    ,(reglas(deposiciones=P(lambda dep: dep>=3)& P(lambda dep: dep<=8)))
    ,(reglas(vomito="si"))
    ,(reglas(apetito="no")))
    def m23(self):
        self.diagnostico="Los sintomas presentados son asociados a ENFERMEDAD CELIACA, se recomienda valoracion medica"
        print("Los sintomas presentados son asociados a ENFERMEDAD CELIACA, se recomienda valoracion medica")
        
        
    @Rule(AND(reglas(abdominal="si"))
    ,(reglas(fiebre="no"))
    ,(reglas(deposiciones=P(lambda dep: dep>=3)& P(lambda dep: dep<=8)))
    ,(reglas(vomito="si"))
    ,(reglas(apetito="si")))
    def m24(self):
        self.diagnostico="Los sintomas presentados son asociados a ENFERMEDAD DE CROHN, se recomienda valoracion medica"
        print("Los sintomas presentados son asociados a ENFERMEDAD DE CROHN, se recomienda valoracion medica")
                              
                              
    @Rule(AND(reglas(abdominal="si"))
    ,(reglas(fiebre="si"))
    ,(reglas(deposiciones=P(lambda dep: dep>=0)& P(lambda dep: dep<=2)))
    ,(reglas(vomito="no"))
    ,(reglas(apetito="no")))  
    def m25(self):
        self.diagnostico="Los sintomas no son concluyentes, se necesita mas informacion para realizar un diagnostico certero. Se recomienda valoracion medica"
        print("Los sintomas no son concluyentes, se necesita mas informacion para realizar un diagnostico certero. Se recomienda valoracion medica" )


    @Rule(AND(reglas(abdominal="si"))
    ,(reglas(fiebre="si"))
    ,(reglas(deposiciones=P(lambda dep: dep>=0)& P(lambda dep: dep<=2)))
    ,(reglas(vomito="no"))
    ,(reglas(apetito="si"))) 
    def m26(self):
        self.diagnostico="Los sintomas no son concluyentes, se necesita mas informacion para realizar un diagnostico certero. Se recomienda valoracion medica"
        print("Los sintomas no son concluyentes, se necesita mas informacion para realizar un diagnostico certero. Se recomienda valoracion medica")
        
        
    @Rule(AND(reglas(abdominal="si"))
    ,(reglas(fiebre="si"))
    ,(reglas(deposiciones=P(lambda dep: dep>=0)& P(lambda dep: dep<=2)))
    ,(reglas(vomito="si"))
    ,(reglas(apetito="no")))
    def m27(self):
        self.diagnostico="Los sintomas presentados son asociados a COLECISTITIS (Calculos Biliares), se recomienda valoracion medica"
        print("Los sintomas presentados son asociados a COLECISTITIS (Calculos Biliares), se recomienda valoracion medica")
        
    @Rule(AND(reglas(abdominal="si"))
    ,(reglas(fiebre="si"))
    ,(reglas(deposiciones=P(lambda dep: dep>=0)& P(lambda dep: dep<=2)))
    ,(reglas(vomito="si"))
    ,(reglas(apetito="si")))
    def m28(self):
        self.diagnostico="Los sintomas presentados son asociados a PANCREATITIS, se recomienda valoracion medica"
        print("Los sintomas presentados son asociados a PANCREATITIS, se recomienda valoracion medica")


    @Rule(AND(reglas(abdominal="si"))
    ,(reglas(fiebre="si"))
    ,(reglas(deposiciones=P(lambda dep: dep>=3)& P(lambda dep: dep<=8)))
    ,(reglas(vomito="no"))
    ,(reglas(apetito="no")))  
    def m29(self):
        self.diagnostico="Los sintomas presentados son asociados a GASTROENTERITIS, se recomienda valoracion medica"
        print("Los sintomas presentados son asociados a GASTROENTERITIS, se recomienda valoracion medica")
        
        
    @Rule(AND(reglas(abdominal="si"))
    ,(reglas(fiebre="si"))
    ,(reglas(deposiciones=P(lambda dep: dep>=3)& P(lambda dep: dep<=8)))
    ,(reglas(vomito="no"))
    ,(reglas(apetito="si")))
    def m30(self):
        self.diagnostico="Los sintomas presentados son asociados a APENDICITIS, se recomienda valoracion medica"
        print("Los sintomas presentados son asociados a APENDICITIS, se recomienda valoracion medica")
            
           
    @Rule(AND(reglas(abdominal="si"))
    ,(reglas(fiebre="si"))
    ,(reglas(deposiciones=P(lambda dep: dep>=3)& P(lambda dep: dep<=8)))
    ,(reglas(vomito="si"))
    ,(reglas(apetito="no")))
    def m31(self):
        self.diagnostico="Los sintomas presentados son asociados a GASTROENTERITIS, se recomienda valoracion medica"
        print("Los sintomas presentados son asociados a GASTROENTERITIS, se recomienda valoracion medica")


    @Rule(AND(reglas(abdominal="si"))
    ,(reglas(fiebre="si"))
    ,(reglas(deposiciones=P(lambda dep: dep>=3)& P(lambda dep: dep<=8)))
    ,(reglas(vomito="si"))
    ,(reglas(apetito="si")))
    def m32(self):
        self.diagnostico ="Los sintomas presentados son asociados a APENDICITIS, se recomienda valoracion medica urgente" 
        print("Los sintomas presentados son asociados a APENDICITIS, se recomienda valoracion medica urgente")
        
        
                               