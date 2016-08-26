def save(file,*args,**kwargs):
  """
  Save the value of some data in a file.
  Usage: save('misdatos.pypic','a',b=b)
  """
  import cPickle
  f=open(file,"wb")
  dico = kwargs
  for name in args:
    dico[name] = eval(name)
  cPickle.dump(dico,f,protocol=-1)
  f.close
  
def restore(file):
    """
    Read data saved with save function.
    Usage: datos = restore('misdatos.pypic')
    """
    import cPickle
    f=open(file,"rb")
    result = cPickle.load(f)
    f.close
    return result