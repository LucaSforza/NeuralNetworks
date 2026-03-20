
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

export class ENode {
  public static counter: number = 0;
  public id: string;
  public position: { x: number; y: number };
  public data: Record<string, any>;
  public type: string

  constructor(x: number | null=null, y: number | null=null) {
    if (x === null || y === null) {
      x = Math.random() * 100;
      y = Math.random() * 100;
    }
    this.position = { x, y };
    this.id = "Node_" + ENode.counter++;
    this.data = {enode: this};
    this.type = "enode";
  }
}

export class Layer extends ENode {
  public static instances: number = 0;
  public name: string
  private hyperparameters: Array<Hyperparameter>

  constructor(name: string | null = null, x: number | null=null, y: number | null=null) {
    super(x, y);
    Layer.instances++;
    if (name === null) {
      name = "layer_" + (Layer.instances);
    }
    this.name = name;
    this.type = "layer";
    // TODO: La mia idea e' avere un file json che rappresenta una serie di
    // Layer comuni che noi forniamo agli utenti (inclusi i rispettivi hyperparameters)
    // cosi l'utente puo aggiungere layer che noi non abbiamo implementato.
    // Per questa ragione dentro il costruttore bisognera implementare il recupero degli
    // hyperparameters e inizializzarli con un valore di default.
    this.hyperparameters = [];
  }
}

export class Diagram {
  public nodes: Array<ENode> = $state([]);
  public edges: Array<any> = $state([]);

  constructor() {
  }

  public addLayer() {
    const l = new Layer();
    this.nodes = [...this.nodes, l];
  }

  public addConnection(conn: any) {
    console.log(conn.valueOf());
    this.edges = [...this.edges, conn];
  }

  public deleteNode(id: string) {    
    this.nodes = this.nodes.filter(node => node.id !== id);
    this.edges = this.edges.filter(edge => edge.source !== id && edge.target !== id);
  }

}
