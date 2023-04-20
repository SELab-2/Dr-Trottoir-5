import Round from "@/api/models/Round";
import PickupDay from "@/api/models/PickupDay";

export default class DayPlanning {
  id: number;
  students: [number];
  time: PickupDay;
  ronde: Round;
  status: [string];
}
