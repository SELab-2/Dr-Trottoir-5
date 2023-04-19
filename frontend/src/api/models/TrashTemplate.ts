import {TrashTemplateStatus} from "@/api/models/TrashTemplateStatus";

export default class TrashTemplate {
  id: number = 1;
  name: string = "";
  even: boolean = true;
  status: TrashTemplateStatus = TrashTemplateStatus.inactief;
  year: number = 2000;
  week: number = 1;
  location_id: number = 0;
}
