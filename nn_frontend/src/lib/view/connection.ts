import { MarkerType } from '@xyflow/svelte';

export class VConnection {
  public id: string;
  public source: string; // Cambiato da ENode a string per compatibilità Flow
  public target: string;
  public type: string;
  public markerEnd: any;
  public style: string;

  constructor(id: string, source: string, target: string) {
    this.id = id;
    this.source = source;
    this.target = target;
    this.type = 'connection'; // Deve corrispondere alla chiave in edgeTypes

    this.markerEnd = {
      type: MarkerType.ArrowClosed,
      width: 20,
      height: 20,
      color: '#FF0072',
    };

    this.style = 'stroke: #FF0072; stroke-width: 2;';
  }

}
