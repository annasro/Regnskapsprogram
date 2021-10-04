from lib.str2bool import str2bool

def GetInput(text, type_ = None, min_=None, max_= None, range_= None):
    if min_ is not None and max_ is not None and max_ < min_:
        raise ValueError('min_ must be less or equal to max_.')
    while True:
        Value = input(text)
        if type_ is not None:
            try:
                Value = type_(Value)
            except ValueError:
                print('Input type must be {0}.'.format(type_.__name__))
                continue
        if max_ is not None and Value > max_:
             print("Input must be less than or equal to {0}.".format(max_))
        elif min_ is not None and Value < min_:
            print("Input must be greater than or equal to {0}.".format(min_))
        elif range_ is not None and Value not in range_:
            if isinstance(range_, range):
                template = 'Input must be between {0.start} and {0.stop}.'
                print(template.format(range_))
            else:
                template = 'Input must be {0}.'
                if len(range_)== 1:
                    print(template.formate(*range_))
                else:
                     print(template.format(" or ".join((", ".join(map(str,range_[:-1])), str(range_[-1])))))
    
        else:
            return Value
        
        
def  AskQuestion(txt, type):
    while True:
        try:
            input = GetInput(txt, type)
            redo = GetInput("Må du fikse noe? (y/n): ", str)
            if str2bool(redo) == True:
                continue 
            else:
                break
            
        except ValueError:
            break
    return input