class Planeta:
  """
  DOCUMENTAR
  """
  def __init__(self, temperaturaMitjana, quantitatAigua, radiacio, gravetat, distanciaSol):
    """
    DOCUMENTAR
    """
    self.temperaturaMitjana = temperaturaMitjana
    self.quantitatAigua = quantitatAigua
    self.radiacio = radiacio
    self.gravetat = gravetat
    self.distanciaSol = distanciaSol
  
  def set_distancia_al_sol(self, distanciaSol):
    """
    DOCUMENTAR (ja està acabat)
    """
    if (self.distanciaSol < 0):
      raise Exception("La distància no pot ser negativa")
    self.distanciaSol = distanciaSol

  def de_celsius_a_kelvin(self):
    """
    DOCUMENTAR
    """
    return self.temperaturaMitjana + 273
    
  def es_habitable(self, temperaturaMitjana, quantitatAigua, radiacio):
    """
    Comprobem que la temperatura mitjana estigui entre 20 i 45 graus Celsius (ambdós inclosos)
    la quantitat d'aigua al planeta sigui almenys del 40%
    tinguem menys de 25 unitats de radiació.

    Aconseguint que cuan el planeta sea habitable ens retorni 1 i cuan algun parametre esta raro donara 0
    """
    # ACABAR
    if 20 <= temperaturaMitjana <= 45 and quantitatAigua >= 45 and radiacio < 25:
      return 1
    else:
      return 0
    
  def pes_persona_en_newtons(self, gravetat):
    """
    Calculara el pes de la persona per el del planeta, despres el retornara amb pes de newtons
    """
    # ACABAR
    pesPersona = 25
    gravetat = 10.5
    pes_newtons = pesPersona * gravetat
    return pes_newtons
  
  def planeta_equilibrat(self, distanciaSol, radiacio):
    """
    Lo que fem aqui es que la cantitat d'aigua es la divisio entre distanciaSol y radiacio en format flotant,
    si la cantitat d'aigua es igual a 1 retornaria "1" de lo contrari retorna "0"
    """
    # ACABAR
    quantitat_aigua = distanciaSol / radiacio

    if quantitat_aigua == 1:
        return 1  
    else:
        return 0
