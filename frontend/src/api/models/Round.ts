import Building from '@/api/models/Building'

export default class Round {
  id: number;
  name: string;
  location: number;
  buildings: [Building];
}
