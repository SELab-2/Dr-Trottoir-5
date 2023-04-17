import Location from "@/api/models/Location";

export default class StudentTemplate {
  id: number;
  name: string;
  even: boolean;
  location: Location;
  status: string;
  start_hour: string;
  end_hour: string;
  year: number;
  week: number;
  rondes: [number];
  dag_planningnen: [number];
}
