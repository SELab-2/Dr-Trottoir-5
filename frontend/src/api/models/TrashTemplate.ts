import { TrashTemplateStatus } from '@/api/models/TrashTemplateStatus'
import Building from '@/api/models/Building'

export default class TrashTemplate {
  id: number = 1;
  name: string = '';
  even: boolean = true;
  status: TrashTemplateStatus = TrashTemplateStatus.inactief;
  year: number = 2000;
  week: number = 1;
  location: number = 0;
  buildings: Building[]
}
