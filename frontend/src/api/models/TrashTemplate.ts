import {TrashTemplateStatus} from "@/api/models/TrashTemplateStatus";

export default class TrashTemplate {
  id: number;
  name: string;
  even: boolean;
  status: TrashTemplateStatus;
  year: number;
  week: number;
  location_id: number;
}
