import Round from '@/api/models/Round'
import ContainerCollectionDay from '@/api/models/ContainerCollectionDay'

export default class DayPlanning {
  id: number;
  students: [number];
  time: ContainerCollectionDay;
  ronde: Round;
  status: [string];
}
