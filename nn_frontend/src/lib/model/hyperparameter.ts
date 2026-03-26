

class Hyperparameter {
  // TODO: aggiungere vincolo di unicità
  public name: string
  // TODO: la mia idea e' che type non e' una stringa ma un tipo, voglio poter dichiarare
  // il tipo del mio hyperparameter senza doverlo successivamente mappare.
  public type: string

  constructor(name: string, type: string) {
    this.name = name;
    this.type = type;
  }
}
